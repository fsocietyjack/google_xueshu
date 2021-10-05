import requests
import pandas as pd
from tomorrow3 import threads

# 导入库
import pdfkit

proxies = {
    'http': "http://localhost:1081",
    'https': 'https://localhost:1081'
}

df = pd.read_csv('./xueshu/data2.csv')['data'].values.tolist()[4500:]


# print(df)


@threads(4)
def getData(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
    }
    try:
        print(url)
        res = requests.get(url=url, headers=headers, proxies=proxies, verify=False)
        suffix = url.split('/')[-1].replace(';', '')
        fileName = suffix if 'pdf' in suffix else suffix + '.pdf'
        content = None if b'html' in res.content else res.content
        if content:
            with open(f'./PDF/{fileName}', 'wb') as wf:
                wf.write(content)
                print('写入完成!')
        else:
            print(res.content)
    except BaseException:
        print('跳过...')


for d in df:
    getData(d)

'''将网页url生成pdf文件'''

# @threads(4)
# def url_to_pdf(url, to_file):
#     config = pdfkit.configuration()
#     # 生成pdf文件，to_file为文件路径
#     pdfkit.from_url(url, to_file, configuration=config)
#     print('完成')


# 这里传入我知乎专栏文章url，转换为pdf
# url_to_pdf(r'https://zhuanlan.zhihu.com/p/69869004', 'out_1.pdf')
# for d in df:
#     suffix = d.split('/')[-1].replace(';', '')
#     fileName = './PDF/' + suffix if 'pdf' in suffix else suffix + '.pdf'
#     url_to_pdf(d, fileName)
