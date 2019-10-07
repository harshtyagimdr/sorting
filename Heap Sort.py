#Initial Template for Python 3
import atexit
import io
import sys
# Contributed by : Harsh tyagi
_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER
@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        buildHeap(arr,n)
        print(*arr)

}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
def heapify(arr, n, i):
    '''
    :param arr: original array
    :param n: size of original array
    :param i: subtree rooted at ith index
    :return: 
    '''
    # code here
    largest = i   
    l = 2 * i + 1      
    r = 2 * i + 2
    if l < n and arr[i] < arr[l]: 
        largest = l 
  
   
    if r < n and arr[largest] < arr[r]: 
        largest = r 
        
    if largest != i: 
        arr[i],arr[largest] = arr[largest],arr[i]  # swap 
  
        
        heapify(arr, n, largest)
def buildHeap(arr,n):
    '''
    :param arr: given array
    :param n: size of array
    :return: None
    '''
    # code 
    for i in range(n, -1, -1): 
        heapify(arr, n, i)
    for i in range(n-1, 0, -1): 
        arr[i], arr[0] = arr[0], arr[i]   # swap 
        heapify(arr, i, 0)