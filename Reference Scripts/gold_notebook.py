# Databricks notebook source
# MAGIC %md
# MAGIC ##Data Access

# COMMAND ----------


spark.conf.set("fs.azure.account.auth.type.nyctaxistoragebag.dfs.core.windows.net", "OAuth")
spark.conf.set("fs.azure.account.oauth.provider.type.nyctaxistoragebag.dfs.core.windows.net", "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider")
spark.conf.set("fs.azure.account.oauth2.client.id.nyctaxistoragebag.dfs.core.windows.net", "9b266e23-d744-4152-ba80-7c9be840e97e")
spark.conf.set("fs.azure.account.oauth2.client.secret.nyctaxistoragebag.dfs.core.windows.net", "Jh78Q~w1jgaXTZ7Q6nCPGicVntKZGNtoUhRFLaZR")
spark.conf.set("fs.azure.account.oauth2.client.endpoint.nyctaxistoragebag.dfs.core.windows.net", "https://login.microsoftonline.com/7f043f5f-692f-49eb-b043-e082087e8641/oauth2/token")

# COMMAND ----------

# MAGIC %md
# MAGIC ##Database Creation

# COMMAND ----------

# MAGIC %sql
# MAGIC create database gold

# COMMAND ----------

# MAGIC %md
# MAGIC ## Data Reading/ Writing/ Creating Delta Tables

# COMMAND ----------

# MAGIC %md
# MAGIC ###Importing Libraries

# COMMAND ----------

from pyspark.sql.functions import *
from pyspark.sql.types import *

# COMMAND ----------

# MAGIC %md
# MAGIC ###Reading data

# COMMAND ----------

# MAGIC %md
# MAGIC ####Variables

# COMMAND ----------

silver =  "abfss://silver@nyctaxistoragebag.dfs.core.windows.net"
gold = "abfss://gold@nyctaxistoragebag.dfs.core.windows.net"

# COMMAND ----------

# MAGIC %md
# MAGIC ####data_ype 

# COMMAND ----------

df_type = spark.read.format("parquet")\
               .option("header", "true")\
               .option("inferSchema", "true")\
               .load(f"{silver}/trip_type")

# COMMAND ----------

df_type.write.format('delta')\
             .mode("append")\
             .option("path", f"{gold}/trip_type")\
             .saveAsTable("gold.trip_type")

# COMMAND ----------

df_trip = spark.read.format("parquet")\
               .option("header", "true")\
               .option("inferSchema", "true")\
               .load(f"{silver}/trips2023data")

# COMMAND ----------

df_trip.display()

# COMMAND ----------

df_trip.write.format('delta')\
             .mode("append")\
             .option("path", f"{gold}/trips2023data")\
             .saveAsTable("gold.trips2023data")