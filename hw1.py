# Добавить в задание с REST API ещё один тест, в котором создаётся новый пост, а потом проверяется его наличие на сервере по полю «описание».
# Подсказка: создание поста
# выполняется запросом к https://test-stand.gb.ru/api/posts с передачей параметров title, description, content.

import requests
import yaml


with open('config.yaml') as f:
    testData = yaml.safe_load(f)


def token_auth(token):
    response = requests.get(url=testData['url1'], headers={'X-Auth-Token': token}, params={"owner": testData['username']})
    conten_var = [item['content'] for item in response.json()['data']]
    return conten_var

def test_create_post(login):
    response = requests.post(url=testData['url'], data={'username': testData['username'], 'password': testData['password']})
    token = response.json()['token']
    post = requests.post(url=testData['url1'], headers={'X-Auth-Token': token}, params={'title': testData['title'], 'description': testData['description'], 'content': testData['content']})
    posts_from_response = post.json()['description']
    assert testData['description'] in posts_from_response

def test_check_post_content(login):
    assert testData['content'] in token_auth(login)






