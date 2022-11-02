import json
import requests
import lxml
import lxml.html
from lxml import etree

r = requests.get('https://currate.ru/api/?get=rates&pairs=USDRUB&key=be54ddc3c404c7ee2894e325f1cea893')
kurs = json.loads(r.content)

print(kurs['data']['USDRUB'])
