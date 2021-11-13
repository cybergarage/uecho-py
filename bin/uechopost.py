#!/usr/local/bin/python3
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
from uecho import Controller, Message, Property
from uecho.util import Hex
import uecho.log as log

args = sys.argv


def usage():
    print(
        'Usage : uechopost <address> <obj> <esv> <property (code, data) ...>')


if __name__ == '__main__':
    #log.setLevel(log.DEBUG)

    if len(args) < 5:
        usage()
        exit(1)

    ipaddr = args[1]

    msg = Message()
    msg.DEOJ = Hex.from_string(args[2])
    msg.ESV = Hex.from_string(args[3])
    for n in range(4, len(args)):
        prop_bytes = args[4]
        if len(prop_bytes) < 2:
            continue
        prop = Property()
        prop.code = Hex.from_string(prop_bytes[:2])
        if 2 < len(prop_bytes):
            prop.data = bytes.fromhex(prop_bytes[2:])
        msg.add_property(prop)

    ctrl = Controller()
    ctrl.start()
    time.sleep(1)

    res_msg = ctrl.post_message(msg, ipaddr)
    if not res_msg is None:
        print('Recived: %s' % res_msg.to_string())

    ctrl.stop()