import numpy
from tsai.all import *
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
# computer_setup()
# dsid = 'NATOPS'
# X, y, splits = get_UCR_data(dsid, return_split=False)
# print(X.shape)
# print(y.shape)
data=pd.read_csv('Gestures2.csv')
data=np.array(data)
predata=np.zeros((1,64))
for i in range(0,data.shape[0]-1):  #先检测出两个手势的交界处，并且要求手势的时间长度要大于10
    if (data[i,0]!=data[i+1,0]) and (data[i,0]==data[i-1,0]==data[i-2,0]==data[i-3,0]==data[i-4,0]==data[i-5,0]
                                     ==data[i-5,0]==data[i-6,0]==data[i-7,0]==data[i-8,0]==data[i-9,0]):
                                     #==data[i-10,0]==data[i-11,0]==data[i-12,0]==data[i-13,0]==data[i-14,0]):
        predata=np.vstack((predata,data[i-9:i+1,:]))

feature_num=63      #63个特征
sample_length=10    #时间长度为10
sample_num=int((predata.shape[0]-1)/10)     #满足要求的样本数量
y=predata[1:,0]     #取出标签列
y=y.reshape(sample_num,sample_length)   #每个标签重复了10次，只取1次即可
y=y[:,0]
X=predata[1:,1:]    #取出特征列
X = X.reshape(sample_num,sample_length,feature_num)
X = X.transpose(0, 2, 1)    #交换维度以满足网络输入条件
X_train,X_test, y_train, y_test =train_test_split(X,y,test_size=0.3)

# Prepare Data
X1, y1, splits = combine_split_data([X_train, X_test], [y_train, y_test])
tfms  = [None, [Categorize()]]
dsets = TSDatasets(X1, y1, tfms=tfms, splits=splits, inplace=True)    #create datasets
dls = TSDataLoaders.from_dsets(dsets.train, dsets.valid, bs=[64, 128], batch_tfms=[TSStandardize()], num_workers=0)
dls.show_batch(sharey=True)

# Build Learner
model = InceptionTime(dls.vars, dls.c)      #采用InceptionTime
learn = Learner(dls, model, metrics=accuracy)
learn.save('stage0')

# Train model
learn.load('stage0')
learn.lr_find()
learn.fit_one_cycle(25, lr_max=1e-3)
learn.save('stage1')
learn.recorder.plot_metrics()
# save data
learn.save_all(path='export', dls_fname='dls', model_fname='model', learner_fname='learner')
del learn, dsets, dls
# load data
learn = load_learner_all(path='export', dls_fname='dls', model_fname='model', learner_fname='learner')
dls = learn.dls
valid_dl = dls.valid    #获取验证集
b = next(iter(valid_dl))
valid_probas, valid_targets, valid_preds = learn.get_preds(dl=valid_dl, with_decoded=True)  #样本属于各类的概率，各个样本的标签，各个样本的预测结果
(valid_targets == valid_preds).float().mean()
learn.show_results()
learn.show_probas()
interp = ClassificationInterpretation.from_learner(learn)
interp.plot_confusion_matrix()      #混淆矩阵
interp.most_confused(min_val=3)

# Prediction
# Labeled test data
test_ds = valid_dl.dataset.add_test(X, y)
test_dl = valid_dl.new(test_ds)
next(iter(test_dl))
test_probas, test_targets, test_preds = learn.get_preds(dl=test_dl, with_decoded=True, save_preds=None, save_targs=None)
print(f'accuracy: {skm.accuracy_score(test_targets, test_preds):10.6f}')
# Unlabeled data
test_ds = dls.dataset.add_test(X)
test_dl = valid_dl.new(test_ds)
next(iter(test_dl))
test_probas, *_ = learn.get_preds(dl=test_dl, save_preds=None)





