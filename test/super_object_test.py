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

from uecho import Device
from uecho.util import Bytes


def test_super_object():

    obj_codes = [
        0x0EF0, # Node profile 
        0x02A6, # Hybrid water heater 
    ]

    prop_codes = [
        Device.ANNO_PROPERTY_MAP,
        Device.GET_PROPERTY_MAP,
        Device.SET_PROPERTY_MAP,
    ]

    for obj_code in obj_codes:
        obj = Device(obj_code)
        for prop_code in prop_codes:
            obj.set_code(prop_code)
            expected_prop_map_codes = []
            for prop in obj.properties:
                if prop_code == Device.ANNO_PROPERTY_MAP and prop.is_announce_required():
                    expected_prop_map_codes.append(prop.code)
                if prop_code == Device.GET_PROPERTY_MAP and prop.is_read_enabled():
                    expected_prop_map_codes.append(prop.code)
                if prop_code == Device.SET_PROPERTY_MAP and prop.is_write_enabled():
                    expected_prop_map_codes.append(prop.code)
            prop = obj.get_property(prop_code)
            assert prop
            if prop is None:
                continue
            prop_map_codes = prop.property_map_codes
            assert prop_map_codes
            if prop_map_codes is None:
                continue
            assert set(prop_map_codes) == set(expected_prop_map_codes)
