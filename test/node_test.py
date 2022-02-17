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

from uecho import Node, LocalNode, IGNORE_SELF_MESSAGE
from uecho.std import Database


def test_node():
    node = Node()
    addr = ('127.0.0.1', 80)
    assert node.set_address(addr)
    assert node.ip == addr[0]
    assert node.port == Node.PORT

    obj = Database().get_object((0x02, 0x91)).copy()
    obj.set_code(0x029101)
    node.add_object(obj)
    assert node.get_object(0x029100) is None
    assert node.get_object(0x029101)
    assert node.get_object((0x02, 0x91, 0x00)) is None
    assert node.get_object((0x02, 0x91, 0x01))


def test_local_node():
    node = LocalNode()
    assert node.is_enabled(IGNORE_SELF_MESSAGE)
    assert node.set_enabled(IGNORE_SELF_MESSAGE, False)
    assert not node.is_enabled(IGNORE_SELF_MESSAGE)
