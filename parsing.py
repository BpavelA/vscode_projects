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

print(result)

# for row in all_rows:
#     if row != "\n":
#         lst.append(row)

# # print(lst[0] , lst[-1])

# link = lst[-1]

# # link = link.find("href")

# # soup = BeautifulSoup(link, "lxml")
# print(link)