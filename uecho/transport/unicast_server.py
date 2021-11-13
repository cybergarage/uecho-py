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

import socket
from .server import Server
from .multicast_server import MulticastServer


class UnicastServer(Server):
    def __init__(self):
        super().__init__()

    def bind(self, ifaddr):
        self.socket = self.create_udp_socket()
        self.socket.bind((ifaddr, self.port))
        return True

    def announce_message(self, msg):
        if self.socket is None:
            return False
        return self.socket.sendto(msg.to_bytes(),
                                  (MulticastServer.ADDRESS, Server.PORT))
