# coding: utf-8
"""
模型转换 ckpt > pb
"""
import os
from nets import model_train as model  # 自己的模型网络
import tensorflow as tf
from tensorflow.saved_model.signature_def_utils import build_signature_def
from tensorflow.saved_model.builder import SavedModelBuilder
from tensorflow.saved_model.utils import build_tensor_info
tf.app.flags.DEFINE_boolean('debug', True, '')
tf.app.flags.DEFINE_string('ckpt_mod_path', "", '')
tf.app.flags.DEFINE_string('save_mod_dir', "./model/crnn", '')

FLAGS = tf.app.flags.FLAGS

def convert():
    # 保存转换好的模型目录
    savedModelDir = FLAGS.save_mod_dir
    # 每次转换都生成一个版本目录
    for i in range(100000, 9999999):
        cur = os.path.join(savedModelDir, str(i))
        if not tf.gfile.Exists(cur):
            savedModelDir = cur
            break

    # 原ckpt模型
    ckptModPath = FLAGS.ckpt_mod_path

    g = tf.Graph()
    with g.as_default():
        # 输入张量
        input_image = tf.placeholder(tf.float32, shape=[None, None, None, 3], name='input_image')
        input_im_info = tf.placeholder(tf.float32, shape=[None, 3], name='input_im_info')
        bbox_pred, _, cls_prob = model.model(input_image)

        global_step = tf.get_variable('global_step', [], initializer=tf.constant_initializer(0), trainable=False)
        variable_averages = tf.train.ExponentialMovingAverage(0.997, global_step)
        saver = tf.train.Saver(variable_averages.variables_to_restore())
        session = tf.Session(graph=g)
        saver.restore(sess=session, save_path=ckptModPath)

        # 保存转换训练好的模型
        builder = SavedModelBuilder(savedModelDir)
        inputs = {
            "input_image": build_tensor_info(input_image),
            "input_im_info": build_tensor_info(input_im_info)
        }
        # model > classes 是模型的输出， 预测的时候就是这个输出
        output = {
            "output_bbox_pred":build_tensor_info(bbox_pred),
            "output_cls_prob": build_tensor_info(cls_prob)
        }
        prediction_signature = build_signature_def(
            inputs=inputs,
            outputs=output,
            method_name=tf.saved_model.signature_constants.PREDICT_METHOD_NAME
        )
        builder.add_meta_graph_and_variables(
            sess=session,
            tags=[tf.saved_model.tag_constants.SERVING],
            signature_def_map={tf.saved_model.DEFAULT_SERVING_SIGNATURE_DEF_KEY: prediction_signature}
        )
        builder.save()


if __name__ == '__main__':
    convert()
