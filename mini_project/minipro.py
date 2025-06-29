import os
from google.cloud import bigquery
import pandas as pd

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:/Users/HP/Downloads/commanding-way-461405-d5-4c041b3d3880.json"

client = bigquery.Client()

query = """
CREATE TABLE IF NOT EXISTS commanding-way-461405-d5.mohiddindataset.movietable
(Title STRING,
Year INT64,
Director STRING,
Duration INT64,
Rating FLOAT64,
Votes INT64,
Description STRING,
Language STRING,
Country STRING,
Budget_USD INT64,
BoxOffice_USD INT64,
Genre STRING,
Production_Company STRING,
Content_Rating STRING,
Lead_Actor STRING,
Num_Awards INT64,
Critic_Reviews INT64
)
"""
job = client.query(query)
job.result()


df = pd.read_csv("C:/Users/HP/Downloads/movie_genre_classification_final.csv")


#transformation
df.drop_duplicates()
table_id = "commanding-way-461405-d5.mohiddindataset.movietable"
job_config = bigquery.LoadJobConfig(write_disposition = "WRITE_TRUNCATE", autodetect = True)
job = client.load_table_from_dataframe(df, table_id, job_config = job_config)
job.result()


query = f"""
CREATE OR REPLACE TABLE commanding-way-461405-d5.mohiddindataset.director_table AS
SELECT
  ROW_NUMBER() OVER (ORDER BY director) AS id,
  director
FROM (
  SELECT DISTINCT director
  FROM commanding-way-461405-d5.mohiddindataset.movietable
)
"""
query_job = client.query(query)
query_job.result()
print("director table done")



query = f"""
CREATE OR REPLACE TABLE commanding-way-461405-d5.mohiddindataset.language_table AS
SELECT
  ROW_NUMBER() OVER (ORDER BY language) AS id,
  Language
FROM (
  SELECT DISTINCT Language
  FROM commanding-way-461405-d5.mohiddindataset.movietable
)
"""
query_job = client.query(query)
query_job.result()
print("language table done")




query = f"""
CREATE OR REPLACE TABLE commanding-way-461405-d5.mohiddindataset.genre_table AS
SELECT
  ROW_NUMBER() OVER (ORDER BY genre) AS id,
  genre
FROM (
  SELECT DISTINCT genre
  FROM commanding-way-461405-d5.mohiddindataset.movietable
)
"""
query_job = client.query(query)
query_job.result()
print("genre table done")




query = f"""
CREATE OR REPLACE TABLE commanding-way-461405-d5.mohiddindataset.country_table AS
SELECT
  ROW_NUMBER() OVER (ORDER BY country) AS id,
  country
FROM (
  SELECT DISTINCT country
  FROM commanding-way-461405-d5.mohiddindataset.movietable
)
"""
query_job = client.query(query)
query_job.result()
print("country table done")




query = f"""
CREATE OR REPLACE TABLE commanding-way-461405-d5.mohiddindataset.production_company_table AS
SELECT
  ROW_NUMBER() OVER (ORDER BY production_company) AS id,
  production_company
FROM (
  SELECT DISTINCT production_company
  FROM commanding-way-461405-d5.mohiddindataset.movietable
)
"""
query_job = client.query(query)
query_job.result()
print("production company table done")




query = f"""
CREATE OR REPLACE TABLE commanding-way-461405-d5.mohiddindataset.leadactor_table AS
SELECT
  ROW_NUMBER() OVER (ORDER BY lead_actor) AS id,
  lead_actor
FROM (
  SELECT DISTINCT lead_actor
  FROM commanding-way-461405-d5.mohiddindataset.movietable
)
"""
query_job = client.query(query)
query_job.result()
print("lead actor table done")
