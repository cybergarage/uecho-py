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

import uecho.log as log
from uecho.transport import Observer

from .local_node import LocalNode
from .node_profile import NodeProfile
from .esv import ESV
from .message import Message
from .property import Property


class SearchMessage(Message):
    def __init__(self):
        super(SearchMessage, self).__init__()
        self.ESV = ESV.READ_REQUEST
        self.SEOJ = NodeProfile.OBJECT
        self.DEOJ = NodeProfile.OBJECT
        prop = Property()
        prop.code = NodeProfile.CLASS_SELF_NODE_CLASS_LIST_S
        prop.data = bytearray()
        self.add_property(prop)


class Controller(Observer):
    def __init__(self):
        self.node = LocalNode()

    def message_received(self, msg):
        log.debug(msg.to_string())

    def search(self):
        msg = SearchMessage()
        return self.node.announce_message(msg)

    def start(self):
        if not self.node.start():
            return False
        self.node.add_observer(self)
        return True

    def stop(self):
        if not self.node.stop():
            return False
        return True
