from pyspark.sql import SparkSession

# Initialize a Spark session
spark = SparkSession.builder.appName("SongDataIngest").getOrCreate()

df = (spark.read.format('csv')
      .option("sep", "\t")
      .load('dbfs:/databricks-datasets/songs/data-001/part-00000'))

# Display the DataFrame
df.show()

# Stop the Spark session
spark.stop()
