import logging
import config

from eventsmonitor.scrape_content import scrape_content
from eventsmonitor.email_summary import send_email


# ----------------------------------------------------------------------
# LOGGING SETUP
# ----------------------------------------------------------------------

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | %(name)s | %(message)s'
)

logger = logging.getLogger(__name__)


# ----------------------------------------------------------------------
# MAIN PIPELINE
# ----------------------------------------------------------------------

def run_pipeline(config):
    text = scrape_content(config)
    send_email(text, config.TO_EMAIL, config)



# ----------------------------------------------------------------------
# ENTRY POINT
# ----------------------------------------------------------------------

if __name__ == '__main__':
    run_pipeline(config)