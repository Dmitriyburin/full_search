import requests

server = input()
port = input()
a, b = input(), input()

params = {
    "a": a,
    "b": b,
}
response = requests.get(f'{server}:{port}', params=params)
json_obj = response.json()
print(' '.join(list(map(str, sorted(json_obj['result'])))),
      json_obj['check'], sep='\n')
