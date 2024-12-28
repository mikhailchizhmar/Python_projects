import requests

i = 990
api_url = f'http://numbersapi.com/{i}/math?json=true'

res = requests.get(api_url)

print(res.status_code)
print(res.json())
res_dict = res.json()
if res_dict['found']:
    print("Interesting")
else:
    print("Boring")