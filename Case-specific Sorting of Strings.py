import atexit
import io
import sys
#Contributed by :HARSH TYAGI
_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER
@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())
if __name__ == '__main__':
   
    for _ in range(int(input())) :
        n = int(input())
        s=input()
        a=[False]*n
        u=[]
        l=[]
        for i in range(n):
            if s[i].isupper():
                u.append(s[i])
                a[i]=True
            else:
                l.append(s[i])
        u.sort()
        l.sort()
        ind1,ind2=0,0
        for i in range(n):
            if a[i] is True:
                a[i]=u[ind1]
                ind1+=1
            else:
                a[i]=l[ind2]
                ind2+=1
        str1=''
        print(str1.join(a))
                