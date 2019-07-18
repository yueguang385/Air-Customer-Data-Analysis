import sys
import io
#input_stream = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')
sum=0
current_word=None
for line in sys.stdin:
    line = line.strip()
    tmp = line.split('\t')
    key = tmp[0]
    value = 1
    if current_word == None:
        current_word = key
    if current_word != key:
        print(current_word+"\t"+str(sum))
        sum = 0
        current_word = key
    sum += 1
print(current_word+"\t"+str(sum))
