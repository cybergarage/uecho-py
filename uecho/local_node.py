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

from typing import List
from .transport.manager import Manager
from .node import Node
from .node_profile import NodeProfile
from .protocol.message import Message as ProtocolMessage
from .message import Message
from .esv import ESV
from .object import Object


class LocalNode(Node):

    __manager: Manager
    __node_profile_obj: NodeProfile

    def __init__(self):
        super().__init__()
        self.__manager = Manager()
        self.__manager.add_observer(self)
        self.__node_profile_obj = NodeProfile()
        self.add_object(self.__node_profile_obj)

    def add_object(self, obj: Object) -> bool:
        return super().add_object(obj)

    def add_observer(self, observer):
        return self.__manager.add_observer(observer)

    def announce_message(self, msg: Message) -> bool:
        return self.__manager.announce_message(msg)

    def send_message(self, msg: Message, addr) -> bool:
        return self.__manager.send_message(msg, addr)

    def start(self, ifaddrs: List[str] = []) -> bool:
        return self.__manager.start()

    def stop(self) -> bool:
        return self.__manager.stop()

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
            self.announce_message(res_msg)
        else:
            # (B) Basic sequence for receiving a request (response required)
            self.send_message(res_msg, req_msg.from_addr)
