import requests

# Sets list
def set_list():
    url = 'https://api.scryfall.com/sets'
    headers = {'user-agent': 'mtgst1/0', 'Accept': '*/*'}
    r = requests.get(url, headers=headers)
    print((r.url) + ' - Status code: ' + str(r.status_code))
    data = r.json()

    set_infos = []
    for set_info in data['data']:
        set_code = set_info['code']
        set_name = set_info['name']
        set_release_date = set_info['released_at']
        set_infos.append({'code': set_code, 'name': set_name, 'released at': set_release_date})
    return set_infos

# Cards list from a specific set
def set_card_list():
    url = 'https://api.scryfall.com/cards/search'
    headers = {'user-agent': 'mtgst1/0', 'Accept': '*/*'}
    payload = {'q': 'set:lea', 'order': 'name'}
    r = requests.get(url, payload, headers=headers)
    print((r.url) + ' - Status code: ' + str(r.status_code))
    data = r.json()

    card_infos = []
    for card_info in data['data']:
        card_rarity = card_info.get('rarity', 'Unknown')
        card_name = card_info.get('name', 'Unknown')
        card_collector_number = card_info.get('collector_number', 'Unknown')
        card_infos.append({'rarity': card_rarity, 'name': card_name, 'collector number': card_collector_number})
    return card_infos
