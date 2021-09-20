Project Description:

Extract, transform and load (ETL) transactional data for a hypothetical café chain. Prior to this, the company was only capable of analysing a single store at a time. This application allows the company to analyse and visualise their data in a comprehensive manner.

The application Lambda triggers when a CSV file containing a single day's transactional data is uploaded to an S3 bucket. It extracts and transforms the data, saves it to another bucket, and sends an SQS message to a second lambda which triggers and loads the data into Redshift.

Technologies Used:

Python 
PostgreSQL
Visual Studio Code
Docker
AWS
S3
Lambda
EC2
Redshift
Cloud Watch
Grafana
Here is a supporting image that illustrates the technical architecture of this project.
