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


def is_palindrome(head):
    values = []

    current = head
    while current:
        values.append(current.val)
        current = current.next

    return values == values[::-1]


def main():
    head = create_linked_list([1, 2, 2, 1])

    print("Is Palindrome:", is_palindrome(head))


if __name__ == "__main__":
    main()