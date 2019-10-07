def sortDoubly(head):
    l=[]
    temp=head
    while(temp!=None):
        l.append(temp.data)
        temp=temp.next
    l.sort()
    temp=head
    i=0
    while(temp!=None):
        temp.data=l[i]
        temp=temp.next
        i+=1
    return head