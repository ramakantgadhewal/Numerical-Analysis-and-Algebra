# import libs
# 二分法 / 牛顿方法 求非线性方程的根
from math import exp, log
from numpy import abs
import pandas as pd

def test_function(x):
    return exp(x) * log(x) - x**2


def main():
    # you can change these vars
    a, b, err = 2, 1, 1e-5
    bisection = Bisection(test_function, a, b, err)
    solution = bisection.find_root()
    return

class Bisection():
    def __init__(self, f, a, b, e) -> None:
        self.function = f   #  非线性函数
        self.high = a # 求解区间上界
        self.low = b # 下界
        self.error = e # 误差
    
    def find_root(self):
        self._check_before_run()
        function = self.function
        high = self.high
        low = self.low
        error = self.error

        while(abs(high - low) > error):
            # core algorithms
            mid = (high + low) / 2
            if abs(function(mid)) < error:
                return mid
            elif function(low) * function(mid) < 0:
                high = mid
            elif function(high) * function(mid) < 0:
                low = mid
            # updating logs
        
        mid = (high + low) / 2
        print(f"Final result{mid}")

        return mid
    
    def _check_before_run(self):
        assert self.function(self.high) * self.function(self.low) < 0
    
# test
if __name__ == '__main__':  
    main()
