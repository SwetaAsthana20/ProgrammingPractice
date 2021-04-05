from LinkedListPack.LinkedList import LinkList


def mergeTwoLists(l1: LinkList, l2: LinkList) -> LinkList:
    if not l1:
        return l2

    if not l2:
        return l1

    if l1.value <= l2.value:
        l1.next = mergeTwoLists(l1.next, l2)
        return l1

    else:
        l2.next = mergeTwoLists(l1, l2.next)
        return l2



ll = LinkList(20)
ll.next = LinkList(50)
ll.next.next = LinkList(60)
ll.next.next.next = LinkList(70)
ll.next.next.next.next = LinkList(90)

ll1 = LinkList(30)
ll1.next = LinkList(40)
ll1.next.next = LinkList(55)
ll1.next.next.next = LinkList(80)
ll1.next.next.next.next = LinkList(100)


a = mergeTwoLists(ll, ll1)
ll.printLinkedList(a)