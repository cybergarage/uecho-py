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

from uecho import RemoteNode, Message, Object


def test_remote_node():
    obj = Object()
    obj.set_code(0x0EF001)

    msg = Message()
    msg.add_object_as_class_instance_list_property(obj)

    node = RemoteNode()
    assert node.parse_message(msg)
