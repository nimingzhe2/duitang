#堆糖资源下载
import requests
import re
import json
import os
import jsonpath
import time
url = 'https://www.duitang.com/'
get_url = 'https://www.duitang.com/napi/blog/list/by_filter_id/?include_fields=top_comments%2Cis_root%2Csource_link%2Citem%2Cbuyable%2Croot_id%2Cstatus%2Clike_count%2Csender%2Calbum%2Creply_count&filter_id={}&start={}&_=1594364135869'
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}




def save_path(path, dex_name):  #保存路径
    rod = 'd://tu//' + dex_name + '//'
    path1 = rod + path.split('/',)[-1]
    print(path1)
    if not os.path.exists(rod):
        os.mkdir(rod)
    if not os.path.exists(path1):
        r = requests.get(path, headers=header).content
        with open(path1,'wb') as f:
            f.write(r)
            print(path + '下载成功')
    else:
        print(path + '已经存在了')



def MMM(MM):       #选项mm
    down_url = requests.get(MM, headers=header)
    down_url = down_url.text
    #print(down_url)

    choice_class = re.findall('''
<a class="column-\d row-\d" href="(.*?)">
(.*?)
</a>''', down_url)
    #print(choice_class)
    num = 1
    for dex in choice_class:
        dex_url = url + dex[0]
        dex_name = dex[1]   #文件夹名字
        print(num, dex_name, dex_url)
        # 创建一个字典接受各个完整的地址
        dictionaryt[num] = dex_url
        dictionaryname[num] = dex_name
        num += 1
    print(dictionaryname)
    number = int(input('please choice one label(just one label)：'))
    if number in dictionaryt.keys():
        name = dictionaryname.get(number)
        print('YOU CHOICE : [' + name + ']')
        print(' Now!  download all about it')
        canshu = dictionaryt.get(number)
        #print(canshu)
        canshu = canshu.split('=',)[-1]
        #print(canshu)

        for num1 in range(0, 24000, 24):
            u = get_url.format(canshu, num1)
            # print(u)
            # 访问所有页面的地址
            try:
                html = requests.get(u, headers=header)
                html = html.text
                html = json.loads(html)
                #print(html)
                path = jsonpath.jsonpath(html, '$..path')
                for i in path:
                    print(i)
                    save_path(i, name)
            except:
                print('未知错误，请联系作者改bug')
                break

    else:
        print('你输入的标号有误：程序提前结束')


def LFF(LF):      #选项lf
    down_url = requests.get(LF, headers=header)
    down_url = down_url.text
    #print(down_url)
    choice_class = re.findall('''
<a href="(.*?)">
(.{2,4})
</a>''', down_url)
    # print(choice_class)
    num = 1
    for dex in choice_class:
        dex_url = url + dex[0]
        dex_name = dex[1]  # 文件夹名字
        print(num, dex_name, dex_url)
        # 创建一个字典接受各个完整的地址
        dictionaryt[num] = dex_url
        dictionaryname[num] = dex_name
        num += 1
    print(dictionaryname)
    number = int(input('please choice one label(just one label)：'))
    if number in dictionaryt.keys():
        name = dictionaryname.get(number)
        print('YOU CHOICE : [' + name + ']')
        print(' Now!  download all about it')
        canshu = dictionaryt.get(number)
        # print(canshu)
        canshu = canshu.split('=', )[-1]
        # print(canshu)

        for num1 in range(0, 24000, 24):
            u = get_url.format(canshu, num1)
            # print(u)
            # 访问所有页面的地址
            try:
                html = requests.get(u, headers=header)
                html = html.text
                html = json.loads(html)
                # print(html)
                path = jsonpath.jsonpath(html, '$..path')
                for i in path:
                    print(i)
                    save_path(i, name)
            except:
                break
                print('未知错误,请联系作者改bug')
    else:
        print('你输入的标号有误；程序提前结束！')
def main():
    print('''感谢使用，堆糖提供超快捷的图文收集工具，一键收集分享兴趣，还有各种兴趣主题小组，可以轻易地找到日常生活中难以遇到的、
    跟自己兴趣相同的朋友。主题是收集发现喜爱的事物，以图片的方式来展示和浏览。堆糖的目标是链接人的兴趣和事物，重新组织信息流动的方式。
    ''')
    print('作者：坏狗i')
    time.sleep(2)
    print('''

          __            /^\ 
        .’  \          / :.\   
       /     \         | :: \ 
      /   /.  \       / ::: | 
    |    |::. \     / :::’/  
    |   / \::. |   / :::’/
    `--`   \’  `~~~ ’:’/`
             /         (    
            /   0 _ 0   \   
          \/     \_/     \/  
        -== ’.’   |   ’.’ ==-   
          /\    ’-^-’    /\    
            \   _   _   /             
           .-`-((\o/))-`-.   
      _   /     //^\ \      \   _    
    .'o'.(    , .:::. ,    ).'o'.  
    |o  o\ \    \:::::/    //o  o| 
    \    \ \   |:::::|   //    /   
      \    \ \__/:::::\__//    /   
       \ .:.\  `’:::’`  /.:. /      
        \’:: |_       _| ::’/  
         `---` `' '' ''` `---`

    ''')
    time.sleep(3)
    print('堆糖网的所有资源，每次只能选择一个类型的所有资源下载(下载完成后会自动结束)')
    time.sleep(2)
    # 访问堆糖官网获取分类数据
    dt_choice = requests.get(url, headers=header)
    dt_choice = dt_choice.text
    # print(dt_choice)

    classification = re.findall('<a href="(.*?)">(.*?)</a>', dt_choice)
    # print(classification)
    classification = classification[0:20]
    num = 1
    for fenlei in classification:
        # print(fenlei)
        # 分类地址拼接
        # 选择后的完整地址
        choice_url = url + fenlei[0]
        choice_name = fenlei[1]
        print(num, choice_name, choice_url)
        # 创建一个字典接受各个完整的地址
        dictionary[num] = choice_url
        num += 1
        # print(dictionary)

    print('it\'s all the resource types of the heap sugar. ')
    choice_label = int(input("please type one label:"))  # 输入选择
    # 从字典中遍历出来键 与输入值做对比
    if choice_label in dictionary.keys():
        if choice_label in list:
            LF = dictionary.get(choice_label)
            # print('你选择2')
            LFF(LF)


        else:
            MM = dictionary.get(choice_label)
            MMM(MM)


    else:
        print('你所输入的标号不存在！！！（进程结束，请重新打开程序）')
if __name__ == '__main__':
    dictionary = {}
    dictionaryt = {}
    dictionaryname = {}
    list = [7, 10, 11, 12, 16, 20]
    MM = {}
    LF = {}
    main()
    print('''
    へ　　　　　／|
　　/＼7　　∠＿/
　 /　│　　 ／　／
　│　Z ＿,＜　／　　 /`ヽ
　│　　　　　ヽ　　 /　　〉
　 Y　　　　　`　 /　　/
　ｲ●　､　●　　⊂⊃〈　　/
　()　 へ　　　　|　＼〈
　　>ｰ ､_　 ィ　 │ ／／
　 / へ　　 /　ﾉ＜| ＼＼
　 ヽ_ﾉ　　(_／　 │／／
　　7　　　　　　　|／
　　＞―r￣￣`ｰ―＿
    下载完成''')
    input("please input any key to exit!")



