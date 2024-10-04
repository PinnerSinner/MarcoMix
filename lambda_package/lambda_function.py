import json
import pymysql
import requests

def lambda_handler(event, context):
    # Database connection settings
    rds_host = "YOUR_RDS_ENDPOINT"
    db_username = "YOUR_DB_USERNAME"
    db_password = "YOUR_DB_PASSWORD"
    db_name = "YOUR_DB_NAME"

    # Connect to the database
    connection = pymysql.connect(host=rds_host, user=db_username, passwd=db_password, db=db_name)
    cursor = connection.cursor()

    # Fetch data from the API
    response = requests.get("https://api.nationalgrideso.com/dataset/88313ae5-94e4-4ddc-a790-593554d8c6b9/resource/f93d1835-75bc-43e5-84ad-12472b180a98/download/df_fuel_ckan.csv")
    data = response.text

    # Process the CSV data
    lines = data.split("\n")
    for line in lines[1:]:
        if line:
            fields = line.split(",")
            if len(fields) < 4:  # ensure there are enough fields
                continue
            timestamp, demand_forecast, generation_mix, carbon_intensity = fields
            # Insert data into the database
            cursor.execute(f"INSERT INTO EnergyData (timestamp, demand_forecast, generation_mix, carbon_intensity) VALUES ('{timestamp}', {demand_forecast}, '{generation_mix}', {carbon_intensity})")
    
    connection.commit()
    cursor.close()
    connection.close()

    return {
        'statusCode': 200,
        'body': json.dumps('Data fetched and uploaded successfully')
    }
