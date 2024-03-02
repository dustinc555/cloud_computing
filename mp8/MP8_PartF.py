from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType
from pyspark.sql import functions as F
from pyspark.sql.window import Window


sc = SparkContext()
spark = SparkSession.builder.getOrCreate()

# 1. Setup: Write a function to load it into an RDD and DataFrame

def load_gbooks_data(file_path):
    # Read the data into an RDD
    rdd = sc.textFile(file_path).map(lambda line: line.split())
    rdd = rdd.map(lambda elements: elements[:-3] + [int(x) for x in elements[-3:]])

    # Define the schema for the DataFrame
    schema = StructType([
        StructField("word", StringType(), True),
        StructField("year", IntegerType(), True),
        StructField("frequency", IntegerType(), True),
        StructField("books", IntegerType(), True)
    ])

    # Convert RDD to DataFrame with proper data type conversion
    df = spark.createDataFrame(rdd, schema=schema)

    return rdd, df

file_path = "gbooks"
rdd_data, dataframe_data = load_gbooks_data(file_path)

###
# 2. Frequency Increase: analyze the frequency increase of words starting from the year 1500 to the year 2000
###
# Spark SQL - DataFrame API

# Create a temporary view for DataFrame
dataframe_data.createOrReplaceTempView("gbooks_data")

# Filter for only 1500-2000
filtered_data = spark.sql("""
    SELECT *
    FROM gbooks_data
    WHERE year >= 1500 AND year <= 2000
""")

# Create a window for book and year, ordering by year
window_spec = Window.partitionBy("word").orderBy("year")

# Create a new frequency_increase column with lag, adjusting the offset to 1
filtered_data = filtered_data.withColumn("frequency_increase", F.lag("frequency", -1, 0).over(window_spec))

# Sort on total_increase
filtered_data = filtered_data.orderBy("word", "year")

# Sum up the frequency_increases for each word
result_df = filtered_data.groupBy("word").agg(F.sum("frequency_increase").alias("total_increase"))

# Sort the result DataFrame by total_frequency_increase in descending order
result_df = result_df.orderBy(F.desc("total_increase"))

# Show the result
result_df.show(20)