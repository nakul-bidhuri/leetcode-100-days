class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None


def create_cycle_list(arr, pos):
    if not arr:
        return None

    nodes = [ListNode(num) for num in arr]

    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]

    if pos != -1:
        nodes[-1].next = nodes[pos]

    return nodes[0]


def has_cycle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False


def main():
    head = create_cycle_list([3, 2, 0, -4], 1)

    print("Has Cycle:", has_cycle(head))


if __name__ == "__main__":
    main()