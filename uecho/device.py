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

from typing import Any, Union, Tuple

from .object import Object
from .std import Database


class Device(Object):

    SUPER_CLASS_CODE = 0x0000

    def __init__(self, code: Union[int, Tuple[int, int], Tuple[int, int, int], Any]):
        super().__init__()
        self.set_code(code)

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
