import requests

def fetch_data(page, level_id, sortby):
    try:
        url = 'https://totaljerkface.com/replay.hw'
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        data = {
            'action': 'get_all_by_level',
            'page': page,
            'level_id': level_id,
            'sortby': sortby
        }
        response = requests.post(url, headers=headers, data=data)
        response.raise_for_status()
        return response.text
    except requests.RequestException:
        print("request error")
        return None

def main():
    try:
        level_id = int(input("level_id: "))
    except ValueError:
        return 1
    print(fetch_data(1, level_id, completion_time))