import requests
import pandas as pd

url = "https://cricbuzz-cricket.p.rapidapi.com/stats/v1/rankings/batsmen"

querystring = {"formatType":"odi"}

headers = {
	"X-RapidAPI-Key": "fc69733edbmsh9bdf2f51eb88710p14a0cdjsn7db96e5af297",
	"X-RapidAPI-Host": "cricbuzz-cricket.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

# print(response.json())

# {'rank': [{'id': '8359', 'rank': '1', 'name': 'Babar Azam', 'country': 'Pakistan', 'rating': '824', 'points': '824', 'lastUpdatedOn': '2024-04-16', 'trend': 'Flat', 'faceImageId': '352417', 'countryId': '3', 'avg': '56.72'}
#         , {'id': '11808', 'rank': '2', 'name': 'Shubman Gill', 'country': 'India', 'rating': '801', 'points': '801', 'lastUpdatedOn': '2024-04-16', 'trend': 'Flat', 'faceImageId': '352479', 'countryId': '2', 'avg': '61.38'}
#         , {'id': '1413', 'rank': '3', 'name': 'Virat Kohli', 'country': 'India', 'rating': '768', 'points': '768', 'lastUpdatedOn': '2024-04-16', 'trend': 'Flat', 'faceImageId': '332891', 'countryId': '2', 'avg': '58.68'}
#         , {'id': '576', 'rank': '4', 'name': 'Rohit Sharma', 'country': 'India', 'rating': '746', 'points': '746', 'lastUpdatedOn': '2024-04-16', 'trend': 'Flat', 'faceImageId': '352478', 'countryId': '2', 'avg': '49.12'}
#         , {'id': '11130', 'rank': '4', 'name': 'Harry Tector', 'country': 'Ireland', 'rating': '746', 'points': '746', 'lastUpdatedOn': '2024-04-16', 'trend': 'Flat', 'faceImageId': '244641', 'countryId': '27', 'avg': '49.91'}
#         , {'id': '10713', 'rank': '6', 'name': 'Daryl Mitchell', 'country': 'New Zealand', 'rating': '728', 'points': '728', 'lastUpdatedOn': '2024-04-16', 'trend': 'Flat', 'faceImageId': '351601', 'countryId': '13', 'avg': '52.57'}
#         , {'id': '1739', 'rank': '7', 'name': 'David Warner', 'country': 'Australia', 'rating': '723', 'points': '723', 'lastUpdatedOn': '2024-04-16', 'trend': 'Flat', 'faceImageId': '352449', 'countryId': '4', 'avg': '45.01'}
#         , {'id': '13682', 'rank': '8', 'name': 'Pathum Nissanka', 'country': 'Sri Lanka', 'rating': '711', 'points': '711', 'lastUpdatedOn': '2024-04-16', 'trend': 'Flat', 'faceImageId': '351889', 'countryId': '5', 'avg': '44.50'}
#         , {'id': '6660', 'rank': '9', 'name': 'Dawid Malan', 'country': 'England', 'rating': '707', 'points': '707', 'lastUpdatedOn': '2024-04-16', 'trend': 'Flat', 'faceImageId': '351857', 'countryId': '9', 'avg': '55.77'}
#         , {'id': '9554', 'rank': '10', 'name': 'Rassie van der Dussen', 'country': 'South Africa', 'rating': '701', 'points': '701', 'lastUpdatedOn': '2024-04-16', 'trend': 'Flat', 'faceImageId': '351830', 'countryId': '11', 'avg': '52.44'}
#         , {'id': '10209', 'rank': '11', 'name': 'Heinrich Klaasen', 'country': 'South Africa', 'rating': '697', 'points': '697', 'lastUpdatedOn': '2024-04-16', 'trend': 'Flat', 'faceImageId': '351833', 'countryId': '11', 'avg': '40.07'}
#         , {'id': '9428', 'rank': '12', 'name': 'Shreyas Iyer', 'country': 'India', 'rating': '689', 'points': '689', 'lastUpdatedOn': '2024-04-16', 'trend': 'Flat', 'faceImageId': '352480', 'countryId': '2', 'avg': '49.65'}
#         , {'id': '10863', 'rank': '13', 'name': 'Fakhar Zaman', 'country': 'Pakistan', 'rating': '682', 'points': '682', 'lastUpdatedOn': '2024-04-16', 'trend': 'Flat', 'faceImageId': '352419', 'countryId': '3', 'avg': '46.56'}
#         , {'id': '10934', 'rank': '14', 'name': 'Charith Asalanka', 'country': 'Sri Lanka', 'rating': '681', 'points': '681', 'lastUpdatedOn': '2024-04-16', 'trend': 'Flat', 'faceImageId': '351873', 'countryId': '5', 'avg': '43.59'}
#         , {'id': '10384', 'rank': '15', 'name': 'Shai Hope', 'country': 'West Indies', 'rating': '676', 'points': '676', 'lastUpdatedOn': '2024-04-16', 'trend': 'Flat', 'faceImageId': '170814', 'countryId': '10', 'avg': '49.78'}
#         ]
#         , 'appIndex': {'seoTitle': 'ICC Cricket Rankings - Top 100 Batter | Cricbuzz.com', 'webURL': 'www.cricbuzz.com/cricket-stats/icc-rankings'}
# }

if response.status_code==200:
    response_data = response.json()
    # df = pd.json_normalize(response_data['rank'], max_level=0)
    df = (pd
          .DataFrame
          .from_dict(response_data['rank'])
          .drop(columns=['id','trend','faceImageId'])
          )
    df.to_csv('./data/batsman_ranking.csv', index=False, header=False)

else:
    raise(f'error fetching response:\n{response.status_code}')
