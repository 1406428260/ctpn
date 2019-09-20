import tensorflow as tf

str1 = "hello"
str2 = "my name is liu, i came from China"

x1 = tf.convert_to_tensor(str1, dtype=tf.string)
x2 = tf.convert_to_tensor(str2, dtype=tf.string)

with tf.Session() as sess:
    c1,c2 = sess.run([x1,x2])
    print(c1)
    print(c2)
    print(type(c2))