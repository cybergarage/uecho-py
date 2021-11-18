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
DEVICE_LIST_SOURCE_FILE=objects.py

MANUFACTURE_XLSX=list_code_e.xlsx
MANUFACTURE_CSV=list_code_e.csv
MANUFACTURE_LIST_URL=https://echonet.jp/wp/wp-content/uploads/pdf/General/Echonet/ManufacturerCode_en/${MANUFACTURE_XLSX}
MANUFACTURE_LIST_SOURCE_FILE=manufacturers.py

SOURCE_FILE=${MANUFACTURE_LIST_SOURCE_FILE} ${DEVICE_LIST_SOURCE_FILE}

.PHONY: all ${DEVICE_LIST_CSV} ${MANUFACTURE_CSV} clean

all: ${SOURCE_FILE} clean

${DEVICE_LIST_SOURCE_FILE} : ${DEVICE_LIST_CSV}
	@./objects.pl ${DEVICE_LIST_CSV} > $@

${MANUFACTURE_LIST_SOURCE_FILE} : ${MANUFACTURE_CSV}
	@./manufacturers.pl ${MANUFACTURE_CSV} > $@

${DEVICE_LIST_CSV}:
	@wget -q -O ${DEVICE_LIST_CSV} ${DEVICE_LIST_URL}

${MANUFACTURE_XLSX}:
	@wget -q -O ${MANUFACTURE_XLSX} ${MANUFACTURE_LIST_URL}

${MANUFACTURE_CSV}: ${MANUFACTURE_XLSX}
	@-ssconvert $< $@

${DEVICE_LIST_SOURCE_FILE}: ${DEVICE_LIST_CSV}
${MANUFACTURE_LIST_SOURCE_FILE}: ${MANUFACTURE_CSV} 

clean:
	@rm -f *.csv *.xlsx
