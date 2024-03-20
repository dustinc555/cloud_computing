import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
import re

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Script generated for node AWS Glue Data Catalog
AWSGlueDataCatalog_node1710557938080 = glueContext.create_dynamic_frame.from_catalog(
    database="mp9-database",
    table_name="flights",
    transformation_ctx="AWSGlueDataCatalog_node1710557938080",
)

# Script generated for node Change Schema
ChangeSchema_node1710566543902 = ApplyMapping.apply(
    frame=AWSGlueDataCatalog_node1710557938080,
    mappings=[
        ("year", "long", "year", "long"),
        ("month", "long", "month", "long"),
        ("day", "long", "day", "long"),
        ("airline", "string", "airline", "string"),
        ("origin_airport", "string", "origin_airport", "string"),
        ("destination_airport", "string", "destination_airport", "string"),
        ("scheduled_departure", "long", "scheduled_departure", "long"),
        ("departure_time", "long", "departure_time", "long"),
        ("departure_delay", "long", "departure_delay", "long"),
        ("scheduled_time", "long", "scheduled_time", "long"),
        ("elapsed_time", "long", "elapsed_time", "long"),
        ("scheduled_arrival", "long", "scheduled_arrival", "long"),
        ("arrival_time", "long", "arrival_time", "long"),
        ("arrival_delay", "long", "arrival_delay", "long"),
        ("diverted", "long", "diverted", "long"),
        ("cancelled", "long", "cancelled", "long"),
    ],
    transformation_ctx="ChangeSchema_node1710566543902",
)

# Script generated for node Filter
Filter_node1710566889317 = Filter.apply(
    frame=ChangeSchema_node1710566543902,
    f=lambda row: (not (row["cancelled"] == 1)),
    transformation_ctx="Filter_node1710566889317",
)

# Script generated for node AWS Glue Data Catalog
AWSGlueDataCatalog_node1710567083596 = glueContext.write_dynamic_frame.from_catalog(
    frame=Filter_node1710566889317,
    database="mp9-database",
    table_name="gluejob1",
    transformation_ctx="AWSGlueDataCatalog_node1710567083596",
)

job.commit()
