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

SHELL := bash

DEVICE_LIST_CSV=DeviceList.csv
DEVICE_LIST_URL=https://raw.githubusercontent.com/SonyCSL/ECHONETLite-ObjectDatabase/master/data/csv/en/${DEVICE_LIST_CSV}

SOURCE_FILE=objects.py

.PHONY: all devicelist clean

all: ${SOURCE_FILE} clean

%.py : %.pl
	@./$< ${DEVICE_LIST_CSV} > $@

devicelist:
	@wget -q -O ${DEVICE_LIST_CSV} ${DEVICE_LIST_URL}

${SOURCE_FILE}: devicelist

clean:
	@rm -f *.csv
