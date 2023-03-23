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

import sys
sys.path.insert(0, '.')
from src.sdk.python.rtdip_sdk.pipelines.destinations.spark.delta import SparkDeltaDestination
from tests.sdk.python.rtdip_sdk.pipelines._pipeline_utils.spark_configuration_constants import spark_session
from pyspark.sql.functions import lit
from pyspark.sql import SparkSession
from pytest_mock import MockerFixture

class TestStreamingQueryClass():
    isActive: bool = False

def test_spark_delta_write_batch(spark_session: SparkSession):
    expected_df = spark_session.createDataFrame([{"id": "1"}])
    delta_destination = SparkDeltaDestination("test_spark_delta_write_batch", {}, "overwrite")
    delta_destination.write_batch(expected_df)
    actual_df = spark_session.table("test_spark_delta_write_batch")
    assert expected_df.schema == actual_df.schema
    assert expected_df.collect() == actual_df.collect()

def test_spark_delta_write_stream(spark_session: SparkSession, mocker: MockerFixture):
    mocker.patch("pyspark.sql.DataFrame.writeStream", new_callable=mocker.Mock(return_value=mocker.Mock(trigger=mocker.Mock(return_value=mocker.Mock(format=mocker.Mock(return_value=mocker.Mock(queryName=mocker.Mock(return_value=mocker.Mock(outputMode=mocker.Mock(return_value=mocker.Mock(options=mocker.Mock(return_value=mocker.Mock(toTable=mocker.Mock(return_value=TestStreamingQueryClass()))))))))))))))
    expected_df = spark_session.createDataFrame([{"id": "1"}])
    eventhub_destination = SparkDeltaDestination("test_spark_delta_write_stream", {}, "overwrite")
    actual = eventhub_destination.write_stream(expected_df)
    assert actual is None