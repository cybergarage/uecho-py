# Copyright (C) 2021 The uecho-py Authors. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License")
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

import abc

from .object import Object
from .property import Property
from .remote_node import RemoteNode


class DeviceListener(metaclass=abc.ABCMeta):
    """DeviceListener is an abstract listener class to listen to request messages to a device.
    """

    @abc.abstractmethod
    def property_requested(self, node: RemoteNode, obj: Object, prop: Property):
        pass


class Device(Object):

    def __init__(self):
        pass
