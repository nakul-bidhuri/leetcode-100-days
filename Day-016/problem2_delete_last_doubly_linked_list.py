class Node:

    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


def create_dll(arr):

    if not arr:
        return None

    head = Node(arr[0])
    current = head

    for num in arr[1:]:

        new_node = Node(num)

        current.next = new_node
        new_node.prev = current

        current = new_node

    return head


def print_dll(head):

    while head:
        print(head.data, end=" ")
        head = head.next

    print()


def delete_last_node(head):

    if head is None:
        return None

    if head.next is None:
        return None

    current = head

    while current.next:
        current = current.next

    current.prev.next = None

    return head


def main():

    head = create_dll([1, 2, 3, 4])

    print("Original DLL:")
    print_dll(head)

    head = delete_last_node(head)

    print("After Deleting Last Node:")
    print_dll(head)


if __name__ == "__main__":
    main()