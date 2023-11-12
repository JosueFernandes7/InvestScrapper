import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    API_BASE_URL = os.environ.get("API_BASE_URL")
    XPATH_VALOR_ATUAL = "/html/body/main/div[2]/div/div[1]/div/div[1]/div/div[1]/strong"
    XPATH_RENDIMENTO_MENSAL = "/html/body/main/div[2]/div/div[1]/div/div[5]/div/div[1]/strong"
    XPATH_ALTERACAO_ATUAL = "/html/body/main/div[2]/div/div[1]/div/div[1]/div/div[2]/span/b"
    XPATH_TABLE = "/html/body/main/div[3]/div/div[1]/div[2]/div[7]/div/div[2]/table"


settings = Settings()