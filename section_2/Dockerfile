FROM jupyter/pyspark-notebook

ADD app.py .
ADD util.py .
ADD requirements.txt .
ADD DATA.csv .
ADD /jar/mysql-connector-java-8.0.11.jar .
RUN pip install -r requirements.txt

CMD ["python3", "./app.py"]
RUN python app.py
