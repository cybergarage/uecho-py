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

from uecho.transport import Manager

from .node import Node
from .node_profile import NodeProfile


class LocalNode(Manager):
    def __init__(self):
        super(LocalNode, self).__init__()
        self.TID = 0

    def next_TID(self):
        self.TID += 1
        if 0xFF < self.TID:
            self.TID = 0
        return self.TID

    def announce_message(self, msg):
        msg.TID = self.next_TID()
        msg.DEOJ = NodeProfile.OBJECT
        return super().announce_message(msg)
