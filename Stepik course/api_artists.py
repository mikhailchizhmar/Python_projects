import requests
import json

client_id = '6c337864cdaa4ab8ea95'
client_secret = 'ed1ad6f6389d87b3b7986ea277b5d9f3'

# инициируем запрос на получение токена
r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })

# разбираем ответ сервера
j = json.loads(r.text)

# достаем токен
token = j["token"]

# создаем заголовок, содержащий наш токен
headers = {"X-Xapp-Token" : token}
author_id = ''
author_dict = {}
while True:
    author_id = input()
    if author_id == '0':
        break

    # инициируем запрос с заголовком
    r = requests.get(f"https://api.artsy.net/api/artists/{author_id}", headers=headers)

    # разбираем ответ сервера
    j = json.loads(r.text)
    author_dict[j["sortable_name"]] = j["birthday"]
    sorted_author_dict = sorted(author_dict.items(), key=lambda x: (x[1], x[0]))  # list of tuples
print(author_dict)
print(sorted_author_dict)
for elem in sorted_author_dict:
    print(elem[0])
