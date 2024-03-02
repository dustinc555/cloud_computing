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
        StructField("year", IntegerType(), True),
        StructField("frequency", IntegerType(), True),
        StructField("books", IntegerType(), True)
    ])

    # Convert RDD to DataFrame
    df = spark.createDataFrame(rdd, schema=schema)

    return rdd, df

# Example usage
file_path = "gbooks"
rdd_data, dataframe_data = load_gbooks_data(file_path)

# 2. Print DataFrame schema
dataframe_data.printSchema()
