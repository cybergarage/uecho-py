# Copyright (C) 2021 The uecho-py Authors. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License")
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

from typing import Any, Union, Tuple

from .object import Object


class Profile(Object):

    def __init__(self, code: Union[int, Tuple[int, int], Tuple[int, int, int], Any] = None):
        super().__init__(code)

    def message_received(self, msg) -> bool:
        if msg.is_read_request():
            return True
        return False