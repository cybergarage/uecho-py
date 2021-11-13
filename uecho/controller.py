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
from .remote_node import RemoteNode


class SearchMessage(Message):
    def __init__(self):
        super(SearchMessage, self).__init__()
        self.ESV = ESV.READ_REQUEST
        self.SEOJ = NodeProfile.OBJECT
        self.DEOJ = NodeProfile.OBJECT
        prop = Property()
        prop.code = NodeProfile.CLASS_SELF_NODE_INSTANCE_LIST_S
        prop.data = bytearray()
        self.add_property(prop)


class Controller(Observer):
    def __init__(self):
        self.node = LocalNode()
        self.found_nodes = {}

    @property
    def nodes(self):
        nodes = []
        for node in self.found_nodes.values():
            nodes.append(node)
        return nodes

    def __is_node_profile_message(self, msg):
        if msg.ESV != ESV.NOTIFICATION and msg.ESV != ESV.READ_RESPONSE:
            return False
        if msg.DEOJ != NodeProfile.OBJECT and msg.DEOJ != NodeProfile.OBJECT_READ_ONLY:
            return False
        return True

    def __add_found_node(self, node):
        self.found_nodes[node.ip] = node

    def message_received(self, msg):
        log.debug('%s %s' % (msg.from_addr[0].ljust(15), msg.to_string()))
        if self.__is_node_profile_message(msg):
            node = RemoteNode()
            node.set_address(msg.from_addr)
            if node.parse_message(msg):
                self.__add_found_node(node)

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
