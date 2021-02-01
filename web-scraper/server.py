import os
import time
import json
import logging
from dotenv import load_dotenv
from http.server import BaseHTTPRequestHandler, HTTPServer

#########################################################################################################
# Global definitions

logging.basicConfig(format='%(levelname)s: %(asctime)s - %(name)s.%(funcName)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

try:
    load_dotenv()
    HOSTNAME = os.getenv('WEB_SCRAPER_HOSTNAME')
    PORT = os.getenv('WEB_SCRAPER_PORT')
except Exception as ex:
    logger.critical('Failed to retrieve environment variables. Please verify environment variable exists')
    logger.critical(str(ex))
    exit(1)

class Server(BaseHTTPRequestHandler):
    def set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_HEAD(self):
        self.set_headers()

    def do_GET(self):
        logger.info('Received GET request')
        self.set_headers()
        response = json.dumps({'hello': 'world', 'received': 'ok'})
        logger.info(f'Response: {response}')
        self.wfile.write(response.encode('utf-8'))

def run():
    server = HTTPServer((HOSTNAME, int(PORT)), Server)
    logger.info('Server is up and listening')
    logger.info(f'Port: {PORT}')

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass

    server.server_close()
    logger.info('Server stopped')

if __name__ == "__main__":
    run()