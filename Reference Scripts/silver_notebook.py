# Databricks notebook source
# MAGIC %md
# MAGIC ##Data Access

# COMMAND ----------

APP ID: "9b266e23-d744-4152-ba80-7c9be840e97e"
TENANT ID: "7f043f5f-692f-49eb-b043-e082087e8641"
SECRET ID: "Jh78Q~w1jgaXTZ7Q6nCPGicVntKZGNtoUhRFLaZR"


# COMMAND ----------


spark.conf.set("fs.azure.account.auth.type.nyctaxistoragebag.dfs.core.windows.net", "OAuth")
spark.conf.set("fs.azure.account.oauth.provider.type.nyctaxistoragebag.dfs.core.windows.net", "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider")
spark.conf.set("fs.azure.account.oauth2.client.id.nyctaxistoragebag.dfs.core.windows.net", "9b266e23-d744-4152-ba80-7c9be840e97e")
spark.conf.set("fs.azure.account.oauth2.client.secret.nyctaxistoragebag.dfs.core.windows.net", "Jh78Q~w1jgaXTZ7Q6nCPGicVntKZGNtoUhRFLaZR")
spark.conf.set("fs.azure.account.oauth2.client.endpoint.nyctaxistoragebag.dfs.core.windows.net", "https://login.microsoftonline.com/7f043f5f-692f-49eb-b043-e082087e8641/oauth2/token")

# COMMAND ----------

dbutils.fs.ls("abfss://bronze@nyctaxistoragebag.dfs.core.windows.net/")

# COMMAND ----------

# MAGIC %md
# MAGIC ##Data Reading

# COMMAND ----------

# MAGIC %md
# MAGIC ###Importing Libraries

# COMMAND ----------

from pyspark.sql.functions import *
from pyspark.sql.types import *

# COMMAND ----------

# MAGIC %md
# MAGIC ###Reading CSV data ( Just for demonstration)

# COMMAND ----------

df_trip_type = spark.read.format("csv")\
                    .option("header", "true")\
                    .option("inferSchema", "true")\
                    .load("abfss://bronze@nyctaxistoragebag.dfs.core.windows.net/trip_type")

# COMMAND ----------

df_trip_type.display()

# COMMAND ----------

df_trip_zone = spark.read.format("csv")\
                    .option("header", "true")\
                    .option("inferSchema", "true")\
                    .load("abfss://bronze@nyctaxistoragebag.dfs.core.windows.net/trip_zone")

# COMMAND ----------

df_trip_zone.display()

# COMMAND ----------

# MAGIC %md
# MAGIC ###Reading Parquet Files
# MAGIC ####Trip data(Main data for this project)

# COMMAND ----------

# MAGIC %md
# MAGIC ####Creating Custom schema

# COMMAND ----------

myschema = '''
    VendorID BIGINT,
    lpep_pickup_datetime TIMESTAMP,
    lpep_dropoff_datetime TIMESTAMP,
    store_and_fwd_flag STRING,
    RatecodeID BIGINT,
    PULocationID BIGINT,
    DOLocationID BIGINT,
    passenger_count BIGINT,
    trip_distance DOUBLE,
    fare_amount DOUBLE,
    extra DOUBLE,
    mta_tax DOUBLE,
    tip_amount DOUBLE,
    tolls_amount DOUBLE,
    ehail_fee DOUBLE,
    improvement_surcharge DOUBLE,
    total_amount DOUBLE,
    payment_type BIGINT,
    trip_type BIGINT,
    congestion_surcharge DOUBLE
'''


# COMMAND ----------

# MAGIC %md
# MAGIC ####Reading the data

# COMMAND ----------

df_trip = spark.read.format("parquet")\
               .option("header", "true")\
               .schema(myschema)\
               .option("recursiveFileLookup", "true")\
               .load("abfss://bronze@nyctaxistoragebag.dfs.core.windows.net/trips2023data")

# COMMAND ----------

df_trip.display()

# COMMAND ----------

# MAGIC %md
# MAGIC ##Data Transformations 

# COMMAND ----------

# MAGIC %md
# MAGIC ###trip_type

# COMMAND ----------

df_trip_type = df_trip_type.withColumnRenamed("description", "trip_description")


# COMMAND ----------

df_trip_type.display()

# COMMAND ----------

df_trip_type.write.format("parquet")\
                  .mode("append")\
                  .option("path","abfss://silver@nyctaxistoragebag.dfs.core.windows.net/trip_type")\
                  .save()

# COMMAND ----------

# MAGIC %md
# MAGIC ###trip_zone

# COMMAND ----------

df_trip_zone = df_trip_zone.withColumn("Zone1", split(col("Zone"), "/")[0]) \
                           .withColumn("Zone2", split(col("Zone"), "/")[1])

display(df_trip_zone)

# COMMAND ----------

df_trip_zone = df_trip_zone.na.fill({"Zone2": "N/A"})
display(df_trip_zone)

# COMMAND ----------

df_trip_zone.write.format("parquet")\
                  .mode("overwrite")\
                  .option("path","abfss://silver@nyctaxistoragebag.dfs.core.windows.net/trip_zone")\
                  .save()

# COMMAND ----------

# MAGIC %md
# MAGIC ###trip data(Main dataset)

# COMMAND ----------

df_trip.display()

# COMMAND ----------

df_trip = df_trip.withColumn("trip-date", to_date(col("lpep_pickup_datetime")))\
                 .withColumn("trip-year", year(col("lpep_pickup_datetime")))\
                 .withColumn("trip-month", month(col("lpep_pickup_datetime")))

# COMMAND ----------

df_trip.display()

# COMMAND ----------

df_trip = df_trip.select("VendorID","PULocationID", "DOLocationID", "fare_amount", "total_amount")

# COMMAND ----------

df_trip.display()

# COMMAND ----------

df_trip.write.format("parquet")\
             .mode("append")\
             .option("path", "abfss://silver@nyctaxistoragebag.dfs.core.windows.net/trips2023data")\
             .save()

# COMMAND ----------

# MAGIC %md
# MAGIC ##Analysis

# COMMAND ----------

display(df_trip)