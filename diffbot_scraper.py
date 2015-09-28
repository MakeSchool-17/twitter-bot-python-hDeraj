import requests


def get_api_key():
    with open("data/diffbot_api_key.txt") as f:
        key = f.read().split("\n")[0]
        return key


def get_all_links():
    links = []
    with open("data/debate_links.txt", "r") as f:
        for line in f:
            title = line.split(": ")[0].strip()
            link = line.split(": ")[1].strip()
            links.append((title, link))
    return links


def diffbot_get_link(key, link):
    print("getting: ", link)
    url = "http://api.diffbot.com/v3/article"
    params = {'token': key,
              'url': link,
              'discussion': 'false'}
    res = requests.get(url, params)
    if not res.json()['objects']:
        print("FAILED: ", link)
        return None
    res_obj = res.json()['objects'][0]
    return res_obj['text']


if __name__ == "__main__":
    key = get_api_key()
    links = get_all_links()

    for title, link in links:
        text = diffbot_get_link(key, link)
        if not text:
            continue
        with open("data/corpus/" + title.replace(" ", "_"), "w") as f:
            f.write(text)
