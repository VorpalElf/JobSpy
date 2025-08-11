import requests
from bs4 import BeautifulSoup

BASE_URL = "https://proxydb.net/?country=&offset={offset}&protocol=https"
TOTAL_PROXIES = 1352
PAGE_SIZE = 30

proxies = []

for offset in range(0, TOTAL_PROXIES, PAGE_SIZE):
    url = BASE_URL.format(offset=offset)
    print(f"Downloading proxies from: {url}")
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    table = soup.find("table")
    if table:
        tbody = table.find("tbody")
        if tbody:
            for tr in tbody.find_all("tr"):
                tds = tr.find_all("td")
                if len(tds) > 1:
                    ip_a = tds[0].find("a")
                    port_a = tds[1].find("a")
                    if ip_a and port_a:
                        ip = ip_a.text.strip()
                        port = port_a.text.strip()
                        proxies.append(f"{ip}:{port}")

with open("proxies.txt", "w") as out:
    for proxy in proxies:
        out.write(proxy + "\n")

print(f"Extracted {len(proxies)} proxies.")