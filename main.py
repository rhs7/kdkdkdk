try:
	import requests
	import random
	import threading
	import pyfiglet
	
	
O = '\033[0;37m'
Le = pyfiglet.figlet_format(' climer [:] ')
print(O+Le)

heros1 = 'qwertyuiopasdfghjklzxcvbnm1234567890'
num = '1234657890'
id = input("\033[0;37mEnTeR iD : ")
token = input("\033[0;37mEnTeR ToKeN : ")
sessionid = input("\033[0;37mEnTeR sEssioniD : ")
def Lev ():

	hea = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'user-agent': 'user-agent: Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html',
        'Cookie': 'sessionid='+sessionid,
    }
	while True:
	   time2 = str("".join(random.choice(num)for x in range (3)))
				time3 = str("".join(random.choice(num)for x in range (2)))
				user = str("".join(random.choice(heros1)for x in range(1)))
	   user1 = str("".join(random.choice(heros1)for x in range(1)))
	   user2 = str("".join(random.choice(heros1)for x in range(1)))
	   user3 = str("".join(random.choice(heros1)for x in range(1)))
	   user5 = (user1+user2+'.'+user3)
	   user6 = (user1+user2+'_'+user3)
	   user7 = (user+user1+user2+user3)
	   user8 = (user3+'_'+user3+user)
	   heros= (user5, user6, user7, user8,)
	   user = random.choice(heros)
				time9 = (time2+time3)
				time10 = (time3+time2)
				abood = (time3, time2,)
				haha = random.choice(abood)
	   tiko = f'https://www.tiktok.com/api/user/detail/?aid=1988&app_language=ar&app_name=tiktok_web&battery_info=0.32&browser_language=ar&browser_name=Mozilla&browser_online=true&browser_platform=MacIntel&browser_version=5.0%20%28Macintosh%3B%20Intel%20Mac%20OS%20X%2010_15_7%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F109.0.0.0%20Safari%2F537.36&channel=tiktok_web&cookie_enabled=true&device_id=7193110014067459586&device_platform=web_pc&focus_state=true&from_page=user&history_len=10&is_fullscreen=false&is_page_visible=true&language=ar&os=mac&priority_region=&referer=&region=SA&screen_height=900&screen_width=1440tz_name=Asia%2FRiyadh&uniqueId={user}&verifyFp=verify_ldvov399_du9goymx_OHxC_4RTw_AEjU_Dth4CFGFw3lR&webcast_language=ar&msToken=f7RQRFGwBsu3WXbrhdLVX9gDRSynM_O_C7U9SX6WNqZqmb0QEsNO6H3dJ10pMAxt24bmyb2eMNPzUpr8w8-6Wx-xAawe1R6vbD6HZdDoWTPL4VOHo6ebwjHadXlUoyhG9ovbpBnhHipd_EWG&X-Bogus=DFSzswVY9D0ANeIIShUJbR/F6qHH&_signature=_02B4Z6wo00001xH2Y0gAAIDCaTiITAKYgosR9mfAAKeo28'
	   reqsnd = requests.get(tiko, headers=hea).text
	   if '"statusCode":10221,' in reqsnd:
	           print(f'\033[0;32m uSeR is Available! | {user}')
	           requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={id}&text=Nigga iAm Here : @{user} | After : {haha}")
	   else:
	   	print(f'\033[0;31mmuSeR is NoT Available | {user}')
Threads=[] 
for t in range(1):
    x = threading.Thread(target=Lev)
    x.start()
    Threads.append(x)
for Th in Threads:
    Th.join()