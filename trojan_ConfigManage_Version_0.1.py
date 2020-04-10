#感謝 @harderandbetter 提供了解决win10下颜色转义序列失效的玄学方法
#參考文獻： https://blog.csdn.net/ytzlln/article/details/81945246
import os
import json
import shutil
first_page_state=0 #Begin:0 problem:-1 exit:-2
second_page_state=0 #Begin:0 problem:-1
os.system("") #在执行完system()之后，转移序列都会生效，原因未知 For print color
#import trojan-url #解碼URL

def print_first_page_choices():
    num=file_num()
    print('Trojan_win \033[1;31;40m [v0.1.0_alpha] \033[0m')
    print('-------- By:Matseoi --------')
    print('')
    print('\033[1;32;40m 1. \033[0m 添加配置文件')
    print('\033[1;32;40m 2. \033[0m 確認本次使用的服務器配置並運行')
    print('\033[1;32;40m 3. \033[0m 查看其它服務器內容')
    print('\033[1;32;40m 4. \033[0m 退出腳本')
    print('---------------------------------------')
    print('You have '+str(num)+' file(s) for config') #print the number of config files
    print('---------------------------------------')

def mkdir_data():
    folder=os.path.exists('data')
    if not folder:
        os.makedirs('data')
mkdir_data()

def file_num(): #get the number of files in path
    path=".\data"
    return len([lists for lists in os.listdir(path) if os.path.isfile(os.path.join(path, lists))])

num=file_num()

def enter_data(): #get data from user input. It will return json
    try:
        f_cl=open("examples\client.json-example")
        f_cl.close()
        os.rename("examples\client.json-example","examples\client.json")
    except FileNotFoundError:
        print ("File is not found.")
    with open("examples\client.json","r",encoding="utf-8") as f:      #把json文件，解碼爲py中的dict   data is  dict
        data = json.load(f)
    data["local_port"]=int(input("Input the local port here(please enter an int):\n")) 
    data["remote_addr"]=str(input("Input the address here:\n"))
    data["password"][0]=str(input("Input your password here:\n"))
    data["ssl"]["verify"]=bool(input('Do you want to verify your certificate? Enter\033[1;34;40m true \033[0mor\033[1;34;40m false \033[0mfalse\n'))
    return json.dumps(data, sort_keys=True, indent=4, separators=(',', ': ')) #convert data to json. Data is json now. 

def rename_file(rename_num):
    path='data/'
    while rename_num+1<num:
        os.rename(path+'config'+str(rename_num+1)+'.json', path+'config'+str(rename_num)+'.json')
        rename_num+=1

def print_designated_file_data(which_file): #get data for a file and PRINT the information
    str_file_name=str(which_file)
    name_for_file="data\config"+str_file_name+".json"
    with open(name_for_file,"r",encoding="utf-8") as f:      #把json文件，解碼爲py中的dict   data is  dict
        data = json.load(f)
    print('This is the information of the \033[1;31;40m'+str_file_name+'\033[0m file')
    print('Here is the local port for this file:')
    print(data["local_port"])
    print('Here is the address of your server:')
    print(data["remote_addr"])
    print('Here is the password of your config:')
    print(data["password"])

def print_each_data(): #Print the data of each file.
    each_file=1
    print('\033[1;31;40m This is the information of each file \033[0m')
    print('---------------------------------------')
    while each_file<=num:
        print_designated_file_data(each_file)
        each_file+=1
        print('---------------------------------------')

def get_state(how_much):
    print('請輸入數字 [1-'+str(how_much)+']')
    state=int(input())
    if state<1 or state>how_much:
        state=-1
    return state

def get_now_config(): #Print the config now.
    with open("config.json","r",encoding="utf-8") as f:      #把json文件，解碼爲py中的dict   data is  dict
        data = json.load(f)
    print('Here is the local port for this file: '+str(data["local_port"]))
    print('Here is the address of your server: '+str(data["remote_addr"]))
    print('Here is the password of your config: '+str(data["password"]))
    print('---------------------------------------')

def print_third_page_choices():
    print('\033[1;32;40m 1. \033[0m 選擇配置文件')
    print('\033[1;32;40m 2. \033[0m 刪除配置文件')

def delete_file():
    path="data/"
    print('你要删除哪个文件？')
    delete_num=int(input())
    file_have=len([lists for lists in os.listdir(path) if os.path.isfile(os.path.join(path, lists))])

    if delete_num<1 or delete_num>file_have:
        delete_num=-1
        print('你没有这个file')
    else:
        os.remove(path+'config'+str(delete_num)+'.json')
        rename_file(delete_num)

def select_config_file():
    os.remove('config.json')
    print('你要选哪个文件？')
    select=int(input())
    shutil.copy('data/config'+str(select)+'.json', './')
    os.rename('config'+str(select)+'.json','config.json')
    
while first_page_state==0:
    print_first_page_choices()#First page
    get_now_config()#First page
    first_page_state=get_state(4)#First page input
    
    while first_page_state!=-1 and first_page_state!=-2 and first_page_state!=0:
        if first_page_state==1:#添加配置文件
            num=file_num()
            new_file='data\config'+str(num+1)+'.json' 
            new_data=enter_data()
            with open(new_file, 'w') as ff:
                ff.write(new_data)
            first_page_state=0
        if first_page_state==2:#確認本次使用的服務器配置並運行
            os.system('trojan.exe')
            first_page_state=0
        if first_page_state==3:#查看其它服務器內容
            num=file_num()
            print_each_data()
            print_third_page_choices()
            second_page_state=get_state(2)
            if second_page_state==1:
                select_config_file()
            if second_page_state==2:
                delete_file()
            first_page_state=0
        if first_page_state==4:#退出腳本
            first_page_state=-2