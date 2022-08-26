# Copyright (C) 2021 Satoshi Konno. All rights reserved.
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

from .super_object import SuperObject
from .object import Object
from .std import Database


class Profile(SuperObject):

    def __init__(self, code: Union[int, Tuple[int, int], Tuple[int, int, int], Any] = None):
        super().__init__()
        std_obj = Database().get_object(SuperObject.CODE)
        if isinstance(std_obj, Object):
            self._set_object_properties(std_obj)
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
        std_obj = Database().get_object(code)
        if isinstance(std_obj, Object):
            self._set_object_properties(std_obj)
        return self._update_property_map_properties()
