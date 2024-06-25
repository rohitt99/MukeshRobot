class Config(object):
    LOGGER = True
    API_ID = 25830228
    API_HASH = "a23a5133bddbdab87df3df06ccf63a89"
    TOKEN = "6938324585:AAESsDWsNja6lf89EKd25CkMtoJR9D-VQpU"  
    OWNER_ID = 6722550550
    
    SUPPORT_CHAT = "@IMPERILMENT_SUPPORT" 
    START_IMG = "https://graph.org/file/fc3fff668765511b35f5b.jpg"
    EVENT_LOGS = (-1001977784654)
    MONGO_DB_URI= "mongodb+srv://rohit6205881743:rohit6205881743@cluster0.soqtewz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
   
    DATABASE_URL = "postgresql://xrlkskby:gobwyeqocauwmdrggqom@alpha.mkdb.sh:5432/rjfvbvce"  # A sql database url from elephantsql.com
    CASH_API_KEY = (
        "ODEUSYY8R0JUK2DU"
    )
    TIME_API_KEY = "AYJ7PU3K31JB"

    
    BL_CHATS = [] 
    DRAGONS = []
    DEV_USERS = []  
    DEMONS = [] 
    TIGERS = []  
    WOLVES = [] 

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
