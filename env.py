from environs import Env
from loguru import logger

env = Env()
logger.info(f"Loading environment variables...")


ENVIRONMENT = env.str("ENVIRONMENT", "production")


ENVIRONMENT = env.str("ENVIRONMENT", "production")


DATABASE_URL = env.str("SETTING_SERVICE_DATABASE_URL")


SUPABASE_PROJECT_ID = env.str("SUPABASE_PROJECT_ID")
SUPABASE_URL = f"https://{SUPABASE_PROJECT_ID}.supabase.co"
JWKS_URL = f"{SUPABASE_URL}/auth/v1/.well-known/jwks.json"
ISSUER = f"{SUPABASE_URL}/auth/v1"
AUDIENCE = "authenticated"
