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

from uecho.std import Database, Property


def test_database():
    db = Database()

    assert db.get_object(0x00, 0x00) is None

    obj = db.get_object(0x00, 0x01)
    assert (obj)

    expecteds = [
        [0x80, Property.REQUIRED, Property.OPTIONAL, Property.PROHIBITED, Property.REQUIRED],
        [0xB0, Property.OPTIONAL, Property.OPTIONAL, Property.PROHIBITED, Property.PROHIBITED],
        [0xB1, Property.REQUIRED, Property.PROHIBITED, Property.PROHIBITED, Property.REQUIRED],
        [0xBF, Property.PROHIBITED, Property.OPTIONAL, Property.PROHIBITED, Property.PROHIBITED],
    ]

    assert obj.get_property(0x00) is None
    for expected in expecteds:
        prop = obj.get_property(expected[0])
        assert prop
        assert prop.get_attribute(Property.GET) == expected[1]
        assert prop.get_attribute(Property.SET) == expected[2]
        assert prop.get_attribute(Property.ANNO) == expected[3]
        assert prop.get_attribute(Property.ANNO_STATUS) == expected[4]
