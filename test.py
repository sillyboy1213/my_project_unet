import torch
x = torch.randn(1,2)
x = x.to('cuda' if torch.cuda.is_available() else 'cpu')
print(x)