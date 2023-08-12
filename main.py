import random, string
import time
import requests
import datetime

print("\n此程式原作者：KJW (kangjwme) ， 修改者：ChenArnold (3.14159265358)\n")
print("事先聲明，這些代碼都是亂數產生，再檢查可用性，個人覺得機率很低！如果都不可用請不要怪程式！")
txtwriter=open("NitroCodes.txt","w", encoding='utf-8')

print("\n\n隨機生成代碼中...\n\n")

NitroCount = 0

for n in range(int(10000)):
   #尾數亂數生成
   possiblecode = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(24))
   #連結組合
   txtwriter.write('https://discord.gift/')
   txtwriter.write(possiblecode)
   txtwriter.write("\n")
   NitroCount += 1

txtwriter.close()

print(f"已生成{NitroCount}個Nitro代碼，目前準備開始檢查")
print("我們無法保證您查看時是否已失效，故您有看見「可用」開頭的代碼，請盡速領取")
print("\n\n")

#驗證連結可用性
with open("NitroCodes.txt") as txtwriter:
    print("開始測試！\n")
    for line in txtwriter:
        try:
            nitro = line.strip("\n")

            url = "https://discordapp.com/api/v6/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"

            r = requests.get(url)

            if r.status_code == 200:
                print(r.status_code," 可用 | {} ".format(line.strip("\n")),"偵測時間：",datetime.datetime.now())
                canuse=open("NitroCanUseCodes.txt","w", encoding='utf-8')
                canuse.write(line)
                canuse.close()
            elif r.status_code == 429:
                print(r.status_code," 請求過多，將於600秒後重試",datetime.datetime.now())
                time.sleep(600)
            else:
                print(r.status_code," 不可用 | {} ".format(line.strip("\n")),"偵測時間：",datetime.datetime.now())
                time.sleep(30)
        except:
            print("目前斷網! 偵測時間：",datetime.datetime.now())
            time.sleep(30)
            
   
        	
input("檢查完畢，請查看 NitroCanUseCodes.txt 檔案，裡頭是可以使用的Nitro連結喔！(我們無法保證您查看時是否已失效)")
