from dbt.adapters.sparkconnect.connections import SparkConnectConnectionManager # noqa
from dbt.adapters.sparkconnect.connections import SparkConnectCredentials
from dbt.adapters.sparkconnect.impl import SparkConnectAdapter

from dbt.adapters.base import AdapterPlugin
from dbt.include import sparkconnect


Plugin = AdapterPlugin(
    adapter=SparkConnectAdapter,
    credentials=SparkConnectCredentials,
    include_path=sparkconnect.PACKAGE_PATH
    )
