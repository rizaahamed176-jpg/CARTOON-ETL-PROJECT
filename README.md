# CARTOON-ETL-PROJECT
ETL pipeline that cleans, transforms, and analyzes a cartoon shows dataset using Python and SQL Server, with SQL queries including aggregations and window functions.
# Cartoon Shows ETL & SQL Analysis

## Overview
Built an ETL pipeline to clean, transform, and analyze a dataset of 100 classic 
cartoon shows, then loaded it into SQL Server Express for querying and analysis.

## What I Did
- Extracted raw CSV data containing show name, span, description, and rating
- Cleaned data using Python (pandas): removed duplicates, checked for missing values
- Created a new feature: rating_category (High if rating > 8, else Average) using a 
  custom function applied across the dataset
- Loaded cleaned data into SQL Server using Python (SQLAlchemy + pyodbc)
- Wrote SQL queries including filtering, aggregation, subqueries, and a 
  DENSE_RANK() window function to rank shows within categories

## Key Insights
- 41 shows rated "High" (rating > 8), 59 rated "Average"
- Highest rated show: Avatar: The Last Airbender (9.3)
- Lowest rated show: Viking Skool (6.4)

## Tools Used
Python (pandas, sqlalchemy, pyodbc), SQL Server Express, SSMS, VS Code

## Files
- cartoon_dataset.py — ETL script (clean, transform, load)
- cartoon.sql — SQL analysis queries
- cleaned_cartoon.csv — cleaned dataset
