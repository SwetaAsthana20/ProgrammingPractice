class LinkList(object):

    def __init__(self, root):
        self.value = root
        self.next = None

    def deleteNodeInLL(self, linked_list, node):
        if linked_list:
            if linked_list.next.value == node:
                linked_list.next = linked_list.next.next
        return linked_list

    def printLinkedList(self, val):
        if val:
            if val.next:
                print(val.value)
                self.printLinkedList(val.next)
            else:
                print(val.value)
        return

    def reverseLinkedList(self, head):
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

