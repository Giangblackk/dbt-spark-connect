#!/usr/bin/env python
from setuptools import find_namespace_packages, setup

package_name = "dbt-spark-connect"
# make sure this always matches dbt/adapters/{adapter}/__version__.py
package_version = "0.0.1"
description = """The SparkConnect adapter plugin for dbt"""

setup(
    name=package_name,
    version=package_version,
    description=description,
    long_description=description,
    author="Giangblackk",
    author_email="giangblackk@gmail.com",
    url="https://github.com/Giangblackk/dbt-spark-connect",
    packages=find_namespace_packages(include=["dbt", "dbt.*"]),
    include_package_data=True,
    install_requires=[
        "dbt-common>=1.10,<2.0",
        "dbt-adapters>=1.7,<2.0",
        # add dbt-core to ensure backwards compatibility of installation, this is not a functional dependency
        "dbt-core>=1.8.0",
    ],
)
