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

from uecho import Object, Property


def test_object_code():
    obj = Object()
    assert obj.set_code(0x0EF001)
    assert obj.code == 0x0EF001
    assert obj.group_code == 0x0E
    assert obj.class_code == 0xF0
    assert obj.instance_code == 0x01


def test_object_tuple_code():
    obj = Object()
    assert obj.set_code((0x0E, 0xF0, 0x01))
    assert obj.code == 0x0EF001
    assert obj.group_code == 0x0E
    assert obj.class_code == 0xF0
    assert obj.instance_code == 0x01


def test_object_tuple_group_class_code():
    obj = Object()
    assert obj.set_code((0x0E, 0xF0))
    assert obj.code == 0x0EF000
    assert obj.group_code == 0x0E
    assert obj.class_code == 0xF0
    assert obj.instance_code == 0x00


def test_property():
    prop = Property()
    assert prop.code == 0
    assert len(prop.data) == 0
