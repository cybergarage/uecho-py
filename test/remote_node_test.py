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

from uecho.util import Bytes
from uecho import RemoteNode, Message, Object, Property, NodeProfile


def test_remote_node_parse():
    obj = Object()
    obj.set_code(0x0EF001)

    prop = Property()
    prop.code = NodeProfile.SELF_NODE_INSTANCE_LIST_S
    prop_data = bytearray([1])
    prop_data.extend(Bytes.from_int(obj.code, Object.CODE_SIZE))
    prop.data = prop_data

    msg = Message()
    msg.add_property(prop)

    node = RemoteNode()
    assert node.parse_message(msg)


def test_remote_node_parse_bytes():
    obj = Object()
    obj.set_code(0x0EF001)

    msg = Message()
    msg.parse_bytes(bytes.fromhex('108100010EF0010EF0017201D607020F2001029101'))

    node = RemoteNode()
    assert node.parse_message(msg)
    assert node.has_object(0x0F2001)
    assert node.has_object(0x029101)
