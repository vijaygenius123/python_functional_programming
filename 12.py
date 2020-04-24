import requests
from functools import reduce
URL = "https://randomuser.me/api?results=10"

resp = requests.get(URL)
if(resp.status_code == 200):
    results = resp.json()['results']
    all_female = list(filter(lambda x : x['gender'] == "female", results))
    all_female_age = list(map(lambda x :x['dob']['age'], all_female))
    sum_all_female_age =  reduce(lambda a,c: a + c, all_female_age)
    print(all_female_age)
    print(sum_all_female_age)
else:
    print("Error")