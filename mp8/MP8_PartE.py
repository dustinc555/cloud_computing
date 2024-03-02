from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

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

# Example usage
file_path = "gbooks"
rdd_data, dataframe_data = load_gbooks_data(file_path)


df2 = dataframe_data.select("word", "year").distinct().limit(100)
df2.createOrReplaceTempView('gbooks2')


# 3. Perform JOIN operation on 'df2' and find the number of pairs of words in the same year
result = spark.sql("""
    SELECT COUNT(*) as pairs_count
    FROM gbooks2 g1 JOIN gbooks2 g2 
    ON g1.year = g2.year
""")

# Show the result
count_value = result.first()["pairs_count"]
print(count_value)