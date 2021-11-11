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
from abc import ABCMeta, abstractmethod


class Server(metaclass=ABCMeta):
    PORT = 3610

    # socket: socket.socket
    # port: int

    def __init__(self):
        self.socket = None
        self.port = Server.PORT

    def create_udp_socket(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
        return sock

    @abstractmethod
    def bind(self, ifaddr):
        pass

    def start(self):
        if self.socket is None:
            return False
        return True

    def stop(self):
        if self.socket is None:
            return False
        self.socket.close()
        self.socket = None
        return True
