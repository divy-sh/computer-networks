import requests
import json
import configparser

config = configparser.ConfigParser()
config.read('salesforceconfig.ini')

def get_access_token():
    url = config['OAUTH']['base_url'] + '/services/oauth2/token'
    payload = {
        'grant_type': config['OAUTH']['grant_type'],
        'client_id': config['OAUTH']['client_id'],
        'client_secret': config['OAUTH']['client_secret'],
        'username': config['OAUTH']['username'],
        'password': config['OAUTH']['password']
    }
    response = requests.request("POST", url, data=payload)
    json_response = response.json()
    if 'access_token' not in json_response:
        raise Exception("getting access token failed")
    return json_response['access_token']

def get_data(access_token):
    url = config['OAUTH']['base_url'] + '/services/data/v55.0/query/'
    query_params = {
        'q': 'SELECT NAME, ID, BillingAddress FROM ACCOUNT'
    }
    headers = {
        'Authorization' : 'Bearer ' + access_token
    }
    response = requests.request("GET", url, params=query_params, headers=headers)
    return response.content

def main():
    access_token = get_access_token()
    data = get_data(access_token)
    print(data)

if __name__ == '__main__':
    main()