
The project features a backend for a shop using MongoDB on localhost:27017, Flask as API.

Installation:

- clone project:
"""
git clone https://github.com/
"""
- create venv:
```
python3 -m venv env
source env/bin/activate
```
- install requirements:
pip install -r requirements.txt
- start server:
python "server.py"

API usage:

- create:
curl -X POST "http://127.0.0.1:80/api/phone/" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{\"name\":\"Redmi\",\"description\":\"mobile phone\",\"parameters\":[{\"OS\":\"Android\"},{\"color\":\"green\"}]}"
- read one:
curl -X GET "http://127.0.0.1:80/api/phone/5fbc06cb11bcf5cbbd8b6c3d" -H  "accept: application/json"
- read filtering by parameters:
curl -X GET "http://127.0.0.1:80/api/phones/?OS=Android&color=green" -H  "accept: application/json"
