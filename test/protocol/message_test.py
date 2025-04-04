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


def test_message_equals():
    msg = Message()
    msg.ESV == ESV.UNKNOWN
    assert msg == msg


def test_parse_message():

    tid = 100
    seoj = 0x0A0B0C
    deoj = 0x0D0E0F
    opc = 3

    def generate_test_msg_bytes():
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
            0x41,    # a
            2,
            2,
            0x41,    # a
            0x42,    # b
            3,
            3,
            0x41,    # a
            0x42,    # b
            0x43,    # c
        ])

        return msg_bytes

    def assert_test_msg(msg):
        assert msg.TID == tid
        assert msg.SEOJ == seoj
        assert msg.DEOJ == deoj
        assert msg.ESV == ESV.NOTIFICATION
        assert msg.OPC == opc
        for n in range(opc):
            prop = msg.properties[n]
            assert prop.code == (n + 1)
            assert len(prop.data) == (n + 1)
            for i in range(len(prop.data)):
                assert prop.data[i] == (0x41 + i)

    msg = Message()
    assert msg.parse_bytes(generate_test_msg_bytes())
    assert_test_msg(msg)

    msg_bytes = msg.to_bytes()
    msg = Message()
    assert msg.parse_bytes(msg_bytes)
    assert_test_msg(msg)


def test_parse_read_write_message():

    tid = 100
    seoj = 0x0A0B0C
    deoj = 0x0D0E0F
    opc = 3

    def generate_test_msg_bytes():
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
            ESV.WRITE_READ_REQUEST,
            opc,
            1,
            1,
            0x41,    # a
            2,
            2,
            0x41,    # a
            0x42,    # b
            3,
            3,
            0x41,    # a
            0x42,    # b
            0x43,    # c
            opc,
            1,
            1,
            0x78,    # x
            2,
            2,
            0x78,    # x
            0x79,    # y
            3,
            3,
            0x78,    # x
            0x79,    # y
            0x7A,    # z
        ])

        return msg_bytes

    def assert_test_msg(msg):
        assert msg.TID == tid
        assert msg.SEOJ == seoj
        assert msg.DEOJ == deoj
        assert msg.ESV == ESV.WRITE_READ_REQUEST

        assert msg.OPCSet == opc
        for n in range(opc):
            prop = msg.set_properties[n]
            assert prop.code == (n + 1)
            assert len(prop.data) == (n + 1)
            for i in range(len(prop.data)):
                assert prop.data[i] == (0x41 + i)

        assert msg.OPCGet == opc
        for n in range(opc):
            prop = msg.get_properties[n]
            assert prop.code == (n + 1)
            assert len(prop.data) == (n + 1)
            for i in range(len(prop.data)):
                assert prop.data[i] == (0x78 + i)

    msg = Message()
    assert msg.parse_bytes(generate_test_msg_bytes())
    assert_test_msg(msg)

    msg_bytes = msg.to_bytes()
    msg = Message()
    assert msg.parse_bytes(msg_bytes)
    assert_test_msg(msg)
