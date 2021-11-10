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

from .esv import ESV


class Message(ESV):
    """
    Message represents a protocol message of Echonet Lite.
    """
    FRAME_HEADER_SIZE = (1 + 1 + 2)
    FORMAT1_HEADER_SIZE = (3 + 3 + 1 + 1)
    FORMAT1_MIN_SIZE = (FRAME_HEADER_SIZE + FORMAT1_HEADER_SIZE)
    FORMAT1_PROPERTY_HEADER_SIZE = 2
    EHD1_ECHONET = 0x10
    EHD2_FORMAT1 = 0x81
    TID_SIZE = 2
    TID_MAX = 65535
    EOJ_SIZE = 3

    def __init__(self):
        #super(ESV, self).__init__()
        super().__init__()
        self.TID = 0
        self.SEOJ = 0
        self.DEOJ = 0

    def parse_bytes(self, msg_bytes):
        pass
