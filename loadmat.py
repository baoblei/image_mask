#coding:UTF-8
 
import scipy.io as scio
 
dataFile = './matlab.mat'
data = scio.loadmat(dataFile)
# print(type(data))
# print(data)
workspace = data['None']['s0']
print(workspace.item)