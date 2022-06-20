import torch
import torch.nn as nn
import torch.optim as optim
import torchvision
from torchvision import transforms
from dataprocess import X_train, X_test
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt


class LSTM(nn.Module):
    def __init__(self, in_dim, hidden_dim, n_layer, n_class):
        super(LSTM, self).__init__()
        self.n_layer = n_layer
        self.hidden_dim = hidden_dim
        self.lstm = nn.LSTM(in_dim, hidden_dim, n_layer,
                            batch_first=True)
        self.classifier = nn.Linear(hidden_dim, n_class)

    def forward(self, x):
        # h0 = Variable(torch.zeros(self.n_layer, x.size(1),
        #   self.hidden_dim)).cuda()
        # c0 = Variable(torch.zeros(self.n_layer, x.size(1),
        #   self.hidden_dim)).cuda()
        out, _ = self.lstm(x)
        out = out[:, -1, :]
        out = self.classifier(out)
        return out


# trainset = torchvision.datasets.MNIST(root='./data', train=True, download=True, transform=transform)
trainloader = torch.utils.data.DataLoader(X_train, batch_size=32, shuffle=True)
#
# testset = torchvision.datasets.MNIST(root='./data', train=False, download=True, transform=transform)
testloader = torch.utils.data.DataLoader(X_test, batch_size=32, shuffle=False)

net = LSTM(63, 32, 2, 3)

net = net.to('cpu')
criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(net.parameters(), lr=0.1, momentum=0.9)

# Training
def train(epoch):
    print('\nEpoch: %d' % epoch)
    net.train()
    train_loss = 0
    correct = 0
    total = 0
    for batch_idx, data in enumerate(trainloader):
        # inputs, targets = inputs.to('cpu'), targets.to('cpu')
        inputs = data[:, :, 1:].to(torch.float32).to('cpu')
        # print(inputs.shape)
        targets = data[:, 0, 0].to(torch.long).to('cpu')


        optimizer.zero_grad()
        # outputs = net(torch.squeeze(inputs, 1))
        outputs = net(inputs)
        loss = criterion(outputs, targets)
        loss.backward()
        optimizer.step()

        train_loss += loss.item()
        _, predicted = outputs.max(1)
        total += targets.size(0)
        correct += predicted.eq(targets).sum().item()

    print('train Loss: %.3f | Acc: %.3f%% '
            % (train_loss/(batch_idx+1), 100.*correct/total))

def test(epoch):
    global best_acc
    net.eval()
    test_loss = 0
    correct = 0
    total = 0
    with torch.no_grad():
        for batch_idx, data in enumerate(testloader):
            # inputs, targets = inputs.to('cpu'), targets.to('cpu')
            inputs = data[:, :, 1:].to(torch.float32).to('cpu')
            # print(inputs)
            # print(inputs.shape)
            targets = data[:, 0, 0].to(torch.long).to('cpu')
            # outputs = net(torch.squeeze(inputs, 1))
            outputs = net(inputs)
            loss = criterion(outputs, targets)

            test_loss += loss.item()
            _, predicted = outputs.max(1)
            total += targets.size(0)
            correct += predicted.eq(targets).sum().item()

        print('teat Loss: %.3f | Acc: %.3f%% '
                % (test_loss/(batch_idx+1), 100.*correct/total))


if __name__ == "__main__":
    # 训练模型
    for epoch in range(100):
        train(epoch)
        test(epoch)
    # torch.save(net.state_dict(), 'model_param.pkl')
        # 保存模型
        torch.save(net, "model.pth")
        print('file loaded!')
    # torch.save(net.state_dict(), 'model_param.pkl')
    # print('file loaded!')


    # 绘制混淆矩阵
    y_true = []
    y_pred = []
    net = LSTM(63, 32, 2, 3)
    # 加载参数
    model_param = torch.load('model_param.pkl')
    # 为模型设置参数
    net.load_state_dict(model_param)

    net.eval()
    with torch.no_grad():
        for batch_idx, data in enumerate(testloader):
            # inputs, targets = inputs.to('cpu'), targets.to('cpu')
            inputs = data[:, :, 1:].to(torch.float32).to('cpu')
            print(inputs)
            print(inputs.shape)
            targets = data[:, 0, 0].to(torch.long).to('cpu')
            for target in targets:
                y_true.append(target.numpy())

            # outputs = net(torch.squeeze(inputs, 1))
            outputs = net(inputs)
            _, predicted = outputs.max(1)
            for output in predicted:
                y_pred.append(output.numpy())

    # print(y_true)
    # print(y_pred)
    C = confusion_matrix(y_true, y_pred)

    plt.imshow(C, cmap=plt.cm.Blues)


    plt.show()

