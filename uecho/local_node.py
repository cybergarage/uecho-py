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

from .transport.manager import Manager
from .node import Node
from .node_profile import NodeProfile
from .protocol.message import Message as ProtocolMessage
from .message import Message


class LocalNode(Node, Manager):

    def __init__(self):
        super(Node, self).__init__()
        super(Manager, self).__init__()

    def announce_message(self, proto_msg: ProtocolMessage) -> bool:
        proto_msg.SEOJ = NodeProfile.CODE
        return super().announce_message(proto_msg)

    def send_message(self, proto_msg: ProtocolMessage, addr) -> bool:
        proto_msg.SEOJ = NodeProfile.CODE
        return super().send_message(proto_msg, addr)

    def message_received(self, proto_msg: ProtocolMessage):
        msg = Message(proto_msg)
        obj = self.get_object(msg.DEOJ)
        if obj is None:
            return
        obj.message_received(msg)
