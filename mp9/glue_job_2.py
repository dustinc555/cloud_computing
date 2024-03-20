import sys
from pyspark.sql.functions import col, expr, lit
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.dynamicframe import DynamicFrame
from awsglue.job import Job
import re

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Load data from Glue catalog
source_dyf = glueContext.create_dynamic_frame.from_catalog(
    database="mp9-database",
    table_name="gluejob1",
    transformation_ctx="source_dyf",
)

df = source_dyf.toDF()

# time_zone_difference = (f1.scheduled_arrival / 100)*60 + (f1.scheduled_arrival % 100) - ((f1.scheduled_departure / 100)*60 + (f1.scheduled_departure % 100) + f1.scheduled_time)%(24*60)
time_zone_difference_expr = expr('cast((FLOOR(scheduled_arrival / 100))*60 + (scheduled_arrival % 100) - (FLOOR(scheduled_departure / 100)*60 + (scheduled_departure % 100) + scheduled_time)%(1440) as int)')


# Add column "time_zone_difference" to DataFrame
df_with_timezone = df.withColumn("time_zone_difference", time_zone_difference_expr)

# Convert DataFrame back to DynamicFrame if needed
source_dyf_with_timezone = DynamicFrame.fromDF(df_with_timezone, glueContext, "df_with_timezone_dyf")

AWSGlueDataCatalog_node = glueContext.write_dynamic_frame.from_catalog(
    frame=source_dyf_with_timezone,
    database="mp9-database",
    table_name="gluejob2",
    transformation_ctx="AWSGlueDataCatalog_node",
)

job.commit()
