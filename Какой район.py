import requests

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
        return toponym
    print("Ошибка выполнения запроса:")
    print(geocoder_request)
    print("Http статус:", response.status_code, "(", response.reason, ")")
    return False


coords = get_geocoder(input())["Point"]["pos"].split()
district = get_geocoder(','.join(coords), kind='district')\
    ['metaDataProperty']['GeocoderMetaData']['Address']['Components'][4]['name']
print(district)
