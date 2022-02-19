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

from uecho import NodeProfile
from uecho.util import Bytes


def test_node_profile():
    prof = NodeProfile()

    prop = prof.get_property(NodeProfile.NUMBER_OF_SELF_NODE_INSTANCES)
    assert prop
    assert len(prop.data) == NodeProfile.NUMBER_OF_SELF_NODE_INSTANCES_SIZE
    assert Bytes.to_int(prop.data) == 0

    prop = prof.get_property(NodeProfile.NUMBER_OF_SELF_NODE_CLASSES)
    assert prop
    assert len(prop.data) == NodeProfile.NUMBER_OF_SELF_NODE_CLASSES_SIZE
    assert Bytes.to_int(prop.data) == 1
