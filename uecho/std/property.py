# Copyright (C) 2021 The uecho-py Authors. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
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

from typing import Any


class Property(object):
    GET = 0
    SET = 1
    ANNO = 2
    ANNO_STATUS = 3

    NONE = 0
    REQUIRED = 1
    OPTIONAL = 2

    code: int
    name: str
    typ: str
    size: int
    get: int
    set: int
    anno: int
    anno_status: int

    def __init__(self, code: int, name: str, typ: str, size: int, get: Any, set: Any, anno: Any, chg: Any):
        self.code = code
        self.name = name
        self.typ = typ
        self.size = size
        self.get = self.__to_attribute(get)
        self.set = self.__to_attribute(set)
        self.anno = self.__to_attribute(anno)
        self.anno_status = self.__to_attribute(chg)

    def __to_attribute(self, val: Any) -> int:
        attr = Property.NONE
        if isinstance(val, int):
            attr = val
        if isinstance(val, str):
            if val.lower() == "mandatory":
                attr = Property.REQUIRED
            elif val.lower() == "optional":
                attr = Property.OPTIONAL
        return attr

    def attribute(self, typ: int) -> int:
        if typ == Property.GET:
            return self.get
        if typ == Property.SET:
            return self.set
        if typ == Property.ANNO:
            return self.anno
        if typ == Property.ANNO_STATUS:
            return self.anno_status
        return Property.NONE
