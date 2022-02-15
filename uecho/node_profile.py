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

from typing import List
from .profile import Profile
from .object import Object
from .std import Database
from .util.bytes import Bytes


class NodeProfile(Profile):
    CODE = 0x0EF001
    CLASS_CODE = 0xF0
    INSTANCE_GENERAL_CODE = 0x01
    INSTANCE_TRANSMISSION_ONLY_CODE = 0x02

    CLASS_OPERATING_STATUS = Profile.OPERATING_STATUS
    CLASS_VERSION_INFORMATION = 0x82
    CLASS_IDENTIFICATION_NUMBER = 0x83
    CLASS_FAULT_CONTENT = 0x89
    CLASS_UNIQUE_IDENTIFIER_DATA = 0xBF
    CLASS_NUMBER_OF_SELF_NODE_INSTANCES = 0xD3
    CLASS_NUMBER_OF_SELF_NODE_CLASSES = 0xD4
    CLASS_INSTANCE_LIST_NOTIFICATION = 0xD5
    CLASS_SELF_NODE_INSTANCE_LIST_S = 0xD6
    CLASS_SELF_NODE_CLASS_LIST_S = 0xD7

    CLASS_OPERATING_STATUS_SIZE = 1
    CLASS_VERSION_INFORMATION_SIZE = 4
    CLASS_IDENTIFICATION_MANUFACTURER_CODE_SIZE = 3
    CLASS_IDENTIFICATION_UNIQUE_ID_SIZE = 13
    CLASS_IDENTIFICATION_NUMBER_SIZE = 1 + CLASS_IDENTIFICATION_MANUFACTURER_CODE_SIZE + CLASS_IDENTIFICATION_UNIQUE_ID_SIZE
    CLASS_FAULT_CONTENT_SIZE = 2
    CLASS_UNIQUE_IDENTIFIER_DATA_SIZE = 2
    CLASS_NUMBER_OF_SELF_NODE_INSTANCES_SIZE = 3
    CLASS_NUMBER_OF_SELF_NODE_CLASSES_SIZE = 2
    CLASS_SELF_NODE_INSTANCE_LIST_S_MAX = 0xFF
    CLASS_SELF_NODE_CLASS_LIST_S_MAX = 0xFF
    CLASS_INSTANCE_LIST_NOTIFICATION_MAX = CLASS_SELF_NODE_INSTANCE_LIST_S_MAX

    CLASS_OPERATING_STATUS_ON = Profile.OPERATING_STATUS_ON
    CLASS_OPERATING_STATUS_OFF = Profile.OPERATING_STATUS_OFF
    CLASS_BOOTING = 0x30
    CLASS_NOT_BOOTING = 0x31
    LOWER_COMMUNICATION_LAYER_PROTOCOL_TYPE = 0xFE

    def __init__(self):
        super().__init__(NodeProfile.CODE)
        std_obj = Database().get_object(NodeProfile.CODE)
        if isinstance(std_obj, Object):
            self._set_object_properties(std_obj)
        self.update_class_instance_properties([self])

    def __is_node_profile_object(self, obj):
        if obj.code == NodeProfile.CODE:
            return True
        if obj.code == NodeProfileReadOnly.CODE:
            return True
        return False

    def __update_instance_properties(self, objs: List[Object]) -> bool:
        instance_cnt = 0
        instance_list = bytearray()
        for obj in objs:
            if self.__is_node_profile_object(obj):
                continue
            instance_cnt += 1
            instance_list.extend(Bytes.from_int(obj.code, 3))

        if not self.set_property_data(NodeProfile.CLASS_NUMBER_OF_SELF_NODE_INSTANCES, Bytes.from_int(instance_cnt, NodeProfile.CLASS_NUMBER_OF_SELF_NODE_INSTANCES_SIZE)):
            return False

        instance_list_bytes = bytearray(Bytes.from_int(instance_cnt, 1))
        instance_list_bytes.extend(instance_list)
        if not self.set_property_data(NodeProfile.CLASS_INSTANCE_LIST_NOTIFICATION, instance_list_bytes):
            return False
        if not self.set_property_data(NodeProfile.CLASS_SELF_NODE_INSTANCE_LIST_S, instance_list_bytes):
            return False

        return True

    def __update_class_properties(self, objs: List[Object]) -> bool:
        class_cnt = 0
        class_list = bytearray()
        for obj in objs:
            class_cnt += 1
            if self.__is_node_profile_object(obj):
                continue
            class_list.extend(Bytes.from_int(obj.code, 3))

        if not self.set_property_data(NodeProfile.CLASS_NUMBER_OF_SELF_NODE_CLASSES, Bytes.from_int(class_cnt, NodeProfile.CLASS_NUMBER_OF_SELF_NODE_CLASSES_SIZE)):
            return False

        class_list_bytes = bytearray(Bytes.from_int(len(class_list), 1))
        class_list_bytes.extend(class_list)
        if not self.set_property_data(NodeProfile.CLASS_SELF_NODE_CLASS_LIST_S, class_list_bytes):
            return False

        return True

    def update_class_instance_properties(self, objs: List[Object]) -> bool:
        if not self.__update_instance_properties(objs):
            return False
        if not self.__update_class_properties(objs):
            return False
        return True


class NodeProfileReadOnly(NodeProfile):
    CODE = 0x0EF002

    def __init__(self):
        super().__init__()
        self.set_code(NodeProfileReadOnly.CODE)

