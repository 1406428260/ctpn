# coding: utf-8
"""
模型转换 ckpt > pb
"""
import os

import tensorflow as tf

from nets import model  # 自己的模型网络

tf.app.flags.DEFINE_boolean('debug', False, '')


def convert():
    # 保存转换好的模型目录
    savedModelDir = "./model_name"
    # 每次转换都生成一个版本目录
    for i in range(100000, 9999999):
        cur = os.path.join(savedModelDir, str(i))
        if not tf.gfile.Exists(cur):
            savedModelDir = cur
            break
    # 原ckpt模型
    savePath = "../../model/ctpn-2019-08-14-15-14-05-2.ckpt"
    # 输入张量
    ph_input_image = tf.placeholder(tf.float32, shape=[None, None, None, 3], name='ph_input_image')
    _, classes = model.model(ph_input_image)
    print(classes)
    session = tf.Session()
    session.run(tf.global_variables_initializer())
    saver = tf.train.Saver()
    saver.restore(sess=session, save_path=savePath)

    # 保存转换训练好的模型
    builder = tf.saved_model.builder.SavedModelBuilder(savedModelDir)
    inputs = {
        # ph_input_image 就是模型里面定义的输入placeholder
        "input": tf.saved_model.utils.build_tensor_info(ph_input_image)
    }
    # model > classes 是模型的输出， 预测的时候就是这个输出
    output = {"output": tf.saved_model.utils.build_tensor_info(classes)}
    prediction_signature = tf.saved_model.signature_def_utils.build_signature_def(
        inputs=inputs,
        outputs=output,
        method_name=tf.saved_model.signature_constants.PREDICT_METHOD_NAME
    )
    builder.add_meta_graph_and_variables(
        session,
        [tf.saved_model.tag_constants.SERVING],
        {tf.saved_model.signature_constants.DEFAULT_SERVING_SIGNATURE_DEF_KEY: prediction_signature}
    )
    builder.save()


if __name__ == '__main__':
    convert()