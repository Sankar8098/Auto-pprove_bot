from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "23990433"))
    API_HASH = getenv("API_HASH", "e6c4b6ee1933711bc4da9d7d17e1eb20")
    BOT_TOKEN = getenv("BOT_TOKEN", "5849628330:AAHjBZeXFAM9f2LkgH4OprLoyPycg9VQbhE")
    FSUB = getenv("FSUB", "SK_MoviesOffl")
    CHID = int(getenv("CHID", "-1001828551401"))
    SUDO = int(getenv("SUDO", "5821871362"))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://jnanesh:mongodb+srv://Test:1234@cluster0.2bzsp0q.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    
cfg = Config()
