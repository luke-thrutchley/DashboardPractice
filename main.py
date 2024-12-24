"""

    This is a community effort discord bot for the Happy Wheels Speedrunning Community
    The majority of this code was based on code provided by _lethalpotato_ on discord

"""

import requests
from lxml import etree

def fetch_data(page, level_id, sortby):
    print("start fetch")
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
        print("end fetch")
        return response.text
    except requests.RequestException:
        print("request error")
        return None

def parse_xml(text):
    print("start parse")
    root = etree.fromstring(text.encode('utf-8'))
    print("end parse")
    return root
    

def parse_top_10(level_id, top10, top10ct, top10dt, t10index):
    print("start p10")
    page = 1
    if level_id == "":
        print("ValueError")
        return False, top10, top10ct, top10dt, t10index
    while True:
        response = fetch_data(page, level_id, "completion_time")

        if response is None:
            print(f"page {page + 1} is empty, end p10")
            return True, top10, top10ct, top10dt, t10index
        else:
            print("Response received")
            rps = parse_xml(response)
            for rp in rps:
                username = rp.attrib.get('un')
                clear_time = rp.attrib.get('ct')
                date_of_clear = rp.attrib.get('dc')
                if username in top10:
                    continue
                else:
                    top10[t10index] = username
                    top10ct[t10index] = clear_time 
                    top10dt[t10index] = date_of_clear
                    t10index += 1
                    if t10index == 10:
                        print("top10 found, end p10")
                        return True, top10, top10ct, top10dt, t10index
        page += 1

def input_level_id():
    try:
        return int(input("level_id: "))
    except ValueError:
        print("value error in input")
        return -1
    
def print_top10(level_id, top10, top10ct, top10dt, t10index):
    print(f"\nlevel id: {level_id}")
    print("*" * 70)

    i = 0
    while i < t10index:
        print(f"{i + 1}: {top10[i]}\t\ttime: {top10ct[i]}\t\tdate: {top10dt[i]}")
        i += 1

def main():
    top10 = [""] * 10
    top10ct = [0] * 10
    top10dt = [0] * 10
    t10index = 0

    level_id = input_level_id()
    flag, top10, top10ct, top10dt, t10index = parse_top_10(level_id, top10, top10ct, top10dt, t10index)

    if not flag:
        return 

    print_top10(level_id, top10, top10ct, top10dt, t10index)
           

if __name__ == "__main__":
    main()