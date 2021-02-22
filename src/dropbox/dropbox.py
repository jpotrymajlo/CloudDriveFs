
from requests_oauthlib import OAuth2Session
from http import server
import webbrowser
import logging
from dropbox.endpoints import DropboxEndpoint
from urllib import parse

logger = logging.getLogger(__name__)

class RedirectHandler(server.BaseHTTPRequestHandler):

    def __init__(self, request, address, server, auth_code):
        self.auth_code = auth_code
        super().__init__(request, address, server)

    def log_message(self, format, *args):
        pass

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        print("GET " + self.path)
        self.auth_code = parse.parse_qs(self.path)['code'][0]
        print('Code ' + self.auth_code)
        
        self.wfile.write(b'<html><body> You can close window </body></html>')



class DropboxAuth:
    def __init__(self, config_file):
        self._client_id = 'jwj2fc1q3pj3v2a'
        self._client_secret = 'fit6twbr5v179d9'
        self._redirect_url = 'http://127.0.0.1:5050'
        self._auth_code = 'test'
        

    def get_token(self):
        dropbox = OAuth2Session(self._client_id, redirect_uri=self._redirect_url)
        authorization_url, state = dropbox.authorization_url(DropboxEndpoint.AUTHORIZATION)

        print("start browser")
        webbrowser.open(authorization_url)

        print("start server")
        server.HTTPServer(('127.0.0.1', 5050), 
                lambda request, address, server: RedirectHandler(
                    request, address, server, self._auth_code)).handle_request()

        print("fetch token " + self._auth_code)
        dropbox.fetch_token(DropboxEndpoint.TOKEN, code=self._auth_code, client_id=self._client_id, client_secret=self._client_secret)
        