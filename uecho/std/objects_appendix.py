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
#
# To the extent possible under law, Sony Computer Science Laboratories, Inc has waived
# all copyright and related or neighboring rights to ECHONETLite-ObjectDatabase.
# This work is published from: Japan.
#
# GENERATED FROM objects.pl DO NOT EDIT THIS FILE.

from .object import Object
from .property import Property

__std_appendix_objects: dict = {}


def get_all_std_appendix_objects() -> dict:
    return __std_appendix_objects


# Mono functional lighting (0x02091)
obj = Object("Mono functional lighting", 0x02, 0x91)
obj.add_property(Property(0x80, "Operation status", "unsigned char", 1, "mandatory", "mandatory", "-", "mandatory"))
obj.add_property(Property(0xB0, "Illuminance level setting", "unsigned char", 1, "optional", "optional", "-", "-"))
__std_appendix_objects[(0x02, 0x91)] = obj

# Controller (0x05FF)
obj = Object("Controller", 0x05, 0xFF)
obj.add_property(Property(0x80, "Operation status", "unsigned char", 1, "mandatory", "optional", "-", "mandatory"))
__std_appendix_objects[(0x05, 0xFF)] = obj
