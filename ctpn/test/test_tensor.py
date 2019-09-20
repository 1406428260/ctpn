import tensorflow as tf
import numpy as np


def test_tf_split():
    # A = np.array([[1, 2, 3], [4, 5, 6]])
    # print("A shape:")
    # print(A.shape)

    A = np.array([[1, 2, 3], [4, 5, 6]])
    print(A.shape)
    x = tf.split(A,num_or_size_splits=3, axis=1)

    with tf.Session() as sess:
        c = sess.run(x)
        c = np.array(c)
        print(c.shape)
        for ele in c:
            print(ele)


test_tf_split()