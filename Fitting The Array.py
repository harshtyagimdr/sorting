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
        a = list(map(int,input().strip().split()))
        b = list(map(int,input().strip().split()))
        a.sort()
        b.sort()
        c=0
        for i,j in zip(a,b):
            if i<=j:
                c+=1
        if c==n:
            print("YES")
        else:
            print("NO")