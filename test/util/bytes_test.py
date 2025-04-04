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

from uecho.util import Bytes


def test_convert_bytes():
    for n in range(0xFF + 1):
        ibytes = Bytes.from_int(n, 1)
        assert n == Bytes.to_int(ibytes)
        assert n == Bytes.to_int(bytearray(ibytes))

    for n in range(0, (0xFFFF + 1), int(0xFFFF / 0xFF)):
        ibytes = Bytes.from_int(n, 2)
        assert n == Bytes.to_int(ibytes)
        assert n == Bytes.to_int(bytearray(ibytes))

    for n in range(0, (0xFFFFFF + 1), int(0xFFFFFF / 0xFF)):
        ibytes = Bytes.from_int(n, 3)
        assert n == Bytes.to_int(ibytes)
        assert n == Bytes.to_int(bytearray(ibytes))

    for n in range(0, (0xFFFFFFFF + 1), int(0xFFFFFFFF / 0xFF)):
        ibytes = Bytes.from_int(n, 4)
        assert n == Bytes.to_int(ibytes)
        assert n == Bytes.to_int(bytearray(ibytes))
