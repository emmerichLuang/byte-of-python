

class EEMath:
    def add(self, a, b):
        return a+b

    @staticmethod
    def static_add(a, b):
        return a+b


# 要一个实例化
m = EEMath();
print('要实例化:', m.add(1, 1))
print('要实例化:', EEMath().add(1, 1))

# 不需要实例化
print('不需要实例化:', EEMath.static_add(1,2))

