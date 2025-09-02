# from mod1 import add
# from mod1 import add, sub, secret_message # 두가지 이상 import시 , 로 연결한다.
from mod1 import *

print(add(1, 2))
print(add(3,4))

print(sub(3,4))
print(sub(2,4))

print(f"secret_message: {secret_message}")