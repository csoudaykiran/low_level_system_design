class HttpRequest:
    def __init__(self, method, url, headers, params, body, timeout, auth):
        self.method = method
        self.url = url
        self.headers = headers
        self.params = params
        self.body = body
        self.timeout = timeout
        self.auth = auth

    def send(self):
        print(f"Method: {self.method}")
        print(f"URL: {self.url}")
        print(f"Headers: {self.headers}")
        print(f"Body: {self.body}")
        print(f"Timeout: {self.timeout}")
        print(f"Auth: {self.auth}")


# ----- Builder -----
class HttpRequestBuilder:
    def __init__(self):
        self.method = None
        self.url = None
        self.headers = {}
        self.params = {}
        self.body = None
        self.timeout = None
        self.auth = None

    def set_method(self, method):
        self.method = method
        return self

    def set_url(self, url):
        self.url = url
        return self

    def set_headers(self, headers):
        self.headers = headers
        return self

    def set_params(self, params):
        self.params = params
        return self

    def set_body(self, body):
        self.body = body
        return self

    def set_timeout(self, timeout):
        # 🔍 Validation
        if not isinstance(timeout, (int, float)):
            raise TypeError("Timeout must be a number")
        self.timeout = timeout
        return self

    def set_auth(self, username, password):
        self.auth = (username, password)
        return self

    def build(self):
        # 🔍 Validation for required fields
        if not self.method or not self.url:
            raise ValueError("Both method and URL must be set.")
        return HttpRequest(
            self.method, self.url, self.headers,
            self.params, self.body, self.timeout, self.auth
        )


# ----- Client Code -----


req = HttpRequestBuilder().set_url("https://api.example.com").set_method("GET").build()
req.send()
# Output:
# Method: GET
# URL: https://api.example.com
# Headers: {}
# Body: None


builder = HttpRequestBuilder()
request = (builder
           .set_method("POST")
           .set_url("https://api.example.com/data")
           .set_headers({"Content-Type": "application/json"})
           .set_body('{"key": "value"}')
           .set_timeout(30)
           .set_auth("user", "pass")
           .build()
          )

request.send()
# Output:
# Method: POST
# URL: https://api.example.com/data
# Headers: {'Content-Type': 'application/json'}
# Body: {"key": "value"}
# Timeout: 30
# Auth: ('user', 'pass')
# Problemitic cases handled by Builder:
# Missing Required Fields
