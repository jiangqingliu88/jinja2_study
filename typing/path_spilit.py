import os
path_01='D:/User/wgy/workplace/data/notMNIST_large.tar.gar'
path_02='D:/User/wgy/workplace/data/notMNIST_large'
root_01=os.path.splitext(path_01)[0].strip(".")
root_02=os.path.splitext(path_02)[0].strip(".")
print(root_01)
print(root_02)