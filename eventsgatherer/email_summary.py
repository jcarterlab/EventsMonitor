import logging
import resend
import time
import markdown
from datetime import datetime


# ----------------------------------------------------------------------
# LOGGING SETUP
# ----------------------------------------------------------------------

logger = logging.getLogger(__name__)


# ----------------------------------------------------------------------
# ORCHESTRATION FUNCTIONS
# ----------------------------------------------------------------------

def send_email(text, recipient, config):
    resend.api_key = config.RESEND_API_KEY

    html_summary = markdown.markdown(text)
    month = datetime.now().strftime("%B")

    response = resend.Emails.send({
    'from': config.FROM_EMAIL,
    'to': recipient,
    'subject': f'Events summary {month}',
    'html': f'<p>{html_summary}</p>'
    })