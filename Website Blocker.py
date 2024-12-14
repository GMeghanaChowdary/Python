import time
from datetime import datetime
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
website_list = ["www.facebook.com", "facebook.com"]
def block_websites():
    while True:
        if datetime.now().hour >= 9 and datetime.now().hour < 17:
            with open(hosts_path, 'r+') as file:
                content = file.read()
                for website in website_list:
                    if website not in content:
                        file.write(redirect + " " + website + "\n")
        else:
            with open(hosts_path, 'r+') as file:
                content = file.readlines()
                file.seek(0)
                for line in content:
                    if not any(website in line for website in website_list):
                        file.write(line)
                file.truncate()
        time.sleep(5)
block_websites()
