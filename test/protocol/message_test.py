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

from uecho.protocol import Message, ESV
from uecho.util import Bytes


def test_new_message():
    msg = Message()
    msg.ESV == ESV.UNKNOWN


def test_parse_message():

    tid = 100
    seoj = 0x0A0B0C
    deoj = 0x0D0E0F
    opc = 3

    def test_msg_bytes():
        tid_bytes = Bytes.from_int(tid, 2)
        seoj_bytes = Bytes.from_int(seoj, 3)
        deoj_bytes = Bytes.from_int(deoj, 3)

        msg_bytes = bytearray([
            Message.EHD1_ECHONET,
            Message.EHD2_FORMAT1,
            tid_bytes[0],
            tid_bytes[1],
            seoj_bytes[0],
            seoj_bytes[1],
            seoj_bytes[2],
            deoj_bytes[0],
            deoj_bytes[1],
            deoj_bytes[2],
            ESV.NOTIFICATION,
            opc,
            1,
            1,
            0x41,  # a
            2,
            2,
            0x42,  # b
            0x43,  # c
            3,
            3,
            0x44,  # d
            0x45,  # e
            0x46,  # f
        ])

        return msg_bytes

    msg = Message()
    assert msg.parse_bytes(test_msg_bytes())
    assert msg.TID == tid
    assert msg.SEOJ == seoj
    assert msg.DEOJ == deoj
    assert msg.ESV == ESV.NOTIFICATION
    assert msg.OPC == opc
