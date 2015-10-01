import requests
import time
from multiprocessing import Pool


def get_all_links():
    links = []
    print("Loading old links...")
    old = set()
    with open("data/done_readmes.txt", "r") as f:
        for line in f:
            old.add(line.strip())

    print("Loading github links...")
    with open("data/github-repositories.txt", "r") as f:
        for line in f:
            title = line.replace("/", "__").strip()
            link = line.strip()
            if title not in old:
                links.append((title, link))
    print("Finished loading links")
    return links


def get_link(pair):
    title, link = pair
    url = "https://raw.githubusercontent.com/"+link+"/master/README.md"
    res = requests.get(url)
    if res.status_code != 404:
        text = res.content
        with open("data/readmes/" + title.replace(" ", "_"), "wb") as f:
            f.write(text)


if __name__ == "__main__":
    links = get_all_links()
    print(len(links), "links to download")
    total = str(len(links))
    pool = Pool(processes=50)
    rs = pool.map_async(get_link, links)
    pool.close()

    while not rs.ready():
        time.sleep(5)
        print("waiting...")
    print(len(rs.get()))
