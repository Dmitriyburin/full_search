import sys, pprint

from functions.business import find_businesses
from functions.distance import lonlat_distance
from functions.geocoder import get_ll_span
from functions.mapapi_PG import show_map


def main():
    toponym_to_find = input('Что будем искать?\n')

    ll, spn = get_ll_span(toponym_to_find)
    lat, lon = map(float, ll.split(","))

    organization = find_businesses(ll, spn, "аптека", results="10")
    pt, points = [], []
    for i in range(10):
        point = organization[i]["geometry"]["coordinates"]
        org_lat = float(point[0])
        org_lon = float(point[1])
        color = 'pm2grl'
        if "Hours" in organization[i]["properties"]["CompanyMetaData"]:
            color = 'pm2bll'
            if "TwentyFourHours" in organization[i]["properties"]["CompanyMetaData"]["Hours"]["Availabilities"][0]:
                if organization[i]["properties"]["CompanyMetaData"]["Hours"]["Availabilities"][0]["TwentyFourHours"]:
                    color = 'pm2gnl'

        points.append(point)
        pt.append(f"{org_lat},{org_lon},{color}")

    distances = list(map(lambda p: lonlat_distance(p, (lat, lon)), points))
    max_distance_pt = pt[distances.index(max(distances))]
    org_lat, org_lon = float(max_distance_pt.split(',')[0]), float(max_distance_pt.split(',')[1])
    map_param = {
        "ll": ll,
        "spn": ','.join([str(abs(lat - org_lat) * 2), str(abs(lon - org_lon) * 2)]),
        "l": "map",
        "pt": f"{ll}~{'~'.join(pt)}"
    }

    show_map(params=map_param)


if __name__ == "__main__":
    main()
