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


class Object(object):
    OBJECT_OPERATING_STATUS = 0x80
    OBJECT_MANUFACTURER_CODE = 0x8A
    OBJECT_ANNO_PROPERTY_MAP = 0x9D
    OBJECT_SET_PROPERTY_MAP = 0x9E
    OBJECT_GET_PROPERTY_MAP = 0x9F

    OBJECT_OPERATING_STATUS_ON = 0x30
    OBJECT_OPERATING_STATUS_OFF = 0x31
    OBJECT_OPERATING_STATUS_SIZE = 1
    OBJECT_MANUFACTURER_EVALUATION_CODE_MIN = 0xFFFFF0
    OBJECT_MANUFACTURER_EVALUATION_CODE_MAX = 0xFFFFFF
    OBJECT_MANUFACTURER_CODE_SIZE = 3
    OBJECT_PROPERTY_MAP_MAX_SIZE = 16
    OBJECT_ANNO_PROPERTY_MAP_MAX_SIZE = OBJECT_PROPERTY_MAP_MAX_SIZE + 1
    OBJECT_SET_PROPERTY_MAP_MAX_SIZE = OBJECT_PROPERTY_MAP_MAX_SIZE + 1
    OBJECT_GET_PROPERTY_MAP_MAX_SIZE = OBJECT_PROPERTY_MAP_MAX_SIZE + 1

    OBJECT_MANUFACTURER_UNKNOWN = OBJECT_MANUFACTURER_EVALUATION_CODE_MIN

    def __init__(self):
        self.code = 0
        self.class_group_code = 0
        self.class_code = 0
        self.instance_code = 0
        pass

    def set_code(self, code):
        if type(code) is int:
            self.code = code
            self.class_group_code = ((code >> 16) & 0xFF)
            self.class_code = ((code >> 8) & 0xFF)
            self.instance_code = (code & 0xFF)
            return True
        return False
