import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN","7076324437:AAGwyRLroXPBwpP_I--SqGjTApzPOKLUmBM")
    API_ID = int(os.environ.get("API_ID","15816419"))
    API_HASH = os.environ.get("API_HASH","626ed6dab78881858778d9663682962e")
    AUTH_USER = os.environ.get('AUTH_USERS', '2088265361').split(',')
    AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
    HOST = "https://drm-api-six.vercel.app"
    CREDIT = "[🅱🅴🅰🆂🆃 👑](https://t.me/chiru52)"
