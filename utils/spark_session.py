"""
utils/spark_session.py
──────────────────────
python 3.12~
Dùng chung cho toàn bộ pipeline.
Gọi get_spark() ở đầu mỗi file thay vì tạo SparkSession mới.
"""

import sys
from pyspark.sql import SparkSession


def get_spark(app_name: str = "Rossmann_BigData") -> SparkSession:
    spark = (
        SparkSession.builder
        .appName(app_name)
        .config("spark.sql.shuffle.partitions", "4")
        .config("spark.driver.memory", "4g")
        .config("spark.pyspark.python", sys.executable)
        .config("spark.pyspark.driver.python", sys.executable)
        .config("spark.sql.execution.pyspark.udf.faulthandler.enabled", "true")
        .config("spark.python.worker.faulthandler.enabled", "true")
        .getOrCreate()
    )
    spark.sparkContext.setLogLevel("WARN")
    print(f"[SparkSession] '{app_name}' - Spark {spark.version}")
    return spark