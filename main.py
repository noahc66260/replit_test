import os
import add
import math_operations
print('Hello World!')
print(dir(add))
#print(math_operations.multsub(3,4,5))
breakpoint()
print(math_operations.mult.mult(10,20))
print(math_operations.subtract.sub(80,40))
from replit import db
my_secret = os.environ['password']
print(my_secret)

import rand_string.rand_string as rand
print(rand.RandString("ascii", 10))
print(add.add(1,2))

db["foo"] = "bar"
print(db["foo"])

print(db.keys())