import logging
from bs4 import BeautifulSoup


# ----------------------------------------------------------------------
# LOGGING SETUP
# ----------------------------------------------------------------------

logger = logging.getLogger(__name__)


# ----------------------------------------------------------------------
# HELPER FUNCTIONS
# ----------------------------------------------------------------------

def generic_parser(html, source):
    soup = BeautifulSoup(html, 'html.parser')

    elements = soup.find_all(source['parsing']['generic_scrape_selector'])

    if not elements:
        logger.warning(
            'No elements found website=%s',
            source['name']
        )
        return None
    
    text = ' '.join(
        element.get_text(separator=' ', strip=True)
        for element in elements
    )

    if not text:
        logger.warning(
            'No text found website=%s',
            source['name']
        )
        return None

    logger.info(
        'Extracted %s words', 
        len(text.split())
    )

    return text