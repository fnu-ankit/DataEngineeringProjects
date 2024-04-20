import requests
import pandas as pd
from google.cloud import storage


url = "https://cricbuzz-cricket.p.rapidapi.com/stats/v1/rankings/batsmen"

querystring = {"formatType":"odi"}

headers = {
	"X-RapidAPI-Key": "fc69733edbmsh9bdf2f51eb88710p14a0cdjsn7db96e5af297",
	"X-RapidAPI-Host": "cricbuzz-cricket.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)
csv_filename = 'batsman_ranking.csv'

if response.status_code==200:
    response_data = response.json()
    # df = pd.json_normalize(response_data['rank'], max_level=0)
    df = (pd
          .DataFrame
          .from_dict(response_data['rank'])
          .drop(columns=['id','trend','faceImageId'])
          )
    
    df.to_csv(csv_filename, index=False, header=False)

    print(f"Data fetched successfully and written to '{csv_filename}'")

    # Upload the CSV file to GCS
    bucket_name = 'cricbuzz_batsman_ranking_bucket'
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    destination_blob_name = f'{csv_filename}'  # The path to store in GCS

    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(csv_filename)

    print(f"File {csv_filename} uploaded to GCS bucket {bucket_name} as {destination_blob_name}")

else:
    raise(f'error fetching response:\n{response.status_code}')

