# aad64_Databricks_Pipeline
Data Pipeline with Databricks

## Summary:
This week's mini project was designed to get a better grasp on using Databricks and creating a data pipeline in it. For the same, we followed a databricks [demo project](https://docs.databricks.com/en/getting-started/data-pipeline-get-started.html). 

## Objectives:
[x] Create a data pipeline using Databricks

[x] Include at least one data source and one data sink

## Ingest Data (Initial):
This was a notbeook created to load and see the data we would be working with in the rest of the project as seen below:

<p align = "center"><img width="1144" alt="image" src="https://github.com/AaryaDesai1/aad64_Databricks_Pipeline/assets/143753050/1ba21a9f-4456-4e5a-ad28-4add4fe3528b"></p>

## Ingest Data:
This notebook was created to actually ingest the data and create a database named `raw_song_data`. The code in this file helped in storing the data in a Databricks File System (DBFS). 
<p align = "center"><img width="1470" alt="image" src="https://github.com/AaryaDesai1/aad64_Databricks_Pipeline/assets/143753050/88f8114c-b57a-4f97-af8c-59db9931c0cd"></p>

## Analyze Data:
This notebook then went on to create a SQL database using the `raw_song_data` table created in the previous notebook, named `prepared_song_data`. This was created so that modifications could be made or other analyses could be done easily using SQL and without impacting the original dataset. 
<p align = "center"><img width="1518" alt="image" src="https://github.com/AaryaDesai1/aad64_Databricks_Pipeline/assets/143753050/5fa5202a-befa-40ef-882a-36d0baf8f2bc"></p>

## Query Data:
Finally, this notebook was created to run a simple query on the new table we created as seen below. 
<p align = "center"><img width="1475" alt="image" src="https://github.com/AaryaDesai1/aad64_Databricks_Pipeline/assets/143753050/74891e0d-0473-4be2-bb6e-cd5d16f3804e"></p>

# Workflow:
As seen below, a workflow was created to ensure that these notebook run in succession on a trigger. Here, I specified this workflow to run everyday at 🕞 (3:30 PM, UTC). 
<p align = "center"><img width="844" alt="image" src="https://github.com/AaryaDesai1/aad64_Databricks_Pipeline/assets/143753050/4367c33c-be0c-464e-bd63-1fba9f4981da"></p>

<p align = "center"><img width="1361" alt="image" src="https://github.com/AaryaDesai1/aad64_Databricks_Pipeline/assets/143753050/9371f63c-0f61-4df5-a636-a352aa785498"></p>
