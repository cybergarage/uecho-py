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
from uecho import Controller, Message, Property, Object, NodeProfile, ESV
import uecho.log as log


def create_read_manufacture_code_message() -> Message:
    msg = Message()
    msg.DEOJ = NodeProfile.CODE
    msg.ESV = ESV.READ_REQUEST
    msg.add_property(Object.MANUFACTURER_CODE)
    return msg


def create_read_property_message(obj: Object, prop: Property) -> Message:
    msg = Message()
    msg.DEOJ = obj.code
    msg.ESV = ESV.READ_REQUEST
    msg.add_property(prop.code)
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
    time.sleep(1)

    if not args.verbose:
        for i, node in enumerate(ctrl.nodes):
            msg = ('%s ' % node.ip.ljust(15))
            for j, obj in enumerate(node.objects):
                msg += '[%d] %06X ' % (j, obj.code)
            print(msg)
    else:
        for i, node in enumerate(ctrl.nodes):
            node_msg = ('%s ' % node.ip.ljust(15))
            req_msg = create_read_manufacture_code_message()
            res_msg = ctrl.post_message(req_msg, node)
            if res_msg is not None:
                if 0 < len(res_msg.properties):
                    res_prop = res_msg.properties[0]
                    node_msg += '(%s)' % ctrl.get_standard_manufacturer_name(res_prop.data)
            print(node_msg)
            for j, obj in enumerate(node.objects):
                obj_msg = '[%d] %06X ' % (j, obj.code)
                if 0 < len(obj.name):
                    obj_msg += '(%s) ' % obj.name
                print(obj_msg)
                for k, prop in enumerate(obj.properties):
                    if not prop.is_read_required():
                        continue
                    prop_msg = '[%d] [%d] %02X ' % (j, k, prop.code)
                    if 0 < len(prop.name):
                        prop_msg += '(%s) ' % prop.name
                    req_msg = create_read_property_message(obj, prop)
                    res_msg = ctrl.post_message(req_msg, node)
                    if res_msg is not None:
                        for res_prop in res_msg.properties:
                            prop_msg += '%s ' % res_prop.data.hex()
                    print(prop_msg)

    ctrl.stop()
