import torch

#创建未初始化的tensor
x=torch.empty(5,3)
# tensor是存储和变换数据的工具，提供GPU计算和自动求梯度的功能，更加适合深度学习
print(x)

#创建随机初始化的tensor
y=torch.rand(5,3)
print(y)

#初始化全0的tensor,参数列表：行数，列数，指定数据类型
z=torch.zeros(5,3,dtype=torch.long)
print(z)

#根据给定的数据直接创建
print(torch.tensor([5.5,3]))

print(x.shape)
print(x.size())