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
from .esv import ESV


class LocalNode(Node, Manager):

    def __init__(self):
        super(Node, self).__init__()
        super(Manager, self).__init__()
        self.add_observer(self)

    def announce_message(self, proto_msg: ProtocolMessage) -> bool:
        proto_msg.SEOJ = NodeProfile.CODE
        return super().announce_message(proto_msg)

    def send_message(self, proto_msg: ProtocolMessage, addr) -> bool:
        proto_msg.SEOJ = NodeProfile.CODE
        return super().send_message(proto_msg, addr)

    def message_received(self, proto_msg: ProtocolMessage):
        # 4.2.1 Basic Sequences for Service Content
        req_msg = Message(proto_msg)

        dest_obj = self.get_object(req_msg.DEOJ)
        if dest_obj is None:
            return

        res_msg = dest_obj.message_received(req_msg)

        # (A) Basic sequence for receiving a request (no response required)
        if res_msg is None:
            return

        if res_msg.ESV != ESV.NOTIFICATION:
            # (C) Basic sequence for processing a notification request
            self.notify(res_msg)
        else:
            # (B) Basic sequence for receiving a request (response required)
            self.send_message(res_msg, req_msg.from_addr)
