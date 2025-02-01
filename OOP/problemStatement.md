## Problem Statement
A supermarket has many customers entering and exiting at various points. They want to keep track of customers and get notifications when a customer leaves the store.

There are a number of checkout lines, where customers with baskets of items queue to pay and exit the store. Individual checkout lines and customers are assigned numerical IDs.

As happens in life, sometimes customers want to add more items to their baskets, and sometimes they realize that they don’t need certain items they picked up earlier and remove them from the basket.

To enforce checkout priorities, a few rules have been implemented in the supermarket:

1. A customer cannot switch lines before exiting once they join a given checkout line.

2. If a customer increases the number of items to purchase, they must go to the back of the same line.

3. If a customer removes items from their basket, they will keep their position in the line (or leave the store if they don’t have any more items).

A customer will leave the supermarket as soon as they have no items left to checkout. Note that the lines with smaller IDs are closer to the exit, so if two customers pass the checkout line at the same time, the one closer to the exit would leave the store first.

## Instructions
You will receive a stream of N instructions. Each instruction can be one of the following actions:

1. CustomerEnter: Indicates that a customer joined a checkout line.

Attributes: CustomerId, LineNumber, NumItems.

2. BasketChange: Indicates that a customer changed the number of items in their basket.

Attributes: CustomerId, NewNumItems.

3. LineService: Indicates that several items have been processed in a specific line.

Attributes: LineNumber, NumProcessedItems.

4. LinesService: Indicates that 1 item has been processed in every line (if there are 4 lines, then in total 4 items are processed).

No attributes.

## Functionality to Implement
You are required to implement a class SupermarketCheckout that provides the following methods:

1. `on_customer_enter(customer_id, line_number, num_items)`:
Handles the event when a customer enters a checkout line.

2. `on_basket_change(customer_id, new_num_items)`:
Handles the event when a customer changes the number of items in their basket.

3. `on_line_service(line_number, num_processed_items)`:
Handles the event when items are processed in a specific line.

4. `on_lines_service()`:
Handles the event when one item is processed in every line.

5. Additionally, the `on_customer_exit(customer_id)` method is provided for you and should be called to notify when a customer leaves the store.

## Constraints
1. The number of customers and lines is limited.

- `0 < N ≤ 10^5`

- `0 < CustomerId, LineNumber ≤ 10^5`

- `0 < NumItems, NewNumItems, NumProcessedItems ≤ 10^5`

2. It is guaranteed that `on_basket_change` will only be called for customers who are still in the store.

## Input Format
The input to the program is specified using a simple text format. The first line contains an integer N, which denotes the number of instructions. Each of the subsequent N lines contains one of the following instructions:

1. CustomerEnter:
Format: `CustomerEnter <CustomerId> <LineNumber> <NumItems>`.

2. BasketChange:
Format: `BasketChange <CustomerId> <NewNumItems>`.

3. LineService:
Format: `LineService <LineNumber> <NumProcessedItems>`.

4. LinesService:
Format: `LinesService`.

## Output Format
The program should call the `on_customer_exit(customer_id)` method whenever a customer leaves the store. This method will print the `customer_id`.

## Sample Input and Output
### Sample Input 0:
```
5
CustomerEnter 123 1 5
CustomerEnter 2 2 3
LinesService
CustomerEnter 3 1 2
LineService 1 6
```

### Sample Output 0:
```
123
3
```

### Explanation:
- Initially, customers `123` and `2` are in lines `1` and `2`, respectively.

- After the first `LinesService`, both customers still have items to process.

- Customer `3` joins line `1`.

- After the `LineService` on line `1`, customers `123` and `3` are checked out in that order.

### Sample Input 1:
```
5
CustomerEnter 123 1 5
CustomerEnter 3 1 2
LineService 1 4
BasketChange 123 6
LineService 1 5
```

### Sample Output 1:
```
3
123
```

### Explanation:
- After the first `LineService`, customer `123` has 1 item left.

- Customer `123` increases their basket size, moving to the back of the line.

- During the next `LineService`, customer `3` is checked out first, followed by customer `123`.

## Notes
1. The `NewNumItems` attribute of the `BasketChange` action represents the total number of items in the basket after the change.

2. `LineService` calls with no queue in the line should be ignored.

3. The `on_customer_exit` method is already implemented and should not be modified.