import cv2
import torch
import torch.nn as nn
import numpy as np
class CNN_MODEL(nn.Module):
    def __init__(self, num_classes=6):
        super().__init__()
        self.features = nn.Sequential(
            #1
            nn.Conv2d(1, 64, kernel_size=5, stride = 1, padding=1),
            nn.BatchNorm2d(64),
            nn.ReLU(True),
            #2
            # nn.Conv2d(64, 64, kernel_size=3, padding=1),
            # nn.BatchNorm2d(64),
            # nn.ReLU(True),
            nn.MaxPool2d(kernel_size=2, stride=2),
            # 3
            nn.Conv2d(64, 128, kernel_size=5, stride = 1, padding=1),
            nn.BatchNorm2d(128),
            nn.ReLU(True),
            # 4
            # nn.Conv2d(128, 128, kernel_size=3, padding=1),
            # nn.BatchNorm2d(128),
            # nn.ReLU(True),
            nn.MaxPool2d(kernel_size=2, stride=2),
            # 5
            nn.Conv2d(128, 256, kernel_size=3, stride = 2, padding=1),
            nn.BatchNorm2d(256),
            nn.ReLU(True),
            # 6
            # nn.Conv2d(256, 256, kernel_size=3, padding=1),
            # nn.BatchNorm2d(256),
            # nn.ReLU(True),
            # 7
            # nn.Conv2d(256, 256, kernel_size=3, padding=1),
            # nn.BatchNorm2d(256),
            # nn.ReLU(True),
            nn.MaxPool2d(kernel_size=2, stride=2),
            # 8
            nn.Conv2d(256, 512, kernel_size=3, stride = 2, padding=1),
            nn.BatchNorm2d(512),
            nn.ReLU(True),
            # 9
            # nn.Conv2d(512, 512, kernel_size=3, padding=1),
            # nn.BatchNorm2d(512),
            # nn.ReLU(True),
            # # 10
            # nn.Conv2d(512, 512, kernel_size=3, padding=1),
            # nn.BatchNorm2d(512),
            # nn.ReLU(True),
            nn.MaxPool2d(kernel_size=2, stride=2),
            # # 11
            # nn.Conv2d(512, 512, kernel_size=3, padding=1),
            # nn.BatchNorm2d(512),
            # nn.ReLU(True),
            # 12
            # nn.Conv2d(512, 512, kernel_size=3, padding=1),
            # nn.BatchNorm2d(512),
            # nn.ReLU(True),
            # # 13
            # nn.Conv2d(512, 512, kernel_size=3, padding=1),
            # nn.BatchNorm2d(512),
            # nn.ReLU(True),
            # nn.MaxPool2d(kernel_size=2, stride=2),
            # nn.AvgPool2d(kernel_size=1, stride=1),
        )
        #原本的线性层
        self.classifier = nn.Sequential(
            #14
            nn.Linear(512*4, 512),
            nn.ReLU(True),
            nn.Dropout(),
            #15
            nn.Linear(512, 64),
            nn.ReLU(True),
            nn.Dropout(),
            #16
            nn.Linear(64, num_classes)

        )
        #测试线性层
        self.classifier1 = nn.Sequential(

            nn.Linear(512, 6)
        )
    def forward(self, x):
        out = self.features(x)
        # print(out.shape)
        out = out.view(out.size(0), -1)
        out = self.classifier(out)
        return out

if __name__ == "__main__":
    from figure_input import drawhand
    model = CNN_MODEL()
    input=torch.randn([1, 1, 128, 128])
    img = torch.tensor(input)
    out = model(input)
    # print(out.shape)


#     model.eval()
#     # 加载参数
#     model_param = torch.load('model_param.pkl')
#     # 为模型设置参数
#     model.load_state_dict(model_param)
#     print('file loaded')
#     data = np.array(
# [1, 0.4143, 1.0183, 0.0, 0.4818, 0.986, -0.0275, 0.5141, 0.9387, -0.0479, 0.5173, 0.8726, -0.0709, 0.4803, 0.8247, -0.0908, 0.5049, 0.7519, -0.0298, 0.5383, 0.6243, -0.06, 0.5526, 0.5517, -0.0791, 0.5557, 0.4854, -0.094, 0.4571, 0.7391, -0.0409, 0.4576, 0.6018, -0.0946, 0.4535, 0.5095, -0.1312, 0.4476, 0.4251, -0.1525, 0.4135, 0.7645, -0.052, 0.4102, 0.6593, -0.1053, 0.429, 0.7382, -0.1035, 0.4414, 0.7963, -0.0884, 0.3714, 0.8208, -0.0652, 0.3685, 0.7432, -0.1072, 0.3921, 0.7837, -0.1019, 0.4065, 0.8259, -0.0874])
#     img = np.zeros([64, 64], np.uint8)
#     drawhand(data, img)
#     cv2.imshow('img', img)
#     cv2.waitKey()
#     cv2.destroyAllWindows()
#     img = torch.tensor(img)
#     img = img.to(torch.float32)
#     img = img.unsqueeze(0)
#     img = img.unsqueeze(1)
#     print(img.shape)
#     output = model(img)
#     print(output)
#     _, out = torch.max(output, 1)
#     print(int(out))
