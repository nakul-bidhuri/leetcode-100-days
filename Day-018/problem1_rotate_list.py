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
    values = []

    while head:
        values.append(head.val)
        head = head.next

    print(values)


def rotate_right(head, k):
    if head is None or head.next is None or k == 0:
        return head

    length = 1
    tail = head

    while tail.next:
        tail = tail.next
        length += 1

    k = k % length

    if k == 0:
        return head

    tail.next = head

    steps_to_new_tail = length - k

    new_tail = head

    for _ in range(steps_to_new_tail - 1):
        new_tail = new_tail.next

    new_head = new_tail.next

    new_tail.next = None

    return new_head


def main():
    head = create_linked_list([1, 2, 3, 4, 5])
    k = 2

    head = rotate_right(head, k)

    print("Rotated List:")
    print_list(head)


if __name__ == "__main__":
    main()