# ----- Naive Implementation -----
class HttpRequest:
    def __init__(self, method, url, headers=None, params=None, body=None, timeout=None, auth=None):
        self.method = method
        self.url = url
        self.headers = headers or {}
        self.params = params or {}
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

# ----- Client Code -----
request = HttpRequest(
    method="POST",
    url="https://api.example.com/data",
    headers={"Content-Type": "application/json"},
    body='{"key": "value"}',
    timeout=30,
    auth=("user", "pass")
)
request.send()
# Output:
# Method: POST
# URL: https://api.example.com/data
# Headers: {'Content-Type': 'application/json'}
# Body: {"key": "value"}
# Timeout: 30
# Auth: ('user', 'pass')

# problemitic cases:

req = HttpRequest("https://api.example.com/data", "GET")
req.send()

# Output:
# Method: https://api.example.com/data
# URL: GET
# Headers: {}
# Body: None
# Method and URL are swapped, leading to confusion and potential errors.


# Wrong Data Type
req = HttpRequest(
    method="GET",
    url="https://api.example.com/data",
    headers="Not a dict"  # Incorrect data type
)
req.send()

# Output:
# Method: GET
# URL: https://api.example.com/data
# Headers: Not a dict
# Body: None
# Headers should be a dictionary, but a string is provided, leading to runtime errors when accessing headers.


# Too Many Optional Arguments
req = HttpRequest("POST", "https://api.example.com/upload", None, None, {"file": "abc"}, 30, ("user", "pass"))
req.send()

# Output:
# Method: POST
# URL: https://api.example.com/upload
# Headers: None
# Body: {'file': 'abc'}
# Timeout: 30
# Auth: ('user', 'pass')
# The large number of optional arguments makes it hard to remember the order and purpose of each parameter, leading to potential mistakes.
# Works… but good luck remembering what all those None, None, {...}, 30 mean.