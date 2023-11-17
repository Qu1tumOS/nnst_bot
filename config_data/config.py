from dataclasses import dataclass
from environs import Env


@dataclass
class TgBot:
    token: str            # Токен для доступа к телеграм-боту


@dataclass
class Config:
    tg_bot: TgBot


def load_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env(path)
    return Config(tg_bot=TgBot(token=env('BOT_TOKEN')))

def payment_url():
    env = Env()
    env.read_env()
    return env('PAY_URL')

def admins_id():
    env = Env()
    env.read_env()
    return env('ADMIN_ID')

class DB:
    env = Env()
    env.read_env()

    HOST = env('DB_HOST')
    PORT = env('DB_PORT')
    USER = env('DB_USER')
    PASS = env('DB_PASS')
    NAME = env('DB_NAME')

print(DB.HOST, DB.NAME, DB.PASS, DB.PORT, DB.USER)