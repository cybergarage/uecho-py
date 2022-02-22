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
from uecho import Device, ObjectRequestHandler, Property, Controller, IGNORE_SELF_MESSAGE, ReadMessage
from uecho.node_profile import NodeProfile
from uecho.util import Bytes


class MonoLight(Device, ObjectRequestHandler):

    CODE = 0x029101
    OPERATION_STATUS = 0x80
    OPERATING_STATUS_ON = 0x30
    OPERATING_STATUS_OFF = 0x31

    def __init__(self):
        super().__init__(MonoLight.CODE)

    def property_read_requested(self, prop: Property) -> bool:
        return True

    def property_write_requested(self, prop: Property, data: bytes) -> bool:
        return True


def create_test_device():
    dev = MonoLight()

    # Mandatory properties of device super class
    assert dev.has_property(0x80)    # Operation status
    assert dev.has_property(0x8A)    # Manufacturer code
    # Mandatory properties of mono functional lighting
    assert dev.has_property(0x80)    # Operation status
    assert dev.has_property(0xB0)    # Illuminance Level Setting

    assert dev.set_request_handler(dev)

    # status_off = bytearray([MonoLight.OPERATING_STATUS_OFF])
    status_off = Bytes.from_int(MonoLight.OPERATING_STATUS_OFF, 1)

    assert dev.set_property_data(MonoLight.OPERATING_STATUS, status_off)
    assert dev.get_property_data(MonoLight.OPERATING_STATUS) == status_off

    return dev


def test_device():
    ctrl = node = Controller()
    assert ctrl.set_enabled(IGNORE_SELF_MESSAGE, False)
    assert not ctrl.is_enabled(IGNORE_SELF_MESSAGE)

    dev = create_test_device()
    assert (dev)

    assert node.add_object(dev)

    node_id = node.get_object(NodeProfile.CODE).get_property(NodeProfile.IDENTIFICATION_NUMBER).data

    assert ctrl.start()
    time.sleep(1.0)

    found_nodes = ctrl.nodes
    assert 1 <= len(found_nodes)

    remote_dev_node = None
    for remote_node in found_nodes:
        if remote_node.address != node.address:
            continue
        req_msg = ReadMessage(NodeProfile.CODE)
        req_msg.add_property(NodeProfile.IDENTIFICATION_NUMBER)
        res_msg = ctrl.post_message(req_msg, remote_node)
        if res_msg is None:
            continue
        prop = res_msg.properties[0]
        assert prop
        prop_id = prop.data
        if prop_id != node_id:
            continue
        remote_dev_node = remote_node
        break

    assert remote_dev_node

    # Read message
    req_msg = ReadMessage(NodeProfile.CODE)
    req_msg.add_property(MonoLight.OPERATION_STATUS)
    res_msg = ctrl.post_message(req_msg, remote_dev_node)
    assert res_msg
    assert res_msg.OPC == 1
    assert res_msg.properties[0].data == bytes([MonoLight.OPERATING_STATUS_OFF])

    assert ctrl.stop()
