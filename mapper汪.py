import  sys
import  io

input_stream = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')
sum=0
for line in input_stream:
    sum+=1
    line=line.strip()
    words=line.split(",")
    id=words[0]
    fftdate=words[1]
    loaddate=words[9]
    detailffp=fftdate.split("/")
    detailload=loaddate.split("/")
    year1=detailffp[0]
    month1=detailffp[1]
    day1=detailffp[2]
    year2=detailload[0]
    month2=detailload[1]
    day2=detailload[2]
    month=int(((int(year2)-int(year1))*365+int(month2)*30-int(month1)*30+int(day2)-int(day1))/30)
    lasttoend=int(int(words[22])/30)
    flycount=words[10]
    segkmsum=words[16]
    avadiscount=words[28]
    print(id+","+str(month)+","+str(lasttoend)+","+str(flycount)+","+str(segkmsum)+","+avadiscount)