# Copyright 2020 The StackStorm Authors.
# Copyright 2019 Extreme Networks, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import absolute_import
from st2common import transport
from st2common.persistence import base
from st2common.models.db.pack import pack_access
from st2common.models.db.pack import config_schema_access
from st2common.models.db.pack import config_access

__all__ = ["Pack", "ConfigSchema", "Config"]


class Pack(base.Access):
    impl = pack_access

    @classmethod
    def _get_impl(cls):
        return cls.impl

    @classmethod
    def _get_publisher(cls):
        if not cls.publisher:
            cls.publisher = transport.pack.PackPublisher()
        return cls.publisher


class ConfigSchema(base.Access):
    impl = config_schema_access

    @classmethod
    def _get_impl(cls):
        return cls.impl


class Config(base.Access):
    impl = config_access

    @classmethod
    def _get_impl(cls):
        return cls.impl
