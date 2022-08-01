import os


from util import get_spark_session, is_student
from pyspark.sql import functions as F
from pyspark.sql.types import *
import mysql.connector


# Variables for database connection
data_path = "DATA.csv"
user = "admin"
password = "adminpass"
host = "techdb.cmhgbb7baamz.us-east-1.rds.amazonaws.com"
port = 3306


def main():
    print('running')
    # Build spark session
    spark = get_spark_session('SFL_tech')

    # Defining the spark schema for the data import
    schema = StructType([
        StructField("id", IntegerType(), False),
        StructField("first_name", StringType(), False),
        StructField("last_name", StringType(), False),
        StructField("email", StringType(), False),
        StructField("gender", StringType(), False),
        StructField("ip_address", StringType(), False)
    ])

    # Read data from the provided csv
    data = spark.read.csv(data_path, schema=schema, header=True)

    # Splitting the email to create a column of domains
    email = data.withColumn('email_host', F.split(F.col('email'), "@").getItem(1))

    # Defining is_student function (end of code) as a user defined function for use in pyspark
    stu = F.udf(lambda x: is_student(x), StringType())

    # Using the email_host column to find those with 'edu' to mark as students
    edu = email.withColumn('is_student', F.split(F.col('email_host'), "\.")). \
        withColumn('is_student', stu(F.col('is_student')[F.size('is_student') - 1]).cast('boolean'))

    # Checking for duplicate entries within the data
    dupe_check = edu.dropDuplicates().orderBy(F.col('id').asc())
    dupe_check.show()
    # Connection to mysql database; set up for aws mysql database
    conn = mysql.connector.connect(user=user,
                                   password=password,
                                   host=host,
                                   port=port)

    cur = conn.cursor()

    # Creating database and table if not exists
    cur.execute("CREATE DATABASE IF NOT EXISTS SFL_db")
    cur.execute("""
            CREATE TABLE IF NOT EXISTS SFL_db.new_table (
            id int,
            first_name varchar(255),
            last_name varchar(255),
            email varchar(255),
            gender varchar(255),
            email_host varchar(255),
            is_student boolean
            )
        """)

    conn.close()

    # Writing transformed data to mysql table
    # NOTE: overwrite mode is used for ease of loading for this exercise
    dupe_check.select("*").write.format("jdbc"). \
        mode('overwrite'). \
        option("url", f"jdbc:mysql://{host}/SFL_db"). \
        option("driver", "com.mysql.cj.jdbc.Driver"). \
        option("dbtable", "new_table"). \
        option("user", user). \
        option("password", password).save()


if __name__ == '__main__':
    main()