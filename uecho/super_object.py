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

import random

from typing import Any, Union, Tuple, List
from .object import Object
from .util.bytes import Bytes
from .property import Property, is_propertymap_description_format1


class SuperObject(Object):

    CODE = 0x000000

    def __init__(self, code: Union[int, Tuple[int, int], Tuple[int, int, int], Any] = None):
        super().__init__(code)
        self.set_request_handler(self)

    def add_property(self, prop: Property) -> bool:
        if not super().add_property(prop):
            return False
        self._update_property_map_properties()
        return True

    def _set_object_properties(self, obj) -> bool:
        if not isinstance(obj, Object):
            return False
        self.name = obj.name
        for obj_prop in obj.properties:
            prop = obj_prop.copy()
            self.add_property(prop)
        return True

    def __set_property_map_property(self, code: int, prop_map: List[int]) -> bool:
        # Map property is not added yet.
        if not self.has_property(code):
            return False

        map_bytes = bytearray(bytes([len(prop_map)]))
        for prop_code in prop_map:
            map_bytes.extend(bytes([prop_code]))

        # Description Format 1

        if is_propertymap_description_format1(len(prop_map)):
            map_bytes = bytearray(bytes([len(prop_map)]))
            for prop_code in prop_map:
                map_bytes.extend(bytes([prop_code]))
            return self.set_property_data(code, map_bytes)

        # Description Format 2

        prop_map_codes = [0] * Property.PROPERTYMAP_FORMAT2_MAP_SIZE
        for prop_code in prop_map:
            # 0 <= propCodeIdx <= 15
            prop_code_idx = ((prop_code - Property.CODE_MIN) & 0x0F)
            # 0 <= propCodeIdx <= 7
            prop_code_bit = ((((prop_code - Property.CODE_MIN) & 0xF0) >> 4) & 0x0F)
            prop_map_codes[prop_code_idx] |= ((0x01 << prop_code_bit) & 0x0F)
        map_bytes = bytearray(bytes([Property.PROPERTYMAP_FORMAT2_MAP_SIZE]))
        for prop_map_code in prop_map_codes:
            map_bytes.extend(bytes([prop_map_code]))
        return self.set_property_data(code, map_bytes)

    def _update_property_map_properties(self) -> bool:
        anno_list = []
        get_list = []
        set_list = []
        for prop in self.properties:
            if prop.is_announce_required():
                anno_list.append(prop.code)
            if prop.is_read_enabled():
                get_list.append(prop.code)
            if prop.is_write_enabled():
                set_list.append(prop.code)
        anno_map = list(set(anno_list))
        get_map = list(set(get_list))
        set_map = list(set(set_list))
        if not self.__set_property_map_property(SuperObject.ANNO_PROPERTY_MAP, anno_map):
            return False
        if not self.__set_property_map_property(SuperObject.GET_PROPERTY_MAP, get_map):
            return False
        if not self.__set_property_map_property(SuperObject.SET_PROPERTY_MAP, set_map):
            return False
        return True

    def property_read_requested(self, prop: Property) -> bool:
        obj_prop = self.get_property(prop.code)
        if obj_prop is None:
            return False
        return obj_prop.is_read_enabled()

    def property_write_requested(self, prop: Property, data: bytes) -> bool:
        obj_prop = self.get_property(prop.code)
        if obj_prop is None:
            return False
        return obj_prop.is_write_enabled()


class SuperObjectReadOnly(SuperObject):
    CODE = 0x0EF002

    def __init__(self):
        super().__init__()
        self.set_code(SuperObjectReadOnly.CODE)
