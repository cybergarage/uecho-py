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
from typing import Any, Union, Tuple

from .object import Object
from .property import Property
from .std import Database
from .message import Message


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

        std_obj = Database().get_object(code)
        if isinstance(std_obj, Object):
            self._set_object_properties(std_obj)

        return True

    def set_listener(self, listener: DeviceListener) -> None:
        """ Sets a DeviceListener to handle read and write requests from other controllers and devices.

        Args:
            listener (DeviceListener): The listener that handles read and write requests from other controllers and devices.
        """
        self.__listener = listener

    def message_received(self, msg) -> bool:
        if not isinstance(msg, Message):
            return False

        if self.__listener is None:
            return False

        are_all_requests_accepted = True

        for msg_prop in msg.properties:
            prop = self.get_property(msg_prop.code)
            if prop is None:
                are_all_requests_accepted = False
                continue
            if msg.is_read_request():
                if not self.__listener.property_read_requested(self, prop):
                    are_all_requests_accepted = False
            elif msg.is_write_request():
                if not self.__listener.property_write_requested(self, prop, msg_prop.data):
                    are_all_requests_accepted = False

        return are_all_requests_accepted
