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
#
# To the extent possible under law, Sony Computer Science Laboratories, Inc has waived
# all copyright and related or neighboring rights to ECHONETLite-ObjectDatabase.
# This work is published from: Japan.
#
# GENERATED FROM objects.pl DO NOT EDIT THIS FILE.

from .objects_scsl import get_all_std_scsl_objects
from .objects_mra import get_all_std_mra_objects

__std_objects: dict = {}


def get_all_std_objects() -> dict:
    all_std_objects = {}
    all_std_objects.update(get_all_std_scsl_objects())
    all_std_objects.update(get_all_std_mra_objects())
    return all_std_objects
