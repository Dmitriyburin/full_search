from functions.geocoder import get_ll_span
from functions.mapapi_PG import show_map


def main():
    toponym_to_find = input('Что будем искать?\n')

    if toponym_to_find:
        ll, spn = get_ll_span(toponym_to_find)
        point_param = {
            "ll": ll,
            "spn": spn,
            "l": "map",
            "pt": f'{ll},pm2rdm'
        }

        show_map(params=point_param)

    else:
        print('No data')


if __name__ == "__main__":
    main()
