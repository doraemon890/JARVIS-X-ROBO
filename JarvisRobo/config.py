
class Config(object):
    LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = "" # integer value, dont use ""
    API_HASH = ""
    TOKEN = ""  # This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    OWNER_ID = "7157587567" # If you dont know, run the bot and do /id in your private chat with it, also an integer
    
    SUPPORT_CHAT = "Chatting_2024"  # Your own group for support, do not add the @
    START_IMG = ""
    EVENT_LOGS = ()  # Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit
    MONGO_DB_URI= "mongodb+srv://MANAGERDB:RAJNISHAYUSHI@managerdb.lfnlzdk.mongodb.net/?retryWrites=true&w=majority&appName=managerdb"
    # RECOMMENDED
    DATABASE_URL = "postgres://avnadmin:AVNS_LMygE8KX46Cf9jG-Rrl@jarvis-manager-jarvisxd648-3563.a.aivencloud.com:20557/defaultdb?sslmode=require"  # A sql database url from elephantsql.com
    CASH_API_KEY = (
        " X652FNVGJ0ZXABM0"  # Get your API key from https://www.alphavantage.co/support/#api-key
    )
    TIME_API_KEY = "VR8S3BA8ESW3"
    
    # Get your API key from https://timezonedb.com/api


    # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = []  # User id of sudo users
    DEV_USERS = []  # User id of dev users
    DEMONS = []  # User id of support users
    TIGERS = []  # User id of tiger users
    WOLVES = []  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8
    

class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
