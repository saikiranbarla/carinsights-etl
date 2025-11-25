# carinsights-etl

ETL pipeline project for car sales analytics.

This repository contains:
- SQL DDL for RDS (Postgres) in `sql/create_tables.sql`
- Data generator script to create 3 months of sample CSV files in `data_generator/generate_3months_data.py`
- Folder structure for Glue ETL scripts, Lambda functions, and Infrastructure as Code
- GitHub Actions CI workflow in `.github/workflows/ci.yml`

Next steps:
1. Generate sample CSV data and upload to S3 raw bucket.
2. Build Glue ETL jobs to clean and load data into databases.
3. Add CI/CD workflows to automate deployment.