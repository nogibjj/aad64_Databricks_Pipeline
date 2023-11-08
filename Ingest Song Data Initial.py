# Databricks notebook source
# MAGIC %fs ls "/databricks-datasets/songs/data-001"

# COMMAND ----------

df = spark.read.format('csv').option("sep", "\t").load('dbfs:/databricks-datasets/songs/data-001/part-00000')
df.display()
