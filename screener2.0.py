import requests as r
import time as t 
import random 
import selenium
id_list = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
]
while True:
    print("this version 2.0 it may update! 2.0 版测试加多新功能!")
    print("This is only use for screen website 扫网站")
    print("=="*20)
    print("aim for : information Disclosure[泄露] and access control[未经访问]")
    target=input("Pls enter ur target(ex: http....[enter '0' to leave]:\n").strip()
    if target.strip() =='0':
        print("tq for ur using bye !")
        break
    if not target.startswith("http"): # IF NOT START with http
       target="http://"+ target
    file_path={"dict.txt", "dict2.0.txt"} # first for use for read file first
    for f_name in file_path: # open the above file_path !
        try:
            with open(f_name,"r",encoding="utf-8") as read: # second open for open inside !
              print(f"try to open txt document for screening打开中: {f_name}\n Your target目标:\n{target}")
              for l in read: # second for use to screen inside dict and dict2.0 # read line by line
               path=l.strip() # all path 
              if not path or path.startswith("#"):
                 continue
              aim=f"{target.rstrip('/')}/{path.lstrip('/')}" # auto settle /  ex:rstrp--->google.com//... cut ///  lstrip-->///google.com cut /one
              header={f"User-agent":random.choice(id_list)} # random to choice one of the ip
            try:
              print(f"try to screnning..... : {aim}",end="\r")
              t.sleep(random.uniform(0.1,0.6))
              answer=r.get(aim , headers=header, timeout=5, allow_redirects=False) # if false will not follow again ! # get with headers so that let u become a human
              if answer.status_code==200:
                 print(f"[+ success ! ]found: \n{aim}\n")
                 print(f"content:\n{answer.text[:80].strip()}---")# write down only 80 word to file!
                 try:
                    with open("answer.txt","a",encoding="utf-8") as wr:
                       print(f"[+ success]found!:\n{path}")
                       wr.write(f"态状 status找到!found:\n{aim}")
                 except Exception as e1:
                    print(f"[fail ! pls check]\n:{e1}")
              elif answer.status_code ==403:
                 print(f"{answer.status_code}\n没权限!")
                 print(f"To:{target}")    
                 try:
                     with open("answer.txt","a",encoding="utf-8") as wr2:
                       print(f"写入!:路径:\n{aim}")
                       wr2.write(f"{aim}\n")
                 except Exception as e2:
                    print(f"pls check:\n{e2}")
              elif answer.status_code==429:
                 print(f"[!!!!!!warning !]:\n {answer.status_code}")
                 print("ip may refuse connection pls wait for 10s ...")
                 t.sleep(10)
              elif answer.status_code==401:
                 print(f"{answer.status_code}\n发现好料!:\n{aim}")
                 with open("answer.txt","a",encoding="utf-8") as ww:
                    ww.write(f"[401!]:\n{aim}")
                 try:
                     with open("answer.txt","a",encoding="utf-8") as wr3:
                       print(f"写入!:{aim}")
                       wr3.write(f"{aim}")
                 except Exception as e2:
                    print(f"{e2}")
              elif answer.status_code==405:
                 print(f"有好料但不给:\n{answer.status_code}")
              elif answer.status_code==500:
                 print(f"[!!!有问题]\n{answer.status_code}")
              else: # 404
                 pass
            except Exception as get_wrong:
                print(f"pls check\n:{get_wrong}")
        except Exception as e_final:
           print(f"may have problem!!\n{e_final}")
        except FileNotFoundError as no_found:
           print(f"cannot find the file!{no_found}")
print(f"screen finish! pls check!---->answer.txt")
                       


    






