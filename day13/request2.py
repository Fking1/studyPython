# 钩子  类似于回调函数

import requests
def get_key_info(response,*arg,**kwargs):
    # 回调函数
    print(response.headers['Content-Type'])

def main():
    requests.get('https://api.github.com',hooks=dict(response=get_key_info))


main()