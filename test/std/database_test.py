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


def test_manufacture_database():
    db = Database()

    expecteds = [
        ["Panasonic", 0x00000B],
        ["Panasonic", bytes([0x00, 0x00, 0x0B])],
        ["Panasonic", bytearray([0x00, 0x00, 0x0B])],
        ["Sharp", 0x000005],
        ["Sharp", bytes([0x00, 0x00, 0x05])],
        ["Sharp", bytearray([0x00, 0x00, 0x05])],
    ]

    for expected in expecteds:
        man = db.get_manufacturer(expected[1])
        assert man
        assert man.name.startswith(expected[0])


def test_object_database():
    db = Database()

    obj = db.get_object((0x00, 0x01))
    assert (obj)

    expecteds = [
        [0x80, Property.REQUIRED, Property.OPTIONAL, Property.REQUIRED],
        [0xB0, Property.OPTIONAL, Property.OPTIONAL, Property.PROHIBITED],
        [0xB1, Property.REQUIRED, Property.PROHIBITED, Property.REQUIRED],
        [0xBF, Property.PROHIBITED, Property.OPTIONAL, Property.PROHIBITED],
    ]

    assert obj.get_property(0x00) is None
    for expected in expecteds:
        prop = obj.get_property(expected[0])
        assert prop
        assert prop.get_attribute(Property.GET) == expected[1]
        assert prop.get_attribute(Property.SET) == expected[2]
        assert prop.get_attribute(Property.ANNO) == expected[3]


def test_mra_object_database():
    db = Database()

    obj = db.get_object((0x02, 0x91))
    assert (obj)

    expecteds = [
        [0x80, Property.REQUIRED, Property.REQUIRED, Property.REQUIRED],
        [0xB0, Property.OPTIONAL, Property.OPTIONAL, Property.OPTIONAL],
    ]

    assert obj.get_property(0x00) is None
    for expected in expecteds:
        prop = obj.get_property(expected[0])
        assert prop
        assert prop.get_attribute(Property.GET) == expected[1]
        assert prop.get_attribute(Property.SET) == expected[2]
        assert prop.get_attribute(Property.ANNO) == expected[3]
