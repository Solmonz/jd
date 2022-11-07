

# -*- coding: utf8 -*-
import requests
import simplejson as json
import telegram
from urllib import parse

user = ""
passwd = ""
end = ""
bot_api = ""
chat_id = ""
# email登录方式
url = "https://api.kit9.cn/api/xiaomi_sports/api_email_fixed.php?email="+user+"&password="+passwd+"&step="+end
from fake_useragent import UserAgent
ua = UserAgent()
headers = {'User-Agent': ua.random}
req = requests.get(url=url,headers=headers).json()
code = req["code"]
if code == 200:
    print("提交成功",)
elif code == 207:
    print("提交失败")
    print("登录失败，可能是账号或密码错误")
elif code == -1:
    print("60秒内只允许提交1次")
# TG推送
def post(bot_api, chat_id, text):
    print('开始推送')
    headers = {
       'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.76 Mobile Safari/537.36'}
    text = parse.quote(text)
    # 修改为自己的bot api token
    post_url = 'https://api.telegram.org/bot{}/sendMessage' \
               '?parse_mode=MarkdownV2&chat_id={}&text={}'.format(bot_api, chat_id, text)
    try:
        requests.get(post_url, headers=headers)
        print('推送成功')
    except Exception:
        print("推送失败")
        time.sleep(3)
      # 避免推送死循环
    except Exception:
        pass
post(bot_api, chat_id, "提交成功！:" + end)