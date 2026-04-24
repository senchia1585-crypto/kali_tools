import requests as r
import time as t
import threading as thr
import random as rd
# same as screener2.0 but add muti_threading and more user-agent to make it more like a human and avoid too much thread at the same time
id_list = [
    # Windows - Chrome
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
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
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    # Linux - Firefox
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/121.0",
    # iPhone - Safari
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_2_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2 Mobile/15E148 Safari/604.1",
    # iPhone - Chrome
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/120.0.6099.101 Mobile/15E148 Safari/604.1",
    # Android - Chrome
    "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36",
    # Android - Samsung Browser
    "Mozilla/5.0 (Linux; Android 13; SM-S901B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36 SamsungBrowser/23.0",
    # Chrome on iPad
    "Mozilla/5.0 (iPad; CPU OS 17_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/120.0.6099.101 Mobile/15E148 Safari/604.1",
    # Windows 11 - Opera
    "Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 OPR/106.0.0.0",
    # macOS - Opera
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 OPR/106.0.0.0",
    # generic mobile
    "Mozilla/5.0 (Linux; Android 10; Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36",
    # another Android
    "Mozilla/5.0 (Linux; Android 11; SM-A515F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36",
    # older Windows
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
    # Chromebook
    "Mozilla/5.0 (X11; CrOS x86_64 14541.0.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    # DuckDuckGo Privacy Browser
    "Mozilla/5.0 (Linux; Android 12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36 DuckDuckGo/5"
]
maxi_threads=thr.Semaphore(10) # set the max thread to 10 to avoid too much thread at the same time and then it can be more like a human and avoid too much thread at the same time
number_429=0 # if 429 more than 3 times then break the loop and stop the scan ! or add more time to sleep
def muti_scan(aim,header,path): # path is second to read the inside path make staff understand path contain the path to let staff screnning with knowing path
     # def the muti_scan function for muti_threading use def because many staff will follow below instruction and then it can be more like a human and avoid too much thread at the same time
    global number_429 # if 429 more than 3 times then break the loop and stop the scan ! or add more time to sleep # make staff now 429
    try:
        with maxi_threads: # only 10 satff get in this code at the same time to avoid too much thread at the same time and then it can be more like a human and avoid too much thread at the same time
            answer=r.get(aim, headers=header, timeout=15, allow_redirects=False) 
            print(f"try to screnning..... : {aim}" + " "*10,end="\r")
            t.sleep(rd.uniform(5,8)) # random sleep if more sensitive path ex:env git admin add the time above 10s   to make u more like a human
            if answer.status_code==200:
                print(f"[success!!! check the file]:\n{aim}\n")
                with open("answer.txt","a",encoding="utf-8") as w1:
                    print(f"try to write the answer in txt document写入txt中: {aim}\n")
                    time=t.localtime()
                    print(f"\n{time.tm_hour}:{time.tm_min}:{time.tm_sec}--->try to screening: {aim}")
                    w1.write(f"[+ Found! ]: {aim}\n")
                    w1.write(f"content:\n{answer.text[:400].strip()}---\n") # write down only 400 word to file!
            elif answer.status_code==403:
                print(f"[403 Forbidden]可能存在访问控制问题，路径可能存在但无法访问:\n{aim}\n")
                with open("answer.txt","a",encoding="utf-8") as w2:
                    print(f"try to write the answer in txt document写入txt中: {aim}\n")
                    w2.write(f"[403 Forbidden]可能存在访问控制问题，路径可能存在但无法访问:\n{aim}\n")
            elif answer.status_code==401:
                print(f"{answer.status_code}\n发现好料!但要认证!:\n{aim}\n可以尝试暴力破解认证.开inspect看源码试or开console暴力破解!#039!")
                with open("answer.txt","a",encoding="utf-8") as wr3:
                  print(f"写入!但要认证!:{aim}")
                  wr3.write(f"以尝试暴力破解认证.开inspect看源码试or开console暴力破解!:\n{aim}")
            elif answer.status_code==500:
                print(f"[!!!有问题]\n{answer.status_code}")
            elif answer.status_code==429:
                print(f"[!!!!!!warning !]:\n {answer.status_code}")
                print("ip or web may refuse connection pls wait for a while ...")
                 # if 429 more than 3 times then break the loop and stop the scan ! or add more time to sleep
                #number_429 # if 429 more than 3 times then break the loop and stop the scan ! or add more time to sleep
                number_429 += 1 # if 429 more than 3 times then break the loop and stop the scan ! # dont sleep first !
                if number_429>=3: # if 429 more than 3 times then break the loop and stop the scan ! # make one staff know 429
                    print(f"pls check ur network or target may have problem:\n{answer.status_code}") 
                    print(f"可能是网络问题或者目标站点有问题，请检查！大概是被封了，等一会再试!{number_429}次429了!") 
                    return # if 429 more than 3 times then break the loop and stop the scan !
                t.sleep(30)
            elif answer.status_code==405:
                        print(f"有好料但不给:\n{answer.status_code}")
            elif answer.status_code==520:
                        print(f"它自爆了!!!!:\n{aim}\n去kali试试!")
                        with open("answer.txt","a",encoding="utf-8") as www3:
                          print(f"它自爆了!!!!:\n{aim}\n去kali试试! try 404path aslo !!!!!")
                          www3.write(f"它自爆了!!!!:\n{aim}\n去kali试试!")
            elif answer.status_code==301 or answer.status_code==302:
                        print(f"可能存在重定向问题，路径可能存在但被重定向了:\n{aim}\n")
                        with open("answer.txt","a",encoding="utf-8") as w4:
                            print(f"try to write the answer in txt document写入txt中: {aim}\n")
                            w4.write(f"可能存在重定向问题，路径可能存在但被重定向了或被人乱丢进:\n{answer.headers.get('Location')}|\n它叫我滚!: {aim}\n")
            else: # 404
                pass
    except Exception as get_wrong: # for rquests error
        print(f"pls check:\n{get_wrong}")
if __name__=="__main__": #run this code fist to avoid the problem of muti_threading and then it can be more like a human and avoid too much thread at the same time
        try:
            while True:
                print("""This version is 3.0 of screnner加入多线程,
                       it add muti_threading and more user-agent to make it more like a human and 
                       avoid too much thread at the same time!
                       This is only use for screenning website 扫网站 
                Kindly reminder: this tools is only for learning and testing, please do not use it for illegal purpose! 仅供学习和测试，请勿用于非法用途！
                    This script is only use for support to scan path or file that may have in website ,
                    you have to manually check the content of the path or file to confirm whether it is useful or not!
                    Manually dig for vulnerability! 需要手动挖漏洞！
                    """)
                header={f"User-agent":rd.choice(id_list)} # random to choice one of the ip #here header make coding remember to use it in muti_scan function ! and then it can be used in muti_scan function for get request ! and then it can be more like a human and avoid too much thread at the same time
                target=input("Pls enter ur target[enter '0' to leave]:\n").strip()
                if target.strip()=='0':
                    print("tq for ur using bye!!")
                    break
                if not target.startswith("http"):
                    target=f"https://{target}"
                file_path={"dict.txt","dict2.0.txt"} # first for is open 2 file
                for f_name in file_path: 
                    try:
                        with open(f_name,"r",encoding="utf-8") as read: # read the file
                            print(f"try to open txt document for screnning打开中: {f_name}\n Your target目标:\n{target}")
                            for l in read: # l for read the file contain
                                path=l.strip()
                                if not path or path.startswith("#"):
                                    continue
                                if number_429>=3: # if 429 more than 3 times then break the loop and stop the scan ! # main announcement for 429 
                                    print(f"pls check ur network or target may have problem:\n{number_429} times 429了!") 
                                    break # if 429 more than 3 times then break the loop and stop the scan !
                                aim=f"{target.rstrip('/')}/{path.lstrip('/')}"
                                thread=thr.Thread(target=muti_scan, args=(aim,header,path)) # arg is a tuple so that it can be run by muti_scan and it will continue run until all path is scaned !
                                thread.daemon=True # set the thread as daemon # auto exit!
                                thread.start() # start the thread and sleep for a while to make it more like a human and avoid too much thread at the same time
                                t.sleep(rd.uniform(3,5)) # sleep for a while to make it more like a # this time for staff
                    except Exception as file_wrong:
                        print(f"something wrong ! pls check:\n"+ "=="*20 + f"{file_wrong}")
        except KeyboardInterrupt as keyyy: # the thread will auto exit and then add this statement!
             print(f"[!]收到收到退出信号，正在退出...:\n{keyyy}")    
             t.sleep(3) #give some time to exit the program and then it can be more like a human and avoid too much thread at the same time1
             print("Bye!感谢使用！")           # stop will run this statement and then it can be more like a human and avoid too much thread at the same time
print("pls check ur result in answer.txt or check the code for more details !")
                                

