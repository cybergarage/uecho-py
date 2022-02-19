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

import time
from uecho import Device, ObjectListener, Property, Controller, IGNORE_SELF_MESSAGE


class MonoLight(Device, ObjectListener):

    def __init__(self):
        super().__init__()

    def property_read_requested(self, prop: Property) -> bool:
        pass

    def property_write_requested(self, prop: Property, data: bytes) -> bool:
        pass


def create_test_device():
    dev = MonoLight()
    assert dev.set_code(0x029101)    # Mono functional lighting

    # Mandatory properties of device super class
    assert dev.has_property(0x80)    # Operation status
    assert dev.has_property(0x8A)    # Manufacturer code
    # Mandatory properties of mono functional lighting
    assert dev.has_property(0x80)    # Operation status
    assert dev.has_property(0xB0)    # Illuminance Level Setting

    assert dev.set_listener(dev)

    return dev


def test_device():
    ctrl = node = Controller()
    assert ctrl.set_enabled(IGNORE_SELF_MESSAGE, False)
    assert not ctrl.is_enabled(IGNORE_SELF_MESSAGE)

    dev = create_test_device()
    assert (dev)

    assert node.add_object(dev)

    assert ctrl.start()
    time.sleep(1.0)

    found_nodes = ctrl.nodes
    assert 1 < len(found_nodes)

    assert ctrl.stop()
