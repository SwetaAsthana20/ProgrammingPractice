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


def get_sum_and_carry(num):
    if num >9:
        return num%10, num//10
    return num, 0

def addTwoNumbers(l1, l2):
    if l1 and l2:
        carry = 0
        node1 = LinkList()
        sum, carry = get_sum_and_carry(l1.value + l2.value + carry)
        node1.value = sum
        l1 = l1.next
        l2 = l2.next
        head = node1
        while(l1 or l2 or carry):
            node2 = LinkList()
            l1_value = l1.value if l1 else 0
            l2_value = l2.value if l2 else 0
            sum, carry = get_sum_and_carry(l1_value + l2_value + carry)
            l1 = l1.next if l1 else 0
            l2 = l2.next if l2 else 0
            node2.value = sum
            node1.next = node2
            node1 = node2

        return head
    else:
        return l1 or l2


ll = LinkList(9)
ll.next = LinkList(9)
ll.next.next = LinkList(9)
ll.next.next.next = LinkList(9)
ll.next.next.next.next = LinkList(9)
ll.next.next.next.next.next = LinkList(9)
ll.next.next.next.next.next.next = LinkList(9)

ll2 = LinkList(9)
ll2.next = LinkList(9)
ll2.next.next = LinkList(9)
ll2.next.next.next = LinkList(9)

a = addTwoNumbers(ll, ll2)
ll.printLinkedList(a)


