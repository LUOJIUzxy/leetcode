class SupermarketCheckout:
    def __init__(self):
        self.lines = {}  # Key: LineNumber, Value: Queue of (CustomerId, NumItems)

    def on_customer_enter(self, customer_id, line_number, num_items):
        # TODO Implement
        if line_number not in self.lines:
            self.lines[line_number] = []
        self.lines[line_number].append((customer_id, num_items))

    def on_basket_change(self, customer_id, new_num_items):
        # TODO Implement
        for line in self.lines.values():
            for i, (cid, items) in enumerate(line):
                if cid == customer_id:
                    if new_num_items > items:
                        line.append((cid, new_num_items))
                        del line[i]
                    else:
                        line[i] = (cid, new_num_items)
                    break

    def on_line_service(self, line_number, num_processed_items):
        # TODO Implement
        if line_number in self.lines and self.lines[line_number]:
            customer = self.lines[line_number][0]
            remaining_items = customer[1] - num_processed_items
            if remaining_items <= 0:
                self.on_customer_exit(customer[0])
                self.lines[line_number].pop(0)
            else:
                self.lines[line_number][0] = (customer[0], remaining_items)

    def on_lines_service(self):
        # TODO Implement
        for line in self.lines.values():
            if line:
                customer = line[0]
                remaining_items = customer[1] - 1
                if remaining_items <= 0:
                    self.on_customer_exit(customer[0])
                    line.pop(0)
                else:
                    line[0] = (customer[0], remaining_items)

    def on_customer_exit(self, customer_id):
        # Don't change this implementation.
        print(customer_id)

if __name__ == "__main__":
    import sys

    checkout_tracker = SupermarketCheckout()
    line = sys.stdin.readline().split()
    n = int(line[0])
    for _ in range(n):
        line = sys.stdin.readline().split()
        if line[0] == "CustomerEnter":
            customer_id = int(line[1])
            line_number = int(line[2])
            num_items = int(line[3])
            checkout_tracker.on_customer_enter(customer_id, line_number, num_items)
        elif line[0] == "BasketChange":
            customer_id = int(line[1])
            new_num_items = int(line[2])
            checkout_tracker.on_basket_change(customer_id, new_num_items)
        elif line[0] == "LineService":
            line_number = int(line[1])
            num_processed_items = int(line[2])
            checkout_tracker.on_line_service(line_number, num_processed_items)
        elif line[0] == "LinesService":
            checkout_tracker.on_lines_service()
        else:
            raise Exception("Malformed input!")