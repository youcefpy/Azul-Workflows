from dotenv import load_dotenv
import os

load_dotenv()


class Settings:
    DATABASE_URL    = os.getenv("DATABASE_URL")
    SMTP_SERVER     = os.getenv("SMTP_SERVER")
    SMTP_PORT       = os.getenv("SMTP_PORT")
    SMTP_USERNAME   = os.getenv("SMTP_USERNAME")
    SMTP_PASSWORD   = os.getenv("SMTP_PASSWORD")
    ADMIN_EMAIL     = os.getenv("ADMIN_EMAIL")
    ADMIN_API_KEY   = os.getenv("ADMIN_API_KEY")


settings = Settings()