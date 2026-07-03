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


def swap_pairs(head):

    dummy = ListNode(0)
    dummy.next = head

    prev = dummy

    while prev.next and prev.next.next:

        first = prev.next
        second = first.next

        first.next = second.next
        second.next = first
        prev.next = second

        prev = first

    return dummy.next


def main():

    head = create_linked_list([1, 2, 3, 4])

    print("Original Linked List:")
    print_list(head)

    head = swap_pairs(head)

    print("After Swapping:")
    print_list(head)


if __name__ == "__main__":
    main()