from flask import abort
import requests

def authControl(headers):
    url = 'http://localhost:8000/api/tokenCheck'

    response = requests.post(url, headers={
        'Authorization': headers.get('Authorization'),
        'userId': headers.get('userId')
    })
    if response.status_code != 200 or response.text == 'false':
        abort(401, 'Token Is Invalid')
    else:
        print('Token success')
