class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self._arr = []
        self._min_val = None


    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if self._min_val is None:
            self._arr.append(x)
            self._min_val = x
        else:
            insert_val = x
            if x < self._min_val:
                insert_val = 2 * x - self._min_val
                self._min_val = x
            self._arr.append(insert_val)

    def pop(self):
        """
        :rtype: void
        """
        output_val = self._arr.pop()
        if not self._arr:
            self._min_val = None
            return output_val
        if output_val < self._min_val:
            y = 2 * self._min_val - output_val
            output_val = self._min_val
            self._min_val = y
        return output_val

    def top(self):
        """
        :rtype: int
        """
        if len(self._arr) == 0:
            return None
        if self._arr[-1] >= self._min_val:
            return self._arr[-1]
        else:
            return self._min_val

    def getMin(self):
        """
        :rtype: int
        """
        return self._min_val


# Your MinStack object will be instantiated and called as such:
minStack = MinStack()
print minStack.push(-2)
print minStack.push(0)
print minStack.push(-3)

print "1", minStack.getMin()  #;   --> Returns -3.
print "stack arr before pop", minStack._arr
print minStack.pop()     #;
print "stack arr after pop", minStack._arr
print "2", minStack.top()     #;      --> Returns 0.
print "3", minStack.getMin()  # ;   --> Returns -2.

f = open("", 'r')
f.readline()