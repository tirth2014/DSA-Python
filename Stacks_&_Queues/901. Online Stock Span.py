# Push every pair of <price, result> to a stack.
# Pop lower price from the stack and accumulate the count.

# One price will be pushed once and popped once.
# So 2 * N times stack operations and N times calls.
# time complexity is amortized O(1)

class StockSpanner:  
    def __init__(self):
        # maintain a monotonic stack for stock entry
        self.stack = []

    def next(self, price: int) -> int:
        res = 1
        while self.stack and self.stack[-1][0] <= price:
            res += self.stack.pop()[1]
        self.stack.append([price, res])
        return res


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
