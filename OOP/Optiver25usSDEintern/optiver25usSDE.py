import sys


class _CustomerNode:
    __slots__ = ("customer_id", "total_items", "processed", "line_number", "prev", "next")

    def __init__(self, customer_id, items, line_number):
        self.customer_id = customer_id
        self.total_items = items
        self.processed = 0
        self.line_number = line_number
        self.prev = None
        self.next = None


class _TreapNode:
    __slots__ = ("key", "priority", "left", "right")

    def __init__(self, key):
        self.key = key
        self.priority = _treap_priority(key)
        self.left = None
        self.right = None


def _treap_priority(key):
    x = (key + 0x9E3779B97F4A7C15) & 0xFFFFFFFFFFFFFFFF
    x ^= x >> 30
    x = (x * 0xBF58476D1CE4E5B9) & 0xFFFFFFFFFFFFFFFF
    x ^= x >> 27
    x = (x * 0x94D049BB133111EB) & 0xFFFFFFFFFFFFFFFF
    x ^= x >> 31
    return x


def _treap_insert(root, key):
    if root is None:
        return _TreapNode(key)
    if key < root.key:
        root.left = _treap_insert(root.left, key)
        if root.left.priority < root.priority:
            child = root.left
            root.left = child.right
            child.right = root
            return child
    elif key > root.key:
        root.right = _treap_insert(root.right, key)
        if root.right.priority < root.priority:
            child = root.right
            root.right = child.left
            child.left = root
            return child
    return root


def _treap_delete(root, key):
    if root is None:
        return None
    if key < root.key:
        root.left = _treap_delete(root.left, key)
        return root
    if key > root.key:
        root.right = _treap_delete(root.right, key)
        return root
    if root.left is None:
        return root.right
    if root.right is None:
        return root.left
    if root.left.priority < root.right.priority:
        child = root.left
        root.left = child.right
        child.right = root
        child.right = _treap_delete(child.right, key)
        return child
    child = root.right
    root.right = child.left
    child.left = root
    child.left = _treap_delete(child.left, key)
    return child


class SupermarketCheckout:
    def __init__(self):
        self.lines = {}
        self.customers = {}
        self.active_lines = None

    def on_customer_enter(self, customer_id, line_number, num_items):
        node = _CustomerNode(customer_id, num_items, line_number)
        self.customers[customer_id] = node
        line = self.lines.get(line_number)
        if line is None:
            self.lines[line_number] = [node, node]
            self.active_lines = _treap_insert(self.active_lines, line_number)
            return
        tail = line[1]
        tail.next = node
        node.prev = tail
        line[1] = node

    def on_basket_change(self, customer_id, new_num_items):
        node = self.customers[customer_id]
        new_remaining_items = new_num_items - node.processed
        if new_remaining_items <= 0:
            self._remove_customer(node)
            self.on_customer_exit(customer_id)
            return
        if new_num_items > node.total_items:
            node.total_items = new_num_items
            line = self.lines[node.line_number]
            if node is line[1]:
                return
            prev_node = node.prev
            next_node = node.next
            if prev_node is None:
                line[0] = next_node
            else:
                prev_node.next = next_node
            next_node.prev = prev_node
            tail = line[1]
            tail.next = node
            node.prev = tail
            node.next = None
            line[1] = node
            return
        node.total_items = new_num_items

    def on_line_service(self, line_number, num_processed_items):
        line = self.lines.get(line_number)
        while line is not None and num_processed_items > 0:
            head = line[0]
            remaining_items = head.total_items - head.processed
            if remaining_items > num_processed_items:
                head.processed += num_processed_items
                return
            num_processed_items -= remaining_items
            customer_id = head.customer_id
            self._remove_customer(head)
            self.on_customer_exit(customer_id)
            line = self.lines.get(line_number)

    def on_lines_service(self):
        for line_number in self._iter_active_lines():
            line = self.lines.get(line_number)
            if line is None:
                continue
            head = line[0]
            if head.total_items - head.processed > 1:
                head.processed += 1
                continue
            customer_id = head.customer_id
            self._remove_customer(head)
            self.on_customer_exit(customer_id)

    def on_customer_exit(self, customer_id):
        print(customer_id)

    def _remove_customer(self, node):
        line_number = node.line_number
        line = self.lines[line_number]
        prev_node = node.prev
        next_node = node.next
        if prev_node is None:
            line[0] = next_node
        else:
            prev_node.next = next_node
        if next_node is None:
            line[1] = prev_node
        else:
            next_node.prev = prev_node
        del self.customers[node.customer_id]
        if line[0] is None:
            del self.lines[line_number]
            self.active_lines = _treap_delete(self.active_lines, line_number)

    def _iter_active_lines(self):
        stack = []
        node = self.active_lines
        while stack or node is not None:
            while node is not None:
                stack.append(node)
                node = node.left
            node = stack.pop()
            yield node.key
            node = node.right


if __name__ == "__main__":
    checkout_tracker = SupermarketCheckout()
    read_line = sys.stdin.buffer.readline
    n = int(read_line())
    for _ in range(n):
        parts = read_line().split()
        action = parts[0]
        if action == b"CustomerEnter":
            checkout_tracker.on_customer_enter(int(parts[1]), int(parts[2]), int(parts[3]))
        elif action == b"BasketChange":
            checkout_tracker.on_basket_change(int(parts[1]), int(parts[2]))
        elif action == b"LineService":
            checkout_tracker.on_line_service(int(parts[1]), int(parts[2]))
        elif action == b"LinesService":
            checkout_tracker.on_lines_service()
        else:
            raise Exception("Malformed input!")
