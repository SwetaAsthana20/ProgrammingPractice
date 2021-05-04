class LinkList(object):

    def __init__(self, root=0):
        self.value = root
        self.next = None

    def printLinkedList(self, val):
        if val:
            if val.next:
                print(val.value)
                self.printLinkedList(val.next)
            else:
                print(val.value)
        return

def getIntersectionNode(headA: LinkList, headB: LinkList) -> LinkList:
    if headA and headB:
        node_A = headA
        node_B = headB
        len_A = 1
        len_B = 1
        while(node_A.next):
            len_A +=1
            node_A = node_A.next
        while (node_B.next):
            len_B += 1
            node_B = node_B.next
        maxi = headA if len_A>=len_B else headB
        mini = headA if len_A<len_B else headB
        diff = abs(len_A - len_B)
        for i in range(diff):
            maxi = maxi.next
        while(maxi and mini):
            if maxi == mini:
                return maxi
            maxi = maxi.next
            mini = mini.next

    return None

def getIntersection(headA: LinkList, headB: LinkList) -> LinkList:
    pA = headA
    pB = headB
    while pA != pB:
        pA = headB if pA is None else pA.next
        pB = headA if pB is None else pB.next

    return pA

ll = LinkList(1)
ll.next = LinkList(2)
ll.next.next = LinkList(3)
ll.next.next.next = LinkList(4)
ll.next.next.next.next = LinkList(5)
#ll.next.next.next.next.next = LinkList(6)

ll2 = LinkList(9)
ll2.next = LinkList(2)
ll2.next.next = LinkList(3)
ll2.next.next.next = LinkList(4)
ll2.next.next.next.next = LinkList(5)
ll2.next.next.next.next.next = LinkList(5)

ll1 = LinkList(7)
ll1.next = LinkList(6)
ll1.next.next = ll.next
ll1.next.next.next = ll.next.next
ll1.next.next.next.next = ll.next.next.next
ll1.next.next.next.next.next = ll.next.next.next.next

a = getIntersectionNode(ll, ll2)
c = getIntersection(ll, ll2)
ll.printLinkedList(a)