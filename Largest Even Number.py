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
        n =input()
        s=''
        n=sorted(n,reverse=True)
        if int(n[-1])%2==0:
            s=''.join(n)
            print(s)
        else:
            c=0
            
            l=[int(i) for i in n]
            for i in range(len(l)-1,-1,-1):
                if l[i]%2==0:
                    no=l[i]
                    l.remove(no)
                    
                    c=1
                    break
            if c>0:
                l=map(str,l)
                s="".join(l)
                s+=str(no)
                print(s)
            else:
                l=map(str,l)
                s=''.join(l)
                print(s)
            