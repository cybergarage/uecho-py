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

from .object import Object


class Node(object):
    def __init__(self):
        self.__address = ()
        self.objects = []

    def set_address(self, addr):
        if not isinstance(addr, tuple) or len(addr) != 2:
            return False
        self.__address = addr
        return True

    @property
    def addr(self):
        return self.__address[0]

    @property
    def port(self):
        return self.__address[1]

    def add_object(self, obj):
        if not isinstance(obj, Object):
            return False
        self.objects.append(obj)
        return True
