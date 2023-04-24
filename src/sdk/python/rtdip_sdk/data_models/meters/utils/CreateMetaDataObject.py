# Copyright 2022 RTDIP
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from ..ami_meters import SeriesType
from ..ami_meters import MetaData
from ..ami_meters import ValueType
from ..ami_meters import ModelType
from ..ami_meters import UomUsage


def create_metadata_VO(uid: str,
                       series_id: str,
                       series_parent_id: str,
                       name: str,
                       uom: UomUsage,
                       description: str,
                       timestamp_start: int,
                       timestamp_end: int,
                       time_zone: str,
                       version: str,
                       series_type: SeriesType,
                       model_type: ModelType,
                       value_type: ValueType,
                       properties: dict):
    
    try:
        return MetaData(uid = uid,
                        series_id = series_id,
                        series_parent_id = series_parent_id,
                        name = name,
                        uom = uom,
                        description = description,
                        timestamp_start = timestamp_start,
                        timestamp_end = timestamp_end,
                        time_zone = time_zone,
                        version = version,
                        series_type = series_type,
                        model_type = model_type,
                        value_type = value_type,
                        properties = properties)
    except Exception as ex:
        error_msg_str: str = 'Could not create Metadata Value Object: {}'.format(ex)
        raise SystemError(error_msg_str)