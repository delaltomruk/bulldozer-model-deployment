import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={"YearMade": 1999, "ProductSize": 0, "SaleYear": 2012, "Enclosure": 3463})

print(r.json())