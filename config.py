import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "15191874")
API_HASH = os.environ.get("API_HASH", "3037d39233c6fad9b80d83bb8a339a07")
#BOT_TOKEN = os.environ.get("BOT_TOKEN", "6938410415:AAGqtfxsJjDmsUCai3JWnQrMib53JVCkhoM") 
TOKEN_ONE = os.environ.get("TOKEN_ONE", "6938410415:AAGqtfxsJjDmsUCai3JWnQrMib53JVCkhoM")

CHANNEL = os.environ.get("CHANNEL", "irish_family") # username without '@'
BOT_USERNAME = os.environ.get("BOT_USERNAME","Mr_gojo_bot") # username without '@'
SUPPORT_GROUP = os.environ.get("SUPPORT_GROUP","geniflix_group") # username without '@'
UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL","irish_family") # username without '@'
OWNER_USERNAME = os.environ.get("OWNER_USERNAME","Narayan_k_purohit")
STRING = os.environ.get("STRING", "")

DB_NAME = os.environ.get("DB_NAME","1by1themes")     
DB_URL = os.environ.get("DB_URL","mongodb+srv://1by1themes:IOIfm2sf0ubXeSPu@cluster0.ftauibp.mongodb.net/?retryWrites=true&w=majority")

FLOOD = int(os.environ.get("FLOOD", "90"))
LAZY_PIC = os.environ.get("LAZY_PIC", "https://graph.org/file/d5356aa354a5c6bd2d593.jpg")
ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '5597521952').split()]
PORT = os.environ.get('PORT', '8080')
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001918482012"))
