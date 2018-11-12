import requests
from bs4 import BeautifulSoup

r = requests.get("http://wowturkey.com/") ("linkteki kodları görmeye yarar")
r.content ("linkteki kodları ekrana bastırır")

soup = BeautifulSoup(r.content)
print(soup.prettify()) ("linkteki kodları dünzenleyip ekrana basar")

soup.find_all("a") ("sayfadaki bütün linkleri çeker")

linkler = soup.find_all("a") ("linkleri tek tek basar")
for link in linkler:
    print(link)

for link in linkler:
    print(link.get<"href">) ("sayfada kaç link var onu görmeye yarar")

for link in linkler: 
    print(link.text,link.get<"href>")
