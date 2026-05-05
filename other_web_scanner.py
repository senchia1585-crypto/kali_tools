import requests as r 
from requests.exceptions import RequestException # use to handle exceptions when the website is not alive
import random as rd
import time as t
WORDLIST_PATH ="subdomains_for_web.txt" # search from online (github)
header=["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    # Windows - Firefox
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/121.0",
    # Windows - Edge
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0",
    # macOS - Safari
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_2_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2 Safari/605.1.15",
    # macOS - Chrome
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    # macOS - Firefox
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/121.0",
    # Linux - Chrome
]
total_sub_alive=0
def scan_website(other_domains): # other_domains is my input target !
    global total_sub_alive # the number of web may alive !
    try:
        with open(WORDLIST_PATH,"r",encoding="utf-8") as r1:
            lines=[l.strip() for l in r1 if l.strip() and not l.startswith('#')] # r1 is already read
            total=len(lines)
            print(f"开始扫：{other_domains}, 共--->{total}个词条",end="\r")
            attempt_count=0
            for readd in lines :
                subdomains=readd.strip()
                attempt_count+=1
                if not subdomains or subdomains.startswith('#'):
                    continue
                sub_url=f"{subdomains}.{other_domains}"
                if not sub_url.startswith("http"):
                   sub_url=f"https://{subdomains}.{other_domains}"
                print(f"try to found:{sub_url:<50}  , 已到: {attempt_count}/{total}",end="\r")
                try: # seocnd have to inside the r1 so that it can request by using my dict
                  id={"User-agent":rd.choice(header)}
                  answer=r.head(sub_url , timeout=10,headers=id,allow_redirects=False) # sub_url make staff know the web how to take
                  t.sleep(rd.uniform(0.6,1)) # can change time 
                  status=answer.status_code
                  if status==200:
                    print(f"{sub_url} is alive")
                    if sub_url:
                     total_sub_alive+=1
                    with open("alive_websites.txt","a") as f2:
                        f2.write(f"Alive !({status}):  {sub_url}\n")
                        print(f"{sub_url} is writing to the file !写入中!")
                  elif status in[302,301]:
                     total_sub_alive+=1
                     print(f"{sub_url} is alive but it is redirecting被重定向了")
                     with open("alive_websites.txt","a") as f3:
                        f3.write(f"\nThis web is alive but it is redirecting({status}): {sub_url}\n")
                  elif status in[403,401]:
                     total_sub_alive+=1
                     print(f"{sub_url} is alive but it is forbidden ,被禁止访问")
                     with open("alive_websites.txt","a") as f4:
                        f4.write(f"\nThis web is alive but it is forbidden,被禁止访问({status}):{sub_url}\n")
                  elif status in[500,502,503,504,520]:
                     total_sub_alive+=1
                     print(f"{sub_url} is alive but it is server error服务器错误")
                     with open("alive_websites.txt","a") as f5:
                        f5.write(f"\nThis web is alive but it is server error服务器错误:({status})(try same path but different writing):{sub_url}\n")
                except RequestException:
                   pass # some of them not found
                except Exception as e1:
                  print(f"scan : {sub_url}\n error: {e1}")
            print(f"\n\n✨ 扫描完成！本次共发现 {total_sub_alive} 个存活子域名。")     
    except Exception as e:
        print(f"pls check: {e}")
    except FileNotFoundError as notfound:
      print(f"❌ 找不到字典文件: {WORDLIST_PATH}")
if __name__=="__main__":
   while True:
       print(""" Try to find some sub web by this tools!
             扫描小工具给子网址 """)
       target_url=input("Enter the target url! ['0' to end]: ")
       if target_url.strip()=='0':
           print("Thanks for using see u next time")
           break
       if target_url:
         total_sub_alive=0
         scan_website(target_url) # make target_url = other_domains
        
    
               
       