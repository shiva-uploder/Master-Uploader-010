import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN")
    API_ID = int(os.environ.get("API_ID"))
    API_HASH = os.environ.get("API_HASH")
    AUTH_USER = os.environ.get('AUTH_USERS', '7621154046').split(',')
    AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
    HOST = "https://drm-api-six.vercel.app"
    CREDIT = "[꧁ 𝐉𝐨𝐡𝐧 𝐖𝐢𝐜𝐤 ꧂](https://t.me/Dc5txt_bot)"
