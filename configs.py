from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "15316095"))
    API_HASH = getenv("API_HASH", "5657932594:AAG8GUYld4eqjAkrGee_UFlZ4oSGPl8SMYY")
    BOT_TOKEN = getenv("BOT_TOKEN", "5657932594:AAG8GUYld4eqjAkrGee_UFlZ4oSGPl8SMYY")
    FSUB = getenv("FSUB", "JN_MOVIE_REQUIST_GROUP")
    CHID = int(getenv("CHID", "-1001157009177"))
    SUDO = list(map(int, getenv("SUDO").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://jnanesh:jnanesh@cluster0.8pzxa6s.mongodb.net/?retryWrites=true&w=majority")
    
cfg = Config()
