from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

sc = SparkContext()
spark = SparkSession.builder.getOrCreate()

# 1. Setup: Write a function to load it into an RDD and DataFrame

def load_gbooks_data(file_path):
    # Read the data into an RDD
    rdd = sc.textFile(file_path).map(lambda line: line.split())

    # Define the schema for the DataFrame
    schema = StructType([
        StructField("word", StringType(), True),
        StructField("year", StringType(), True),
        StructField("frequency", StringType(), True),
        StructField("books", StringType(), True)
    ])

    # Convert RDD to DataFrame with proper data type conversion
    df = spark.createDataFrame(rdd, schema=schema)

    return rdd, df

# Example usage
file_path = "gbooks"
rdd_data, dataframe_data = load_gbooks_data(file_path)

# Spark SQL
dataframe_data.createOrReplaceTempView("gbooks_table")
sql_query = """
    SELECT word, COUNT(*)
    FROM gbooks_table
    GROUP BY word
    ORDER BY COUNT(*) DESC
"""
top_words_result = spark.sql(sql_query)
top_words_result.show(3)
