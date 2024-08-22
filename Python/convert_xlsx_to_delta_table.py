from pyspark.sql import SparkSession
from pyspark.sql.functions import col
import pandas as pd

spark = SparkSession.builder.appName("Session1").getOrCreate() #names my session

excel = "abfs path from the data lake xlsx file"
pdf = pd.read_excel(excel, sheet_name='Sheet1')

df = spark.createDataFrame(pdf) #need to convert the df to a spark df

df2 = df.select(
    col("My Company").alias("my_company"),
    col("Personal Number").alias("personal_number"),
    col("ID Code").alias("id_code")) #need to rename column headers as you are not allowed ot have spaces when writing to a delta table

df2.write.format("delta").mode("overwrite").option("overwriteSchema", "true").saveAsTable("xlsx_file_to_delta_table")

spark.stop()