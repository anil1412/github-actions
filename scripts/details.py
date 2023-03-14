import json
import sys

str = ' '.join(sys.argv)
str_i = str.split("###")
customer_name = str_i[1].split("---")[2].strip()
initial_admin = str_i[2].split("---")[2].strip()
print(f"{customer_name}|{initial_admin}")
