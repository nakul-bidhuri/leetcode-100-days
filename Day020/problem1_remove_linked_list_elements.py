class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def create_linked_list(arr):

    dummy = ListNode()
    current = dummy

    for num in arr:
        current.next = ListNode(num)
        current = current.next

    return dummy.next


def print_list(head):

    while head:
        print(head.val, end=" ")
        head = head.next

    print()


def remove_elements(head, val):

    dummy = ListNode(0)
    dummy.next = head

    current = dummy

    while current.next:

        if current.next.val == val:
            current.next = current.next.next
        else:
            current = current.next

    return dummy.next


def main():

    head = create_linked_list([1, 2, 6, 3, 4, 5, 6])

    print("Original List:")
    print_list(head)

    head = remove_elements(head, 6)

    print("After Removing 6:")
    print_list(head)


if __name__ == "__main__":
    main()