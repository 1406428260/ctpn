import numpy as np

gt = 10
anchor = 100

gt_data = np.random.randint(10,1000,size=[gt])

data = np.random.randint(10,1000,size=[anchor,gt])

print(data.shape)

argmax = np.argmax(data,axis=1)
gt_argmax = np.argmax(data,axis=0)

print("argmax,axis=1 [anchor,gt]=[100,10]")
print(argmax.shape)
print(argmax)

print("gt_argmax,axis=0 [anchor,gt]=[100,10]")
print(gt_argmax.shape)
print(gt_argmax)


print("gt_data")
print(gt_data)

# 可以神奇的把gt的数组扩大了，给撑大了
print("gt_data[argmax]")
print(gt_data[argmax])

# 测试一下统计信息
data = np.random.random(1000)
def stat(data):
    return "mean={},std={},max={},min={},0={}".format(
        data.mean(),
        data.std(),
        data.max(),
        data.min(),
        (data==0).sum())

print(stat(data))

print("----------")

overlaps = np.array(
    [
        [1, 2,  3],
        [4, 5,  6],
        [7, 15, 16],
        [14,11, 12],
        [14,15, 16],
    ]

)
print("overlap shape:",overlaps.shape)
gt_argmax_overlaps = overlaps.argmax(axis=0)  # G#找到每个位置上9个anchor中与gtbox，overlap最大的那个
print("gt_argmax_overlaps:",gt_argmax_overlaps)
gt_max_overlaps = overlaps[gt_argmax_overlaps,
                           np.arange(overlaps.shape[1])]
print("gt_max_overlaps:",gt_max_overlaps)
gt_argmax_overlaps = np.where(overlaps == gt_max_overlaps)[0]
print("gt_argmax_overlaps",gt_argmax_overlaps)
