class SolutionDP(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        climb_ways = [0] * n
        climb_ways[0] = 1
        climb_ways[1] = 2
        for i in range(2, n):
            climb_ways[i] += climb_ways[i-1]
            climb_ways[i] += climb_ways[i-2]
        return climb_ways[n-1]

class SolutionNaive(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = self.gen_comb(n)
        print result
        return len(result)


    def gen_comb(self, n):
        methods = []

        for i in [1, 2]:

            if n - i > 0:
                base = [i]
                for sub_comb in self.gen_comb(n - i):
                    methods.append(base + sub_comb)
            elif n - i < 0:
                continue
            else:
                methods.append([i])
        return methods

if __name__ == '__main__':
    s = SolutionDP()
    print s.climbStairs(10)