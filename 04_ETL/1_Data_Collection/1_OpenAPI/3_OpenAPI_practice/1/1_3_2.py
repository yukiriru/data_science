import urllib3, inspect
import urllib3.util.ssl_ as ssl_mod
print("urllib3 from:", urllib3.__file__)
print("ssl_ file:", ssl_mod.__file__)
head = "".join(inspect.getsource(ssl_mod).splitlines(True)[:40])
print("get_response_text" in head or "requests.get" in head)
