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
    result = []

    while head:
        result.append(head.val)
        head = head.next

    print(result)


def delete_duplicates(head):
    current = head

    while current and current.next:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next

    return head


def main():
    head = create_linked_list([1, 1, 2, 3, 3])

    print("Original List:")
    print_list(head)

    head = delete_duplicates(head)

    print("After Removing Duplicates:")
    print_list(head)


if __name__ == "__main__":
    main()