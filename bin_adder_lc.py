class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        carry=0
        c=""
        if 1<=(len(a) and len(b)) and 10**4>=(len(a) and len(b)):
            diff=max(len(a),len(b))-min(len(a),len(b))
            if len(a)>len(b):
                b=diff*"0"+b
            elif len(b)>len(a):
                a=diff*"0"+a
            for i in range(len(a)-1,-1,-1):
                if carry==1:
                    if(a[i]=="1" and b[i]=="1"):
                        c="1"+c
                        if i==0:
                            c="1"+c
                    elif((a[i]=="1" and b[i]=="0") or (a[i]=="0" and b[i]=="1")):
                        c="0"+c
                        if i==0:
                            c="1"+c
                    else:
                        c="1"+c
                        carry=0
                else:
                    if(a[i]=="1" and b[i]=="1"):
                        c="0"+c
                        carry=1
                        if i==0:
                            c="1"+c
                    elif((a[i]=="1" and b[i]=="0") or (a[i]=="0" and b[i]=="1")):
                        c="1"+c
                    else:
                        c="0"+c
            return c
        else:
            return 0
