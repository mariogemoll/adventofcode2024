from common import checksum


class Node:
    def __init__(self, id, length):
        self.id = id
        self.length = length
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.id)


def load_input(filename):
    with open(filename, 'r') as f:
        line = f.read().strip()
        head = None
        tail = None
        id = 0
        for i in range(len(line)):
            length = int(line[i])
            if i % 2 == 0:
                node_id = id
                id += 1
            else:
                node_id = None
            if head is None:
                head = Node(node_id, length)
                tail = head
            else:
                tail.next = Node(node_id, length)
                tail.next.prev = tail
                tail = tail.next
        return head, tail


def traverse(head):
    node = head
    while node is not None:
        print(node.id, node.length)
        node = node.next


def fs_str(head):
    node = head
    output = []
    while node is not None:
        for _ in range(node.length):
            to_display = node.id if node.id is not None else '.'
            output.append(to_display)
        node = node.next
    return output


def main():
    head, tail = load_input('input')
    right = tail
    outer_iteration = 0
    moved = set()
    while right != head:
        if right.id is None or right.id in moved:
            right = right.prev
            continue
        outer_iteration += 1

        found = False
        cursor = head
        while not found and cursor is not right:
            if cursor.id is not None:
                cursor = cursor.next
                continue
            if cursor.length == right.length:
                found = True
                moved.add(right.id)
                cursor.id = right.id
                right.id = None
                cursor = cursor.next
            elif cursor.length > right.length:
                found = True
                moved.add(right.id)
                data_node = Node(right.id, right.length)
                space_node = Node(None, cursor.length - right.length)
                data_node.prev = cursor.prev
                data_node.next = space_node
                space_node.prev = data_node
                space_node.next = cursor.next
                cursor.prev.next = data_node
                right.id = None
                cursor = cursor.next
            else:
                cursor = cursor.next
        right = right.prev
    print(checksum(fs_str(head)))


if __name__ == '__main__':
    main()
