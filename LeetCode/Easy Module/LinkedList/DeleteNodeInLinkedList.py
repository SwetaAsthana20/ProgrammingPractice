from LinkedListPack.LinkedList import LinkList


def deleteNodeInLL(linked_list, node):
    if linked_list:
        if linked_list.next.value == node:
            linked_list.next = linked_list.next.next
    return linked_list


ll = LinkList(20)
ll.next = LinkList(50)
ll.next.next = LinkList(10)
ll.next.next.next = LinkList(70)

a = deleteNodeInLL(ll, 50)
ll.printLinkedList(a)
