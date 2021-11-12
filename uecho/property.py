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

import uecho.protocol


class Property(uecho.protocol.Property):
    PROPERTY_CODE_MIN = 0x80
    PROPERTY_CODE_MAX = 0xFF

    PROPERTY_MAP_FORMAT1_MAX_SIZE = 15
    PROPERTY_MAP_FORMAT2_SIZE = 18
    PROPERTY_MAP_FORMAT_MAX_SIZE = PROPERTY_MAP_FORMAT2_SIZE

    PROPERTY_ATTRIBUTE_NONE = 0x00
    PROPERTY_ATTRIBUTE_READ = 0x01
    PROPERTY_ATTRIBUTE_WRITE = 0x02
    PROPERTY_ATTRIBUTE_ANNO = 0x10
    PROPERTY_ATTRIBUTE_READ_WRITE = PROPERTY_ATTRIBUTE_READ | PROPERTY_ATTRIBUTE_WRITE
    PROPERTY_ATTRIBUTE_READ_ANNO = PROPERTY_ATTRIBUTE_READ | PROPERTY_ATTRIBUTE_ANNO

    def __init__(self):
        super().__init__()
