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

    class Test:

        def __init__(self, code: int, len: int, func):
            self.code = code
            self.len = len
            self.func = func

    tests = [
        Test(NodeProfile.OPERATING_STATUS, NodeProfile.OPERATING_STATUS_SIZE, (lambda prop: prop.number == NodeProfile.BOOTING)),
        Test(NodeProfile.IDENTIFICATION_NUMBER, NodeProfile.IDENTIFICATION_NUMBER_SIZE, None),
        Test(NodeProfile.NUMBER_OF_SELF_NODE_INSTANCES, NodeProfile.NUMBER_OF_SELF_NODE_INSTANCES_SIZE, (lambda prop: prop.number == 0)),
        Test(NodeProfile.NUMBER_OF_SELF_NODE_CLASSES, NodeProfile.NUMBER_OF_SELF_NODE_CLASSES_SIZE, (lambda prop: prop.number == 1)),
    ]

    for test in tests:
        prof = NodeProfile()
        prop = prof.get_property(test.code)
        assert len(prop.data) == test.len
        assert prop
        if test.func is not None:
            assert test.func(prop)
