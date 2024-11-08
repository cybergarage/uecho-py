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

import logging
from .constants import LOGGER_NAME


def setLevel(level):
    logging.getLogger(LOGGER_NAME).setLevel(level)


def debug(msg):
    logging.getLogger(LOGGER_NAME).debug(msg)


def info(msg):
    logging.getLogger(LOGGER_NAME).info(msg)


def warning(msg):
    logging.getLogger(LOGGER_NAME).warning(msg)


def error(msg):
    logging.getLogger(LOGGER_NAME).error(msg)
