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

import copy
from typing import List, Optional, Any
from .protocol.property import Property as ProtocolProperty
from .protocol.message import Message
from uecho.util import Bytes


def is_propertymap_description_format1(n: int) -> bool:
    return n <= Property.PROPERTYMAP_FORMAT1_MAX_SIZE


def is_propertymap_description_format2(n: int) -> bool:
    return is_propertymap_description_format1(n)


class Property(ProtocolProperty):
    """Property represents a property of ECHONET Lite, and it includes the specification attributes and the dynamic data.
    """

    PROPERTYMAP_FORMAT1_MAX_SIZE = 15
    PROPERTYMAP_FORMAT2_MAP_SIZE = 16
    PROPERTYMAP_FORMAT_MAX_SIZE = PROPERTYMAP_FORMAT2_MAP_SIZE + 1

    CODE_MIN = 0x80
    CODE_MAX = 0xFF

    GET = 0
    SET = 1
    ANNO = 2

    PROHIBITED = 0
    REQUIRED = 1
    OPTIONAL = 2

    attrs: List[int]
    name: str
    size: int
    anno_status: bool
    object: Optional[Any]

    def __init__(self, code: int = 0, data: bytes = bytes()):
        super().__init__(code, data)
        self.attrs = [Property.PROHIBITED, Property.PROHIBITED, Property.PROHIBITED]
        self.object = None

    def set_attribute(self, typ: int, attr: int):
        self.attrs[typ] = attr

    def get_attribute(self, typ: int) -> int:
        return self.attrs[typ]

    def __is_attribute_enabled(self, val) -> bool:
        if val == Property.REQUIRED:
            return True
        if val == Property.OPTIONAL:
            return True
        return False

    def __is_attribute_required(self, val) -> bool:
        if val == Property.REQUIRED:
            return True
        return False

    def is_mandatory(self) -> bool:
        for attr in self.attrs:
            if attr == Property.REQUIRED:
                return True
        return False

    def is_read_enabled(self) -> bool:
        return self.__is_attribute_enabled(self.attrs[Property.GET])

    def is_write_enabled(self) -> bool:
        return self.__is_attribute_enabled(self.attrs[Property.SET])

    def is_announce_enabled(self) -> bool:
        return self.__is_attribute_enabled(self.attrs[Property.ANNO])

    def is_read_required(self) -> bool:
        return self.__is_attribute_required(self.attrs[Property.GET])

    def is_write_required(self) -> bool:
        return self.__is_attribute_required(self.attrs[Property.SET])

    def is_announce_required(self) -> bool:
        return self.__is_attribute_required(self.attrs[Property.ANNO])

    def send_message(self, esv: int, data: bytes = bytearray()) -> bool:
        """Sends a unicast message to the property asynchronously.


        Args:
            esv (int): A service type of ECHONET Lite.
            data (bytes, optional): : A property data. Defaults to bytearray().

        Returns:
            bool: True if successful, otherwise False.
        """
        return self.object.send_message(esv, [(self.code, data)])

    def post_message(self, esv: int, data: bytes = bytearray()) -> Optional[Message]:
        """Posts a unicast message to the property and return the response message synchronously.

        Args:
            esv (int): A service type of ECHONET Lite.
            data (bytes, optional): A property data. Defaults to bytearray().

        Returns:
            Optional[Message]: The response message if successful receiving the response message, otherwise None.
        """
        return self.object.post_message(esv, [(self.code, data)])

    @property
    def bytes(self):
        return self.data

    @property
    def number(self):
        return Bytes.to_int(self.data)

    @property
    def property_map_codes(self):
        if len(self.data) < 1:
            return None
        prop_map_code_cnt = self.data[0]

        # Description Format 1

        if is_propertymap_description_format1(prop_map_code_cnt):
            prop_codes = []
            if len(self.data) != (prop_map_code_cnt + 1):
                return False
            for n in range(prop_map_code_cnt):
                prop_codes.append(int(self.data[(n + 1)]))
            return prop_codes

        # Description Format 2

        if len(self.data) != (Property.PROPERTYMAP_FORMAT2_MAP_SIZE + 1):
            return None

        prop_codes = [0] * prop_map_code_cnt
        prop_code_idx = 0
        for i in range(Property.PROPERTYMAP_FORMAT2_MAP_SIZE):
            prop_byte_code = self.data[i + 1]
            for j in range(8):
                prop_byte_bit = (0x01 << j) & 0x0F
                if ((prop_byte_code & prop_byte_bit) == 0):
                    continue
                if prop_map_code_cnt <= prop_code_idx:
                    continue
                code = (0x10 * j) + Property.CODE_MIN
                code += i
                prop_codes[prop_code_idx] = code
                prop_code_idx = prop_code_idx + 1
        return prop_codes

    def copy(self):
        return copy.deepcopy(self)

    def copy(self):
        return copy.deepcopy(self)
