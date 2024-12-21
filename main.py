import requests
from lxml import etree

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

def parse_xml(text):
    print("start parse")
    root = etree.fromstring(text.encode('utf-8'))
    print("end parse")
    return root
    

def format_top_10(level_id):
    print("start format")


def main():
    top10 = [
        []
    ]
    t10index = 0
    try:
        level_id = int(input("level_id: "))
    except ValueError:
        print("ValueError")
        return 1
    response = fetch_data(1, level_id, "completion_time")
    if response is None:
        print("Failed to fetch data.")
        return 1
    else:
        print("Response received")
        rps = parse_xml(response)
        for rp in rps:
            username = rp.attrib.get('un')
            clear_time = rp.attrib.get('ct')
            date_of_clear = rp.attrib.get('dt')
            # save to top 10 if not in hashmap
            

if __name__ == "__main__":
    main()