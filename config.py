import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    def __getattr__(self, name: str):
        key = name.upper()

        if key in os.environ:
            return os.getenv(key)

        possible_keywords = ["TOKEN", "KEY", "SECRET", "API"]
        for env_name, value in os.environ.items():
            if any(k in env_name for k in possible_keywords):
                if key in env_name or env_name in key:
                    return value

        return None


cfg = Config()
