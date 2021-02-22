import http.server
import webbrowser
import urlib.request

from urllib.request import urlopen, HTTPError
from webbrowser import open_new



REDIRECT_URL = 'http://localhost:8080/'
AUTH_URI = ""
PORT=8080

class HTTPServerHandler(http.server.BaseHTTPRequestHandler):

    """
    HTTP Server callbacks to handle Facebook OAuth redirects
    """
    def __init__(self, request, address, server, a_id, a_secret):
        self.app_id = a_id
        self.app_secret = a_secret
        super().__init__(request, address, server)


    def get_access_token_from_url(self, url):
        token = str(urlib.request.urlopen(url).read(), 'utf-8')
        return token.split('=')[1].split('&')[0]

    def do_GET(self):
        GRAPH_API_AUTH_URI = ('https://graph.facebook.com/v2.2/oauth/' 
            + 'access_token?client_id=' + self.app_id + '&redirect_uri=' 
            + REDIRECT_URL + '&client_secret=' + self.app_secret + '&code=')

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        if 'code' in self.path:
            self.auth_code = self.path.split('=')[1]
            self.wfile.write(bytes('<html><h1>You may now close this window.'
                              + '</h1></html>', 'utf-8'))
            self.server.access_token = get_access_token_from_url(
                    GRAPH_API_AUTH_URI + self.auth_code)

    # Disable logging from the HTTP Server
    def log_message(self, format, *args):
        return

class AccessToken:
    def __init__(self, id, secret):
        self._id = id
        self._secret = secret
    
    def get_token():
        server = HTTPServer(('localhost', PORT), 
                lambda request, address, server: HTTPServerHandler(
                    request, address, server, self._id, self._secret))
        webrowser.open_new(AUTH_URI)
        server.handle_request()
        return server.access_token

