from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "15316095"))
    API_HASH = getenv("API_HASH", "6a293d116082b81260ac83d21f595ffa")
    BOT_TOKEN = getenv("BOT_TOKEN", "5657932594:AAG8GUYld4eqjAkrGee_UFlZ4oSGPl8SMYY")
    FSUB = getenv("FSUB", "jn_kannada")
    CHID = int(getenv("CHID", "-1001848686433"))
    SUDO = int(getenv("SUDO", "1384893863"))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://jnanesh:jnanesh@cluster0.8pzxa6s.mongodb.net/?retryWrites=true&w=majority")
    
cfg = Config()
