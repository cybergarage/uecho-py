# Copyright (C) 2021 The uecho-py Authors. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License")
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http:#www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import abc
from typing import Any, Union, Tuple, Optional

from .object import Object
from .property import Property
from .message import Message
from .std import Database
from .esv import ESV


class DeviceListener(metaclass=abc.ABCMeta):
    """DeviceListener is an abstract listener class to listen to request messages to a device.
    """

    @abc.abstractmethod
    def property_read_requested(self, prop: Property) -> bool:
        """ Handles a read request message, and updates the propery data if needed.

        Args:
            prop (Property): The target property.

        Returns:
            bool: True if allowed the access, otherwise False.
        """
        pass

    @abc.abstractmethod
    def property_write_requested(self, prop: Property, data: bytes) -> bool:
        """ Handles a write request message, and updates the propery data by the specified data if allowed.

        Args:
            prop (Property): The target property.
            data (bytes): The update data.

        Returns:
            bool: True if allowed the update, otherwise False.
        """
        pass


class Device(Object):

    SUPER_CLASS_CODE = 0x0000

    __listener: DeviceListener

    def __init__(self, code: Union[int, Tuple[int, int], Tuple[int, int, int], Any] = None):
        super().__init__()
        self.set_code(code)
        self.__listener = None

    def set_code(self, code: Union[int, Tuple[int, int], Tuple[int, int, int], Any]) -> bool:
        """Sets the spcecified code as the object code.

        Args:
            code (Union[int, Tuple[int, int], Tuple[int, int, int], Any]): A code or tuple code.

        Returns:
            bool: True if the specified code is valid, otherwise False.
        """
        if not super().set_code(code):
            return False

        std_db = Database()
        if not self._set_object_properties(std_db.get_object(Device.SUPER_CLASS_CODE)):
            return False
        if not self._set_object_properties(std_db.get_object(code)):
            return False

        return True

    def set_listener(self, listener: DeviceListener) -> bool:
        """ Sets a DeviceListener to handle read and write requests from other controllers and devices.

        Args:
            listener (DeviceListener): The listener that handles read and write requests from other controllers and devices.
        """
        if not isinstance(listener, DeviceListener):
            return False
        self.__listener = listener
        return True

    def message_received(self, req_msg: Message) -> Optional[Message]:
        if not isinstance(req_msg, Message):
            return None

        if self.__listener is None:
            return None

        accepted_request_cnt = 0
        res_msg = Message()
        res_msg.set_response_headert(req_msg)

        for msg_prop in req_msg.all_properties:
            res_prop = Property(msg_prop.code)

            obj_prop = self.get_property(msg_prop.code)
            if obj_prop is not None:
                if req_msg.is_read_request():
                    if self.__listener.property_read_requested(self, obj_prop):
                        res_prop.data = obj_prop.data
                        accepted_request_cnt += 1
                elif req_msg.is_write_request():
                    if self.__listener.property_write_requested(self, obj_prop, msg_prop.data):
                        accepted_request_cnt += 1
                    else:
                        res_prop.data = obj_prop.data

            req_msg.add_property(res_prop)

        opc = req_msg.OPC

        # 4.2.3.1 Property value write service (no response required) [0x60, 0x50]
        if req_msg.ESV == ESV.WRITE_REQUEST:
            if accepted_request_cnt == opc:
                return None
            else:
                res_msg.ESV = ESV.WRITE_REQUEST_ERROR

        res_msg.ESV = req_msg.ESV
        if req_msg.is_read_request():
            if accepted_request_cnt == opc:
                res_msg.ESV = ESV.READ_RESPONSE
            else:
                res_msg.ESV = ESV.READ_REQUEST_ERROR
        elif req_msg.is_write_request():
            if accepted_request_cnt == opc:
                res_msg.ESV = ESV.WRITE_RESPONSE
            else:
                res_msg.ESV = ESV.READ_REQUEST_ERROR

        return res_msg
