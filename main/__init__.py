import requests
import json
import datetime
import os

json_f = os.path.join('data', 'newfile.json')
key = os.getenv('API_KEY')
symbols = 'RUB'