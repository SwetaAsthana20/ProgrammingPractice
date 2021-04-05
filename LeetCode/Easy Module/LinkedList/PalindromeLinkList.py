from LinkedListPack.LinkedList import LinkList


def get_mid(slow_pointer, fast_pointer):
    while fast_pointer.next:
        slow_pointer = slow_pointer.next
        if not fast_pointer.next.next:
            break
        fast_pointer = fast_pointer.next.next
    return slow_pointer.next


def reverse(head):
    if head and head.next:
        first_pointer = head
        second_pointer = head.next

        first_pointer.next = None

        while second_pointer.next:
            third_pointer = second_pointer.next
            second_pointer.next = first_pointer
            first_pointer = second_pointer
            second_pointer = third_pointer

        second_pointer.next = first_pointer

        return second_pointer
    else:
        return head


def compare(first_pointer, second_pointer):
    while second_pointer:
        if first_pointer.value != second_pointer.value:
            return False
        first_pointer = first_pointer.next
        second_pointer = second_pointer.next
    return True


def isPalindrome(head: LinkList) -> bool:
    if not head or not head.next:
        return True
    slow_pointer = head
    fast_pointer = head.next

    slow_pointer = get_mid(slow_pointer, fast_pointer)

    slow_pointer = reverse(slow_pointer)

    return compare(head, slow_pointer)



ll = LinkList(20)
ll.next = LinkList(50)
ll.next.next = LinkList(10)
ll.next.next.next = LinkList(50)
ll.next.next.next.next = LinkList(0)


a = isPalindrome(ll)
print(a)