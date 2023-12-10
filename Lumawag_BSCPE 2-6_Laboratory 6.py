class LinkedList:
    def __init__(self, data=0):
        self.data = data
        self.next = None

def Merge(listone, listtwo):
    count = 0
    newlist = LinkedList()
    current = newlist

    while listone is not None and listtwo is not None:
        if -100 <= listone.data <= 100 and -100 <= listtwo.data <= 100:
            if listone.data < listtwo.data:
                current.next = listone
                listone = listone.next
            else:
                current.next = listtwo
                listtwo = listtwo.next

            current = current.next
            count += 1

        else:
            print("Invalid. Out of range. Enter values from -100 to 100 only.")
            return None

    current.next = listone or listtwo

    while current.next is not None:
        current = current.next
        count += 1

    if count > 50:
        print ("Invalid. Maximum number of nodes is reached.")

    return newlist.next

list1 = LinkedList(1)
list1.next = LinkedList(2)
list1.next.next = LinkedList(4)

list2 = LinkedList(1)
list2.next = LinkedList(3)
list2.next.next = LinkedList(4)

mergedlist = Merge(list1, list2)
while mergedlist is not None:
    print(mergedlist.data, end=" ")
    mergedlist = mergedlist.next

