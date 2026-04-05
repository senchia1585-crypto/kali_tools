import requests as r
while True: # while true for continue
    target=input("\nPlease enter ur target (enter '0' 退出!): ") # enter the ip
    if target.lower()=="0":
        print("tq for ur using ,bye!")
        break 
    if not target.startswith("http"):
        target=f"http://{target}"
    directions={"admin","login","config","backup" , "uploads","phpmyadmin"} # the path for some location
    print(f"screening...:{target} , please wait ")
    for path in directions:
        aim=f"{target}/{path}"
        try:
            answer=r.get(aim, timeout=5) # screening 5 second and then out 
            if answer.status_code==200: # 200 = success # 404 = error 403=not found 
                print(f"[success (+)]找到隐藏路径：{aim}")
                print(f"[oh success yeah :) ]here is ur thing:{answer.text.strip()}") # use answer.text.strip give me ans
            else:
                print(f"[fail (-)] ip不存在:{path}(装态:{answer.status_code})" ) # answer.status_code give me result that i understand 1

        except Exception as e:
            print(f"[warning!]无法连接:{aim} (pls check!)") # use except to prevent wrong situation 

    print(f"[the end!] screening end ! pls check ur result !")
    # in kali using mousepad to paste the code inside 
    # and then python3 the mousepad code
    # using these in kali 


            


