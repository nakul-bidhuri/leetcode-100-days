class ListNode:

    def __init__(self, val=0):
        self.val = val
        self.next = None


def create_linked_list(arr):

    if not arr:
        return None

    head = ListNode(arr[0])
    current = head

    for num in arr[1:]:
        current.next = ListNode(num)
        current = current.next

    return head


def print_list(head):

    while head:
        print(head.val, end=" ")
        head = head.next

    print()


def segregate_even_odd(head):

    if head is None:
        return None

    even_dummy = ListNode(0)
    odd_dummy = ListNode(0)

    even = even_dummy
    odd = odd_dummy

    current = head

    while current:

        if current.val % 2 == 0:
            even.next = current
            even = even.next
        else:
            odd.next = current
            odd = odd.next

        current = current.next

    even.next = odd_dummy.next
    odd.next = None

    return even_dummy.next


def main():

    head = create_linked_list([17, 15, 8, 9, 2, 4, 6])

    print("Original List:")
    print_list(head)

    head = segregate_even_odd(head)

    print("After Rearranging:")
    print_list(head)


if __name__ == "__main__":
    main()