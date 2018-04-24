# 建议用括号，明确是tuple类型
# 类似set结构

zoo = ('python', 'elephant', 'penguin')
print('Number of animals in the zoo is', len(zoo))

new_zoo = 'monkey', 'camel', zoo

# 直接length，一维数组
print('Number of cages in the new zoo is', len(new_zoo))

# 直接输出，就是递归包含所有的元素
print('\nAll animals in new zoo are', new_zoo)

# 下标0开始
print('\nAnimals brought from old zoo are', new_zoo[2])
print('Last animal brought from old zoo is', new_zoo[2][2])


print('\nNumber of animals in the new zoo is', len(new_zoo)-1+len(new_zoo[2]))

