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

from .interface import Interface
from .server import Server, Server
from .multicast_server import MulticastServer
from .unicast_server import UnicastServer
# from typing import List


class MessageManager(object):
    # servers: List[Server]

    def __init__(self):
        self.servers = []
        pass

    def add_observer(self, observer):
        for server in self.servers:
            server.add_observer(observer)

    def notify(self, msg):
        for server in self.servers:
            server.notify(msg)

    def start(self):
        for ifaddr in Interface.get_all_ipaddrs():
            userver = UnicastServer()
            if not userver.bind(ifaddr):
                self.stop()
                return False
            if not userver.start():
                self.stop()
                return False
            self.servers.append(userver)

            mserver = MulticastServer()
            if not mserver.bind(ifaddr):
                self.stop()
                return False
            if not mserver.start():
                self.stop()
                return False
            self.servers.append(mserver)

        return True

    def stop(self):
        for server in self.servers:
            server.stop()
        self.servers = []
        return True