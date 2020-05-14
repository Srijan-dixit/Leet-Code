def main():
    n=4
    if n==1:
        return "1"
    elif n==2:
        return "11"
    out="11 "
    temp=""
    count=1
    l=len(out)
    for i in range(n-2):
        for j in range(1,l):
            if out[j]==out[j-1]:
                count+=1
            else:
                temp+=str(count)
                temp+=out[j-1]
                count=1
        l=len(temp)+1
        out=temp
        out+=" "
        s=temp
        temp=""
    print(s)
main()
