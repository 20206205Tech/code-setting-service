from environs import Env
from loguru import logger

env = Env()
logger.info("Loading environment variables...")


DATABASE_URL = env.str("SETTING_SERVICE_DATABASE_URL")
SERVICE_NAME = "setting-service"
PORT = 30002


ENVIRONMENT = env.str("ENVIRONMENT", "production")
RELOAD = True if ENVIRONMENT == "development" else False


SUPABASE_PROJECT_ID = env.str("SUPABASE_PROJECT_ID")
SUPABASE_URL = f"https://{SUPABASE_PROJECT_ID}.supabase.co"
JWKS_URL = f"{SUPABASE_URL}/auth/v1/.well-known/jwks.json"
ISSUER = f"{SUPABASE_URL}/auth/v1"
AUDIENCE = "authenticated"
