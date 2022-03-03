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
    b_solver = BisectionSolver()
    result = b_solver.find_root(test_function, a, b, err)
    print(f"Bisection solver result is {result}")

    n_solver = NewtonianSolver()
    result = n_solver.find_root(test_function, 2)
    print(f"Newtonian solver result is {result}")
    return

class BisectionSolver():
    def __init__(self) -> None:
        return
    
    def find_root(self, function, high, low, error):
        self._check_before_run(function, high, low)

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
        return mid
    
    def _check_before_run(self, function, high, low):
        assert function(high) * function(low) < 0
        return

class NewtonianSolver():
    def __init__(self) -> None:
        return
    
    def find_root(self, f, x, eps=1e-5, max_step=100, h=1e-5):
        """f: 待求函数
        g: f 的导数, 讲道理这个值也应该利用数值微分 f(x + h) - f(x) / h 得到, 之后再implement
        x: 初始点
        """
        df = (f(x + h) - f(x)) / h
        for i in range(max_step):
            x_ = x - f(x) / df
            if abs(x_ - x) < eps:
                return x_
            x  = x_
        
        raise ValueError(f"在{x}附近函数无根！")

# test
if __name__ == '__main__':  
    main()
