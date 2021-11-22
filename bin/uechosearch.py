#!/usr/bin/python3
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
import argparse
from uecho import Controller, Message, Property, Object, NodeProfile
import uecho.log as log


def create_manufacture_request_message() -> Message:
    msg = Message
    msg.DEOJ = NodeProfile.OBJECT
    msg.ESV = Object.MANUFACTURER_CODE
    prop = Property()
    prop.code = Property.GET
    msg.add_property(prop)
    return msg


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Searches ECHONET Lite nodes.')
    parser.add_argument("-v", "--verbose", help="output found nodes in more detail", action="store_true")
    parser.add_argument("-d", "--debug", help="output debug messages", action="store_true")

    log.setLevel(log.ERROR)
    args = parser.parse_args()
    if args.debug:
        log.setLevel(log.DEBUG)

    ctrl = Controller()
    ctrl.start()
    ctrl.search()
    time.sleep(1)
    ctrl.stop()

    if not args.verbose:
        for i, node in enumerate(ctrl.nodes):
            msg = ('%s ' % node.ip.ljust(15))
            for j, obj in enumerate(node.objects):
                msg += '[%d] %06X ' % (j, obj.code)
            print(msg)
        exit(0)

    for i, node in enumerate(ctrl.nodes):
        msg = ('%s ' % node.ip.ljust(15))
        print(msg)
        res_msg = ctrl.post_message(create_manufacture_request_message(), node)
        print(res_msg)
        for j, obj in enumerate(node.objects):
            msg = '[%d] %06X ' % (j, obj.code)
            if 0 < len(obj.name):
                msg += '(%s)' % obj.name
            print(msg)
