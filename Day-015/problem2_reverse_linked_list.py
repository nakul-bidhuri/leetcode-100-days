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


def reverse_list(head):

    previous = None
    current = head

    while current:

        next_node = current.next

        current.next = previous

        previous = current

        current = next_node

    return previous


def main():

    head = create_linked_list([1, 2, 3, 4, 5])

    print("Original Linked List:")
    print_list(head)

    head = reverse_list(head)

    print("Reversed Linked List:")
    print_list(head)


if __name__ == "__main__":
    main()