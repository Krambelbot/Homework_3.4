from urllib.parse import urlencode
import requests
import pprint

# Запись констант: ссылка на сервер авторизации, id приложения и версия API.
AUTH_URL = 'https://oauth.vk.com/authorize'
APP_ID = 6214564
API_VER = '5.68'

# Параметры запроса авторизации в виде словаря
# params = {
#     'client_id': APP_ID, # id приложения, которое запросило авторизацию.
#     'display': 'page', # Режим отображения запроса
#     'redirect_uri': 'https://oauth.vk.com/blank.html', # куда будет перенапр. запрос
#     'scope': 'friends, status', # К чему запрошен доступ
#     'response_type': 'token', # Что нам нужно получить в ответ (токен)
#     'v': API_VER # Используемая версия API
# }

# Формирование ссылки на запросс авторизации
# print('?'.join(
#     (AUTH_URL, urlencode(params))
# ))

# Авторизация успешна, получен токен
TOKEN = '734283f5292720f6ca5e0dc031e21ee6456f5c55af503277d04175ef9750ebaba0da44047b31610e15aba'
params = {
    'v': API_VER,
    'access_token': TOKEN,
    # 'fields': 'online'
    # 'text': 'set status from api'
}

# Запрос приложением текущего списка друзей с параметром fields.
response = requests.get('https://api.vk.com/method/friends.get', params)

data = response.json()
print(type(data['response']['items']))
for friend in data['response']['items']:
    response = requests.get('https://api.vk.com/method/friends.search&user_id=friend', params)
    print(response.text)