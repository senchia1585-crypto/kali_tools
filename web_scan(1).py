from flask import Flask,render_template,request,jsonify # flask is python version of website framework
import requests as r
import time as t
import random as rd
app=Flask(__name__)#python use to create a website and then we can use it to show the result to the user # here we create a flask app and then we will run it on port 3000
# when someone visit the website it will run the function below and return the html to the user
id_list = [
    # Windows - Chrome
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    # Windows - Firefox
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/121.0",
    # Windows - Edge
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0",
    # macOS - Safari
                   ]
header={"User-agent":rd.choice(id_list)}
@app.route("/web_scan____(version_1.0)") # this is the url that user will visit to see the website
def let_scan(): #to settle the user input and show the result to the user
    result_web="wait for user input..." # this is the result that we will show to the user when they visit the website
    result_accept=[]
    other_result=0
    feedback="301-520_status_code!"
    target=request.args.get("target") # get the target from the url # here rqeuest is use to settle the user input # and arg is user input
    file_path=["dict.txt","dict2.0.txt"] # this is the path that we will scan\
    for file_name in file_path:
                try:
                    with open(file_name,"r",encoding="utf-8") as read:
                         print(f"user target: {target}opening---->{file_name}",end="\r")
                         for l in read:
                              path=l.strip()
                              if not path or path.startswith('#'):
                                   continue
                              aim=f"{target.rstrip('/')}{path.lstrip('/')}" # combine the target and the path to get the target url # here rstrip is use to remove the last / from the target if it exist # and then we will add the path to the target to get the target url
                              print(f"scanning--->{aim}") # print the target url that we are scanning to the console
                              try:
                               t.sleep(rd.uniform(0.5,1.5)) # sleep for a random time between 0.5 and 1.5 seconds to avoid being detected by the target website
                               answer=r.get(aim,timeout=10,headers=header,allow_redirects=False) # send a get request to the target url and set the timeout to 5 seconds
                               if answer.status_code==200: # if the status code is 200 then we found the path
                                  result_accept.append(aim) # append it will write path and content
                               elif answer.status_code in [401,403,500,301,302,520]:
                                    result_accept.append(aim)
                                    user_back="Go try to find these path your may discover some things !"
                               elif answer.status_code==429:
                                    other_result=+1
                                    if other_result>=3:
                                         break
                              except Exception as e: # if there is an error then we will print the error and continue to the next path        
                                    print(f"Error: {e}")
                                    continue
                except Exception as e:
                     print(f"pls check your code or {e}")              
                
    result_web="<br>".join(result_accept) if result_accept else "No hidden path found!没有找到隐藏路径！" # directly if and else to come the result_web variable # if result is not empty then we will join the result list with <br> to make it look better in html # if result is empty then we will set the result_web to "No hidden path found!没有找到隐藏路径！"
    feedback="<br>".join(user_back) if result_accept else "No hidden path found!没有找到隐藏路径！"
    bg_src="https://www.virlan.co/tech/wp-content/uploads/2022/01/digital-technology.jpg"  # result_web is use to show the result to the user in the html # and we will return the html to the user
    return f"""
        <!DOCTYPE html>
        <html>
        <html lang="en","zh-CN">
        <meta charset="UTF-8">
        <head>
        <title>Web Scan</title>
        <rel ="stylesheet" href="css/style.css">
        <style>
        body{{
            background-color: #f0f0f0;
            font-family: Arial, sans-serif;
            text-align: center;
            padding: 50px;
            background-image: url("{bg_src}");
            background-size: cover;
            background-attachment: fixed;
            background-position: center;
            }}
        h1{{
            color: red;
            text-shadow: 2px 2px 4px #000000;
            font-size: 36px;
            padding: 20px;
            border-radius: 10px;
            }}
        p{{font-size: 30px;
            color: white;}}
        </style>
        </head>
        <body>
        <h1>welcome to web scan!欢迎使用Web Scan!</h1>
        <p>this is a simple web scan tool that can help you to find the hidden path in your target website!这是一个简单的web扫描工具,可以帮助你找到目标网站中的隐藏路径！</p> 
        <br>
        <form action="/web_scan____(version_1.0)" method="get"><!-- form is use get =user input and send it to the url -->
        <input type="text" name="target" placeholder="Enter your target URL here!在这里输入你的目标URL! (e.g. http://example.com)" >
        <button type="submit">Scan!扫描！</button>
        </form>
        <hr>
        <p>Scan result:扫描结果:</p>
        <p>your content:\n{result_web}</p>
        <button type="reset" onclick="window.location.href='/web_scan____(version_1.0)'">Reset!重置！</button>
        <p> other code result:\n{feedback}</p>
        </body>


        </html>
            """ # this is the html that we will return to the user # here we use f string to combine the result_web variable with the html # and we will show the result_web variable in the html to show the result to the user
    
app.run(host="0.0.0.0", port=5000) # run the website on port 3000 and listen to all the ip address
# TO OPEN WEB  paste http://location_ip:5000/web_scan____(version 1.0) in the browser and then you can see the website and use it to scan the target website
# http://127.0.0.1:5000/web_scan____(version_1.0) # this is the url that you can use to access the website if you are running it on your local machine

 
                  
                
                 
