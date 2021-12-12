import requests


def test_request(name):
    url = f"https://superheroapi.com/api/2619421814940190/search/{name}"
    response = requests.get(url)
    intelligence_ = response.json()['results'][0]['powerstats']['intelligence']
    return intelligence_

def most_intelligence(*names):
    max_ = 0
    best_name = None
    for name in names:
        service_data = int(test_request(name))
        if service_data > max_:
            max_ = service_data
            best_name = name
    print(f'Самый умный супер герой - это {best_name}')


if __name__ == '__main__':
   most_intelligence('Hulk', 'Captain America', 'Thanos')