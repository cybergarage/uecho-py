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

from uecho import Controller, RemoteNode
from uecho.protocol import Message


def test_controller():
    ctrl = Controller()
    assert ctrl.start()
    assert ctrl.search()
    assert ctrl.stop()


def test_controllermessage_received():
    msg_strs = ["108100010EF0010EF0017201D6040105FF01", "108100010EF0010EF0017201D607020F2001029101"]

    for msg_str in msg_strs:
        msg = Message()
        msg.from_addr = ("127.0.0.1", 80)
        assert msg.parse_hexstring(msg_str)
        ctrl = Controller()
        ctrl.message_received(msg)


def test_controller_nodes():
    ctrl = Controller()
    addr = ("127.0.0.1", 80)
    node = RemoteNode(addr)
    assert ctrl._add_found_node(node)
    assert ctrl.get_node(addr[0])
    assert ctrl.get_node(addr)
    assert ctrl.get_node("localhost")
