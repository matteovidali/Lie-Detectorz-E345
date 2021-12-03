import time 
import os

filename = 'aaaa.csv'
file = open(filename, 'r', encoding='utf-8')
st_results = os.stat(filename)
st_size=st_results[6]
file.seek(st_size)

while 1:
    where = file.tell()
    line = file.readline()
    if not line:
        time.sleep(0.001)
        continue
    print(line)
