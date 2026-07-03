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


def merge_two_lists(list1, list2):

    dummy = ListNode()
    current = dummy

    while list1 and list2:

        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next

        current = current.next

    if list1:
        current.next = list1
    else:
        current.next = list2

    return dummy.next


def main():

    list1 = create_linked_list([1, 2, 4])
    list2 = create_linked_list([1, 3, 4])

    merged = merge_two_lists(list1, list2)

    print("Merged Linked List:")
    print_list(merged)


if __name__ == "__main__":
    main()