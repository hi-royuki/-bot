import requests

r = requests.get('https://book.impress.co.jp/')
print(r.status_code)
