import sys

from functions.business import find_business
from functions.distance import lonlat_distance
from functions.geocoder import get_ll_span
from functions.mapapi_PG import show_map


def main():
    toponym_to_find = input('Что будем искать?\n')

    ll, spn = get_ll_span(toponym_to_find)
    lat, lon = map(float, ll.split(","))

    organization = find_business(ll, spn, "аптека")
    point = organization["geometry"]["coordinates"]
    org_lat = float(point[0])
    org_lon = float(point[1])

    name = organization["properties"]["CompanyMetaData"]["name"]
    address = organization["properties"]["CompanyMetaData"]["address"]
    time = organization["properties"]["CompanyMetaData"]["Hours"]["text"]
    distance = round(lonlat_distance((lon, lat), (org_lon, org_lat)))

    snippet = [
        f"Аптека: {name}",
        f"Адрес: {address}",
        f"Время работы: {time}",
        f"Расстояние: {distance} м."
    ]

    map_param = {
        "ll": ll,
        "spn": ','.join([str(abs(lat - org_lat) * 2), str(abs(lon - org_lon) * 2)]),
        "l": "map",
        "pt": f"{ll}~{org_lat},{org_lon},pm2dgl"
    }

    show_map(params=map_param, text=snippet)


if __name__ == "__main__":
    main()
