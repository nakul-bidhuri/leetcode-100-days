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


def middle_node(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow


def main():
    head = create_linked_list([1, 2, 3, 4, 5, 6])

    middle = middle_node(head)

    print("Middle Node:", middle.val)


if __name__ == "__main__":
    main()