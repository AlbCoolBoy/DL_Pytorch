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
print(x[0, :])

# 广播机制，当对两个额形状不同的tensor进行按元素计算的时候，会触发广播机制，
# 将两个tensor通过复制变成形状相同的tensor进行计算
add1=torch.arange(1,3).view(1,2)
print(add1)
add2=torch.arange(1,4).view(3,1)
print(add2)
print(add1+add2)

#运算的内存开销
#索引和view是不会开辟新内存的，但是像上面的加法运算会开辟新的内存
el1=torch.tensor([2,1])
el2=torch.tensor([3,4])
id_before=id(el2)
el2=el2+el1
print(id(el2)==id_before)
#如果不想创建新的内存，可以使用索引的方式直接运算结果放进之前的el2内存中
#这样就不用开辟新的内存空间而将结果直接放进之前的内存空间
el1=torch.tensor([2,1])
el2=torch.tensor([3,4])
id_before=id(el2)
el2[:]=el1+el2
print(id(el2)==id_before)

#Tensor和Numpy的转换
t1=torch.ones(5)
t2=t1.numpy()
print(t1)
print(t2)