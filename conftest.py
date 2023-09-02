import pytest
import requests
import yaml


with open('config.yaml') as f:
    data1 = yaml.safe_load(f)

username = data1['username']
password = data1['password']
title = data1['title']
description = data1['description']
content = data1['content']
@pytest.fixture()
def login():
    obj_data = requests.post(url=data1['url'], data={'username': username, 'password': password})
    token = obj_data.json()['token']
    return token

