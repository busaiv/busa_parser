import time
import requests
import json
from tqdm import tqdm
from colorama import Fore

def try_request(session, request_type, url, tries=5, **kwargs):
    while tries > 0:
        try:
            if request_type == 'post':
                response = session.post(url, **kwargs).json()
            elif request_type == 'get':
                response = session.get(url, **kwargs).json()
            else:
                tqdm.write(f'{session} is unsupported type for session')
                return None
            return response
        except requests.exceptions.RequestException as e:
            tqdm.write(f'{Fore.LIGHTYELLOW_EX}\n[ERROR] MaxRetryError: waiting for 60 seconds\nretries left: {tries}'
                       f'\ndetails: {e}\n')
            time.sleep(60)
            tries -= 1
        except requests.exceptions.JSONDecodeError as e:
            tqdm.write(f'\n{Fore.LIGHTYELLOW_EX}[ERROR] JSONDecodeError: waiting for 300 seconds\nretries left: {tries}'
                       f'\ndetails: {e}\n')
            time.sleep(300)
            tries -= 1
        except Exception as e:
            tqdm.write(f'\n{Fore.LIGHTYELLOW_EX}[ERROR]: waiting for 60 seconds\nretries left: {tries}'
                       f'\n error details: {e}\n')
            time.sleep(60)
            tries -= 1
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