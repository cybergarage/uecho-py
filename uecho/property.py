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


class Property(object):
    """Property represents a property that includes the specification attributes and the dynamic data.
    """

    CODE_MIN = 0x80
    CODE_MAX = 0xFF

    GET = 0
    SET = 1
    ANNO = 2
    ANNO_STATUS = 3

    PROHIBITED = 0
    REQUIRED = 1
    OPTIONAL = 2

    code: int
    attrs: list[int]
    name: str
    size: int
    data: bytes
    anno_status: bool

    def __init__(self):
        self.code = 0
        self.data = bytes()
        self.attrs = [Property.PROHIBITED, Property.PROHIBITED, Property.PROHIBITED, Property.PROHIBITED]

    def set_attribute(self, typ: int, attr: int):
        self.attrs[typ] = attr

    def get_attribute(self, typ: int) -> int:
        return self.attrs[typ]

    def __is_attribute_enabled(self, val) -> bool:
        if (val & Property.REQUIRED):
            return True
        if (val & Property.OPTIONAL):
            return True
        return False

    def is_read_enabled(self) -> bool:
        return self.__is_attribute_enabled(self.attrs[Property.GET])

    def is_write_enabled(self) -> bool:
        return self.__is_attribute_enabled(self.attrs[Property.SET])

    def is_announce_enabled(self) -> bool:
        return self.__is_attribute_enabled(self.attrs[Property.ANNO])

    def is_status_change_required(self) -> bool:
        return self.__is_attribute_enabled(self.attrs[Property.ANNO_STATUS])
