# 测试调用cython写的nms.so

import ctpn.utils.bbox.nms as nms
import ctpn.utils.bbox.bbox as bbox_overlaps
import numpy as np
print(bbox_overlaps)
print (nms.nms(np.random.rand([20,20]),None))