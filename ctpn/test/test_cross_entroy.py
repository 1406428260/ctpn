import tensorflow as tf

y     = tf.convert_to_tensor([2,2],           dtype=tf.int64)
y_hat = tf.convert_to_tensor([[-2.6, -1.7, 3.2, 0.1],[-2.6, -1.7, 3.2, 0.1]], dtype=tf.float32)
c = tf.nn.sparse_softmax_cross_entropy_with_logits(labels=y,logits=y_hat)

# [1,1]实际上是表示了俩标签
# 第一个1，是说，二分类里面，我选第二个，index=1
y     = tf.convert_to_tensor([1,1],           dtype=tf.int64)
y_hat = tf.convert_to_tensor([[0.1, 99],[2.6,1.7]], dtype=tf.float32)
c2 = tf.nn.sparse_softmax_cross_entropy_with_logits(labels=y,logits=y_hat)


with tf.Session() as sess:
  print ('交叉熵为: %r' % sess.run(c))
  print ('交叉熵为: %r' % sess.run(c2))
