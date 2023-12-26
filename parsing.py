from requests import get
from bs4 import BeautifulSoup

#Step 1

url = "https://диктант.научим.рф/certs?sid=P0a4ab3a8"

headers = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7", 
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.721 YaBrowser/23.9.5.721 (corp) Yowser/2.5 Safari/537.36"}

# src = get(url, headers=headers)

# site = src.text

# with open("page.html", "w", encoding="utf8") as file:
#     file.write(site)

#Step 2

with open("page.html", "r", encoding="utf8") as file:
    src = file.read()

soup = BeautifulSoup(src, "lxml")

all_rows = soup.find("tbody").find("tr").find_all("td")

result = {}

# for i in range(133):
result[all_rows[0].text] = "https://диктант.научим.рф" + all_rows[-1].find("a").get("href")

# for name, link in result.items():
#     with open(f'{name}.png', "w") as image:
#         image.write(get(link, headers=headers))

for name, link in result.items():
    certificate = get(link, headers=headers)
    with open(f'{name}.jpg', "wb") as file:
        file.write(certificate.content)
        
    

