import requests
url = "http://postb.in/0tLKmdJc"
requests.get(url)
type(requests.get(url))
r = requests.get(url) (metodları görme)
r.status_code (doğru çalışıyomu diye kontrol etme)
r.ok (true)
r.url ( istek atılan url i görme)
r = requests.post(url) ( post atma)
r = requests.post(url,data={"username":"bandolero","password":"123"})

