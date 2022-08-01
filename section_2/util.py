from pyspark.sql import SparkSession


# Function to create spark session
def get_spark_session(app_name):
    spark = SparkSession. \
        builder. \
        master('local'). \
        appName('app_name'). \
        config("spark.driver.extraClassPath", "mysql-connector-java-8.0.11.jar"). \
        getOrCreate()

    return spark


# Function to determine if email belongs to a student
def is_student(c):
    if c == 'edu':
        return True
    else:
        return False
