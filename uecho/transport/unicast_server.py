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

from typing import Optional, Tuple
from .server import Server
from .multicast_server import MulticastServer
from ..protocol.message import Message
from ..log.logger import debug


class UnicastServer(Server):

    def __init__(self):
        super().__init__()

    def bind(self, ifaddr: str) -> bool:
        if not super().bind(ifaddr):
            return False
        self.sock = self.create_udp_socket()
        self.sock.bind((ifaddr, self.port))
        return True

    def announce_message(self, msg: Message) -> bool:
        if self.sock is None:
            return False
        to_addr = (MulticastServer.ADDRESS, Server.PORT)
        msg.to_addr = to_addr
        debug('-> %s:%s %s' % (MulticastServer.ADDRESS.ljust(15), str(Server.PORT).ljust(5), msg.to_string()))
        if self.sock.sendto(msg.to_bytes(), to_addr) <= 0:
            return False
        return True

    def send_message(self, msg: Message, addr: Optional[Tuple[str, int]]) -> bool:
        if not isinstance(addr, tuple) or len(addr) != 2:
            return False
        if self.sock is None:
            return False
        msg.to_addr = addr
        debug('%s <- %s' % (addr[0].ljust(15), msg.to_string()))
        if self.sock.sendto(msg.to_bytes(), addr) <= 0:
            return False
        return True
