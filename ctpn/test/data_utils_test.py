import unittest
import numpy as np
from utils.prepare import utils

class TestDict(unittest.TestCase):

    def test_init(self):
        pass

    def test_resize_image_1(self):
        #会按照宽来调整，因为宽的比较大
        # w=2346,h=1001
        mock_image = np.zeros([1001,2345,3],np.uint8) # H,W,C
        image,scale = utils.resize_image(mock_image,2000,1001) # w=2000 , h= 1001
        _scale = 2000/2345
        self.assertEquals(_scale,scale)
        self.assertEquals(list(image.shape[:2]),[round(scale*1001),round(scale*2345)])

    def test_resize_image_2(self):
        #会按照宽来调整，因为宽的比较大
        # w=2001,h=1234
        mock_image = np.zeros([1234,2001,3],np.uint8) # H,W,C
        image,scale = utils.resize_image(mock_image,2000,1000) # w=2000 , h= 1000
        _scale = 1000/1234
        self.assertEquals(_scale,scale)
        self.assertEquals(list(image.shape[:2]),[round(scale*1234),round(scale*2000)+1])

    def test_resize_image_2(self):
        #会按照宽来调整，因为宽的比较大
        # w=2001,h=1234
        mock_image = np.zeros([1000,2000,3],np.uint8) # H,W,C
        image,scale = utils.resize_image(mock_image,2100,1100)
        self.assertEquals(1,scale)
        self.assertEquals(list(image.shape[:2]),[1000,2000])

    def test_resize_labels(self):
        labels = np.ones([2,4]).tolist()
        resized_labels = utils.resize_labels(labels,1)
        self.assertEquals(labels,resized_labels)

        resized_labels = utils.resize_labels(labels,0.2)
        target_labels = [[0.2,0.2,0.2,0.2],[0.2,0.2,0.2,0.2]]
        self.assertEquals(target_labels,resized_labels)


if __name__ == '__main__':
    unittest.main()
