
import logging
from requests_oauthlib import OAuth2Session
from http import server
import webbrowser
from drobfs.auth.endpoints import DropboxEndpoint
from urllib import parse

log = logging.getLogger(__name__)

class RedirectHandler(server.BaseHTTPRequestHandler):

    def __init__(self, request, address, server, auth):
        self.auth = auth 
        super().__init__(request, address, server)

    def log_message(self, format, *args):
        pass

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        log.debug("GET " + self.path)
        self.auth.auth_code = parse.parse_qs(self.path)['code'][0]
        
        self.wfile.write(b'<html><body> You can close window </body></html>')



class DropboxAuth:
    def __init__(self, config_file):
        self._client_id = '' 
        self._client_secret = ''
        self._redirect_url = 'http://127.0.0.1:5050'
        self.auth_code = 'test'
        

    def get_token(self):
        dropbox = OAuth2Session(self._client_id, redirect_uri=self._redirect_url)
        authorization_url, state = dropbox.authorization_url(DropboxEndpoint.AUTHORIZATION)

        log.debug("start browser")
        webbrowser.open(authorization_url)

        server.HTTPServer(('127.0.0.1', 5050), 
                lambda request, address, server: RedirectHandler(
                    request, address, server, self)).handle_request()

        token = dropbox.fetch_token(DropboxEndpoint.TOKEN, code=self.auth_code, client_secret=self._client_secret)
        