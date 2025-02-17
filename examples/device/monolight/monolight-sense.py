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

import sys
import time
import argparse
from uecho import LocalNode, Device, Property, ObjectRequestHandler
import uecho.log as log
from sense_hat import SenseHat


class MonoLight(Device, ObjectRequestHandler):

    CODE = 0x029101
    OPERATION_STATUS = 0x80
    OPERATING_STATUS_ON = 0x30
    OPERATING_STATUS_OFF = 0x31

    def __init__(self):
        super().__init__(MonoLight.CODE)
        self.set_request_handler(self)
        self.sense = SenseHat()

    def __del__(self):
        super().__del__()

    def on(self):
        self.set_property_integer(MonoLight.OPERATION_STATUS, MonoLight.OPERATING_STATUS_ON, 1)
        self.led_on()
        print("ON")

    def off(self):
        self.set_property_integer(MonoLight.OPERATION_STATUS, MonoLight.OPERATING_STATUS_OFF, 1)
        self.led_off()
        print("OFF")

    def led_on(self):
        self.sense.clear([0xFF, 0xFF, 0xFF])

    def led_off(self):
        self.sense.clear([0x00, 0x00, 0x00])

    def property_read_requested(self, prop: Property) -> bool:
        return super().property_read_requested(prop)

    def property_write_requested(self, prop: Property, data: bytes) -> bool:
        if prop.code == MonoLight.OPERATION_STATUS:
            if len(prop.data) != 1:
                return False
            if (data[0] != MonoLight.OPERATING_STATUS_ON) and (data[0] != MonoLight.OPERATING_STATUS_OFF):
                return False
            if data[0] == MonoLight.OPERATING_STATUS_ON:
                self.on()
            else:
                self.off()
            return True
        return super().property_write_requested(prop, data)


class MonoLightNode(LocalNode):

    dev: MonoLight

    def __init__(self):
        super().__init__()
        self.dev = MonoLight()
        self.add_object(self.dev)

    def start(self) -> bool:
        self.dev.on()
        return super().start()

    def stop(self) -> bool:
        self.dev.off()
        return super().stop()


args = sys.argv

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Mono functional lighting device')
    parser.add_argument("-v", "--verbose", help="output all mandatory read properties of found nodes", action="store_true")
    parser.add_argument("-d", "--debug", help="output raw debug messages", action="store_true")

    log.setLevel(log.ERROR)
    args = parser.parse_args()
    if args.debug:
        log.setLevel(log.DEBUG)

    node = MonoLightNode()
    node.start()

    try:
        while True:
            time.sleep(1.0)
    except KeyboardInterrupt:
        node.stop()
