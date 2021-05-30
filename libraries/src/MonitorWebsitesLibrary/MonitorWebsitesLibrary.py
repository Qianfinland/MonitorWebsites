import schedule
import time
import requests
import logging
from datetime import datetime,timezone
from bs4 import BeautifulSoup
from robot.api.deco import keyword
from robot.api import logger

class MonitorWebsitesLibrary(object):
    """
    MonitorWebsitesLibrary contains keywords/functions on monitoring websites
    and reporting their avaliability.
    """
    #requests.Response Object
    #https://www.w3schools.com/python/ref_requests_response.asp
    @keyword("Check Page Response")
    def check_page_response(self, website_url, page_id):
        page_response =  requests.get(website_url)
        server_response_time = page_response.elapsed.total_seconds()
        page_content = page_response.text
        soup = BeautifulSoup(page_content, 'html.parser')
        info_msg = 'Server response time "{}"; Webpage "{}" with status code "{}" '.format(server_response_time, website_url, page_response.status_code)
        if page_response.status_code == 200:
            check_existence_of_id = soup.find(id=page_id)
            if check_existence_of_id:
                debug_msg = 'Webpage "{}" works OK; the required page content "{}" exits, page content "{}" '.format(website_url, page_id, page_content)
                self.logger_example(debug_msg, info_msg)
            else:
                debug_msg = 'Webpage "{}" has issue; the required content "{}" does NOT exits, page content "{}" '.format(website_url, page_id, page_content)
                self.logger_example(debug_msg, info_msg)
        else:
            debug_msg = 'Webpage "{}" has issue; page content "{}" '.format(website_url, page_content)
            self.logger_example(debug_msg, info_msg)

    @keyword("Schedule Monitor Website")
    def schedule_monitor_website(self, website_url, page_id, interval_sec):
        now_utc = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
        print('Start to monitor webpage "{}" at "{}"'.format(website_url, now_utc))
        schedule.every(interval_sec).seconds.do(self.check_page_response, website_url, page_id)
        check_duration = 0
        #while True:
        while check_duration < 5*interval_sec:
            schedule.run_pending()
            time.sleep(1)
            check_duration += 1
            #print('check_duration {}'.format(check_duration))

    @keyword("Logger Example")
    def logger_example(self, debug_msg, info_msg):
        ##https://realpython.com/python-logging/
        ##https://docs.python.org/3/library/logging.html

        # Create a custom logger
        logger = logging.getLogger(__name__)

        # Create handlers
        c_handler = logging.StreamHandler()
        f_handler = logging.FileHandler('monitorfile.log')
        c_handler.setLevel(logging.DEBUG)
        f_handler.setLevel(logging.INFO)

        # Create formatters and add it to handlers
        c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
        f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        c_handler.setFormatter(c_format)
        f_handler.setFormatter(f_format)

        # Add handlers to the logger
        logger.addHandler(c_handler)
        logger.addHandler(f_handler)

        logger.debug(debug_msg)
        logger.info(info_msg)

monitor_ins = MonitorWebsitesLibrary()
#monitor_ins.schedule_monitor_website('https://stackoverflow.com/users/login', 'login-form', 3)
#monitor_ins.schedule_monitor_website('https://stackoverflow.com/teams', 'login-form', 5)
#monitor_ins.schedule_monitor_website('http://www.foobar.com/login', 'login-form', 10)
