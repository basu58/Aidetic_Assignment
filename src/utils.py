from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_timestamp, udf, concat_ws
from pyspark.sql.types import StringType

def create_spark_session():
    return SparkSession.builder.appName("EarthquakeAnalysis").getOrCreate()

def load_dataset(spark, file_path):
    return spark.read.option("header", "true").csv(file_path)

def convert_to_timestamp(df):
    return df.withColumn("Timestamp", concat_ws(" ", col("Date"), col("Time")))

def filter_magnitude(df, threshold=5.0):
    return df.filter(col("Magnitude") > threshold)

def calculate_avg_depth_magnitude(df):
    return df.groupBy("Type").agg({"Depth": "avg", "Magnitude": "avg"})

def categorize_earthquake(magnitude):
    if magnitude < 5.0:
        return "Low"
    elif 5.0 <= magnitude < 7.0:
        return "Moderate"
    else:
        return "High"

categorize_udf = udf(categorize_earthquake, StringType())

def add_magnitude_category(df):
    df = df.withColumn("Magnitude", col("Magnitude").cast("float"))
    return df.withColumn("Magnitude_Category", categorize_udf(col("Magnitude")))

def calculate_distance_from_reference(df, reference_location=(0, 0)):
    return df.withColumn("Distance", ((col("Latitude") - reference_location[0])**2 + (col("Longitude") - reference_location[1])**2)**0.5)
