# -*- coding:utf-8 -*-
import sys
import io
input_stream = io.TextIOWrapper(sys.stdin.buffer,encoding='utf-8')

for line in input_stream:
    line=line.strip()
    words=line.split()
    for word in words:
        print(word+"\t"+str(1))

