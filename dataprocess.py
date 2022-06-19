import numpy
# from tsai.all import *
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import torch
# computer_setup()
# dsid = 'NATOPS'
# X, y, splits = get_UCR_data(dsid, return_split=False)
# print(X.shape)
# print(y.shape)
data=pd.read_csv('train.csv')
data=np.array(data)
predata=np.zeros((1,64))
for i in range(0,data.shape[0]-1):  #先检测出两个手势的交界处，并且要求手势的时间长度要大于10
    if (data[i,0]!=data[i+1,0]) and (data[i,0]==data[i-1,0]==data[i-2,0]==data[i-3,0]==data[i-4,0]==data[i-5,0]
                                     ==data[i-5,0]==data[i-6,0]==data[i-7,0]==data[i-8,0]==data[i-9,0]):
                                     # ==data[i-10,0]==data[i-11,0]==data[i-12,0]==data[i-13,0]==data[i-14,0]):
        predata=np.vstack((predata,data[i-9:i+1,:]))


feature_num=64      #63个特征
sample_length=10    #时间长度为10
sample_num=int((predata.shape[0]-1)/10)     #满足要求的样本数量
data=predata[1:,:]     #取出标签列
for i in range(len(data)):
    data[i][0] = data[i][0] - 1

# y=y.reshape(sample_num,sample_length)   #每个标签重复了10次，只取1次即可
# y=y[:,0]
# X=predata[1:,1:]    #取出特征列
X = data.reshape(sample_num,sample_length,feature_num)
# X = X.transpose(0, 2, 1)    #交换维度以满足网络输入条件
X_train,X_test =train_test_split(X,test_size=0.3)
print(len(X_train))
print(len(X_test))
# print("X_train")
# print(X_train)
# print("X_test")
# print(X_test)
#
# for batch_x, targets in enumerate([X_train, y_train]):
#
#     print(targets)

# trainloader = torch.utils.data.DataLoader(X_train, batch_size=32, shuffle=True)
# for batch_idx, data in enumerate(trainloader):
#     # inputs, targets = inputs.to('cpu'), targets.to('cpu')
#     inputs = data[:, :, 1:].to('cpu')
#     print(inputs.shape)
#     targets = data[:, :, 0].to('cpu')


