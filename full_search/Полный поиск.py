import requests
import sys
from io import BytesIO
from PIL import Image
from selection_parameters import params_scale

API_KEY = "40d1649f-0493-4b70-98ba-98533de7710b"
geocoder_request = "http://geocode-maps.yandex.ru/1.x/"


def get_geocoder(geocode, kind=None):
    params = {
        "apikey": API_KEY,
        "geocode": geocode,
        "format": "json",
        'kind': kind if kind is not None else None
    }
    response = requests.get(
        geocoder_request,
        params=params,
    )
    if response:
        json_response = response.json()
        toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0][
            "GeoObject"
        ]
        return toponym["Point"]["pos"]
    print("Ошибка выполнения запроса:")
    print(geocoder_request)
    print("Http статус:", response.status_code, "(", response.reason, ")")
    return False


ll = get_geocoder(input('Введите адрес: ')).split()
spn = input('Введите размеры объекта в градусной мере (два числа): ').split()
map_request = "http://static-maps.yandex.ru/1.x/"
params = params_scale(ll, spn=spn, pt=ll)
print(params)
response = requests.get(map_request, params=params)
print(response.url)
Image.open(BytesIO(
    response.content)).show()
# map_request = "http://static-maps.yandex.ru/1.x/"
# response = requests.get(
#     map_request,
#     params={
#         "ll": "29.968351,59.952709",
#         "l": "map",
#         "pl": "30.313731,59.942322,30.304370,59.946309,30.282774,59.950197,30.215951,59.965202,30.130391,59.962367,29.910302,59.889026",
#         "spn": "0.3,0.3"
#     },
# )
