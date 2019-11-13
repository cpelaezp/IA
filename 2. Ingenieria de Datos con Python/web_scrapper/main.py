import argparse
from common import config

import logging

logging.basicConfig(level=loggin.INFO)
logger = logging.getLogger(__name__)

def run():
    pass

def _news_screpper(new_site_uid):
    host = config()['news_sites'][new_site_uid]['url']

    logging.info('Beginning scraper for {}'.format(host))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    new_sites_choices = list(config()['news_sites'].keys()) 
    parser.add_argumentd('new_site',
                        help='the new site that you want to scrapper',
                        type=str,
                        choices=new_sites_choices 
                        )

    args = parser.parse_args()
    _news_screpper(args.new_site)

    run()