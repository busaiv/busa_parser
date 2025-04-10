import time
import requests
import json

def try_request(session, request_type, url, tries=5, **kwargs):
    while tries > 0:
        try:
            if request_type == 'post':
                response = session.post(url, **kwargs).json()
            elif request_type == 'get':
                response = session.get(url, **kwargs).json()
            else:
                return f'{session} is unsupported type for session'
            return response
        except ConnectionError as e:
            time.sleep(20)
            tries -= 1
            return f'Retries left {tries} | {e}'
        except requests.exceptions.JSONDecodeError as e:
            time.sleep(300)
            tries -= 1
            return f'Retries left {tries} | {e}'
    return 'SHUTDOWN'

def shutdown_scenario(response_data, file_name, parsed_data):
    if response_data == 'SHUTDOWN':
        save_data(file_name, parsed_data)
        raise Exception('SHUTDOWN | data saved')

def save_data(file_name, data):
    with open(f'data/{file_name}.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def read_data(file_name):
    with open(f'data/{file_name}.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data