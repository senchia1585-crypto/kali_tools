import requests as r
import sys
import time
import random
while True: # while true for continue
    print("\n"+ "="*50)
    print(":)"*10)
    print("This coding only use for cyber range without save the important thing to file !")
    print("不要乱用!")
    print("(ㄏ￣▽￣)ㄏ ㄟ(￣▽￣ㄟ)"*3)
    target=input("\nPlease enter ur target (enter '0' 退出!): ") # enter the ip
    if target.strip()=='0':
        print("tq for ur using ,bye!")
        break
    if not target.startswith("http"):
        target=f"http://{target}"
   # directions={"admin","login","config","backup" , "uploads","phpmyadmin"} # the path for some location
    with open("dict.txt","r",encoding="utf-8") as f: # 读取字典脚本 # remember with have space to while loop!
        print(f"screening...:{target} , please wait ")
        for read in f.readlines(): # read 脚本
            path=read.strip() #读取read的脚本
            if not path or path.startswith("#"):
                continue
            aim=f"{target}/{path}"
            print("\r")
            try:
                print(f"Screening:\n{aim}     \nPls wait.....")
                time.sleep(random.uniform(0.1,0.6)) # use for random click from ? - ?
                #INFO=time.localtime()
               #print([INFO])
                answer=r.get(aim, timeout=5) # screening 5 second and then out 
                if answer.status_code==200: # 200 = success # 404 = not found 403 = error
                    print(f"[success (+)]找到隐藏路径：{aim}")
                    print(f"[oh success yeah :) ]here is ur thing:\n{answer.text.strip()}") # use answer.text.strip give me all ans # strip print all the strip
                    #if path in answer.text: # only have come out same with dict word will be save!
                    with open("answer.txt","a",encoding="utf-8") as a:
                        a.write(f"Your path !:\n{path}\nYour content !:\n{answer.text.strip()}") # write the dict.txt word that have path contain
                        print(f"已保存!!! 相关路径：\n{path}\n 还有相关内容哦~ :\n{answer.text.strip()}")
                elif answer.status_code==403:
                    print(f"[Warning !]:{aim}禁止访问!")
                else: #404 #will run this or other
                 print(f"[fail (-)] ip不存在:{path}(装态:{answer.status_code})" ) # answer.status_code give me result that i understand 1

            except Exception as e:
                print(f"[warning!]无法连接:{aim}   pls check!:\n{e}") # use except to prevent wrong situation 
            except FileNotFoundError as f_not:
                print("oh no !\n Cannot find:\n{f_not}\n pls check your file path ! 请捡查相关问题！")

print(f"[the end!] screening end ! pls check ur result !")
        # in kali using mousepad to paste the code inside 
        # and then python3 the mousepad code
        # using these in kali 



            


