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
from typing import Any, Union, Tuple, List

from .object import Object
from .property import Property
from .std import Database
from .message import Message


class DeviceListener(metaclass=abc.ABCMeta):
    """DeviceListener is an abstract listener class to listen to request messages to a device.
    """

    @abc.abstractmethod
    def property_read_requested(self, prop: Property):
        pass

    @abc.abstractmethod
    def property_write_requested(self, prop: Property, data: bytes):
        pass


class Device(Object):

    __listeners: List[DeviceListener]

    def __init__(self, code: Union[int, Tuple[int, int], Tuple[int, int, int], Any] = None):
        super().__init__()
        self.set_code(code)
        self.__listeners = []

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

    def message_received(self, msg: Message):
        if not isinstance(msg, Message):
            return

        for msg_prop in msg.properties:
            prop = self.get_property(msg_prop.code)
            if prop is None:
                continue
            for listener in self.__listeners:
                if msg.is_read_request():
                    listener.property_read_requested(self, prop)
                elif msg.is_write_request():
                    listener.property_write_requested(self, prop, msg_prop.data)
