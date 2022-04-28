import torch

x=torch.ones(2,2,requires_grad=True)
print(x)
print(x.grad_fn)

y=x+2
print(y)
print(y.grad_fn)
#返回值是与刚才进行的运算相关的对象

