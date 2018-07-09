import time
from datetime import datetime as dt

hosts_temp=r"F:\Desktop\5sem\python\project_2\hosts"
hosts_path=r"C:\Windows\System32\drivers\etc\hosts"
redirect="127.0.0.1"
website_list=["www.facebook.com","www.gmail.com","github.com"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,18) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,19):
        print("work hors.....")
        with open(hosts_path,'r+') as file:
            content=file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+ website+"\n")
        
    else:
        with open(hosts_path,'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        
        print("fun hours...")
    time.sleep(5)
    
