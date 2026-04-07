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


DESCRIPTION = f"""
# Chào mừng đến với {SERVICE_NAME}

Bạn có thể đăng nhập qua Google bằng đường dẫn dưới đây:
* [Đăng nhập với Google](https://{SUPABASE_PROJECT_ID}.supabase.co/auth/v1/authorize?provider=google)

Xem redoc:
* [Xem redoc](/redoc)

Xem docs:
* [Xem docs](/docs)

Xem voyager:
* [Xem voyager](/voyager)

### Thông tin hệ thống:
* **SERVICE_NAME:** {SERVICE_NAME}
* **ENVIRONMENT:** {ENVIRONMENT}
* **RELOAD:** {RELOAD}
""".strip()
