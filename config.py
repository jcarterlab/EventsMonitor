from dotenv import load_dotenv
from pathlib import Path
import os
import json

load_dotenv()


SELENIUM = {
    "headless": True,
    "window_size": "1920,1080",
    "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
}



ENVIRONMENT = os.getenv('ENVIRONMENT', 'development') # development or production




# --------------------------------------------------
# Email parameters
# --------------------------------------------------

# API keys
RESEND_API_KEY = os.getenv('RESEND_API_KEY')

# Email settings
FROM_EMAIL = os.getenv('FROM_EMAIL') or 'onboarding@resend.dev'
EMAIL_RETRY_ATTEMPTS = int(os.getenv('EMAIL_RETRY_ATTEMPTS', 3)) # retries
EMAIL_WAIT_TIME = int(os.getenv('EMAIL_WAIT_TIME', 2)) # second
TO_EMAIL = os.getenv('TO_EMAIL')