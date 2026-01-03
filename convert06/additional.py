# Modification from - https://stackoverflow.com/a
import requests
import json
import urllib3

urllib3.disable_warnings()

url = 'https://reqres.in/api/users?page=2'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

desired_columns = ['first_name', 'last_name', 'email']

r = requests.get(url, headers=headers, verify=False)

if r.status_code == 200:
    users_list = json.loads(r.text)['data']
    with open('response.csv', 'w') as f:
        f.write(','.join(desired_columns) + '\n')

        for user in users_list:
            data_to_write = []
            
            for column in desired_columns:
                data_to_write.append(str(user[column]))

            f.write(','.join(data_to_write) + '\n')
            
    print("Successfully wrote data to response.csv")

else:
    print(f"Failed to retrieve data. Status: {r.status_code}")
