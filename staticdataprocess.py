import numpy
# from tsai.all import *
import pandas as pd
import numpy as np
from openpyxl import load_workbook
from sklearn.model_selection import train_test_split
import os
import torch
import cv2 as cv
# # computer_setup()
# # dsid = 'NATOPS'
# # X, y, splits = get_UCR_data(dsid, return_split=False)
# # print(X.shape)
# # print(y.shape)
# data=pd.read_csv('train_data.csv')
# data=np.array(data)
# predata=np.zeros((1,64))
# for i in range(0,data.shape[0]-1):  #先检测出两个手势的交界处，并且要求手势的时间长度要大于10
#     if (data[i,0]!=data[i+1,0]) and (data[i,0]==data[i-1,0]==data[i-2,0]==data[i-3,0]==data[i-4,0]==data[i-5,0]
#                                      ==data[i-5,0]==data[i-6,0]==data[i-7,0]==data[i-8,0]==data[i-9,0]):
#                                      #==data[i-10,0]==data[i-11,0]==data[i-12,0]==data[i-13,0]==data[i-14,0]):
#         predata=np.vstack((predata,data[i-9:i+1,:]))
#
#
# feature_num=64      #63个特征
# sample_length=10    #时间长度为10
# sample_num=int((predata.shape[0]-1)/10)     #满足要求的样本数量
# data=predata[1:,:]     #取出标签列
# for i in range(len(data)):
#     data[i][0] = data[i][0] - 1
#
# # y=y.reshape(sample_num,sample_length)   #每个标签重复了10次，只取1次即可
# # y=y[:,0]
# # X=predata[1:,1:]    #取出特征列
# X = data.reshape(sample_num,sample_length,feature_num)
# # X = X.transpose(0, 2, 1)    #交换维度以满足网络输入条件
# X_train,X_test =train_test_split(X,test_size=0.3)
# #
# # for batch_x, targets in enumerate([X_train, y_train]):
# #
# #     print(targets)
#
# # trainloader = torch.utils.data.DataLoader(X_train, batch_size=32, shuffle=True)
# # for batch_idx, data in enumerate(trainloader):
# #     # inputs, targets = inputs.to('cpu'), targets.to('cpu')
# #     inputs = data[:, :, 1:].to('cpu')
# #     print(inputs.shape)
# #     targets = data[:, :, 0].to('cpu')


data=pd.read_csv('figure.csv')
data=np.array(data)
h, w = data.shape

datas = []

def drawline(x, y, List, img):
    img_size = 128
    i1_x = int(List[3*x+1] * img_size)
    i1_y = int(List[3*x+2] * img_size)
    if i1_x > img_size - 1:
        i1_x = img_size - 1
    if i1_y > img_size - 1:
        i1_y = img_size - 1

    i2_x = int(List[3 * y+1] * img_size)
    i2_y = int(List[3 * y + 2] * img_size)
    if i2_x > img_size - 1:
        i2_x = img_size - 1
    if i2_y > img_size - 1:
        i2_y = img_size - 1
    cv.line(img, (i1_x, i1_y), (i2_x, i2_y), 255, 2)
def drawlines(x, List, img):
    drawline(x, x+1, List, img)
    drawline(x+1, x+2, List, img)
    drawline(x+2, x+3, List, img)

def drawhand(List, img):
    drawlines(1, List, img)
    drawlines(5, List, img)
    drawlines(9, List, img)
    drawlines(13, List, img)
    drawlines(17, List, img)

    drawline(0, 5, List, img)
    drawline(5, 9, List, img)
    drawline(9, 13, List, img)
    drawline(13, 17, List, img)
    drawline(0, 17, List, img)
    drawline(0, 1, List, img)
img_size = 128
for i in range(h):
    # print("\rProcess {}/{} data".format(i, h), end='')
    data_list = []
    img = np.zeros([img_size, img_size], np.uint8)
    data_list.append(data[i][0])
    # print(data_list)
    drawhand(data[i], img)

    # cv.imshow('img', img)
    # cv.waitKey()
    # cv.destroyAllWindows()
    # for j in range(1, w, 3):
    #     i_x = int(data[i][j] * img_size)
    #     i_y = int(data[i][j+1] * img_size)
    #     if i_x > img_size - 1:
    #         i_x = img_size - 1
    #     if i_y > img_size - 1:
    #         i_y = img_size - 1
    #     # print(i_x, i_y)
    #     img[i_x][i_y] = 255

        # img[i_x-1][i_y-1] = 255
        # img[i_x-1][i_y] = 255
        # img[i_x][i_y-1] = 255
        # img[i_x+1][i_y+1] = 255
        # img[i_x+1][i_y-1] = 255
        # img[i_x-1][i_y+1] = 255
        # img[i_x+1][i_y] = 255
        # img[i_x][i_y+1] = 255
    data_list.append(img)
    datas.append(data_list)





X_train,X_test =train_test_split(datas,test_size=0.3)
if __name__ == "__main__":

    trainloader = torch.utils.data.DataLoader(X_train, batch_size=32, shuffle=True)
    for batch_idx, data in enumerate(trainloader):
        label, img = data
        img = img.unsqueeze(1)
        # print(img.shape)
