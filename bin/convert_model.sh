#!/usr/bin/env bash

echo "模型转换: 从ckpt转成pb"

ckpt_mod_path=$1
save_mod_dir=$2

if [ "$ckpt_mod_path" = "" ]; then
    echo "ckpt模型目录不能为空: conver_model <原始模型的名称> <目标pb模型的生成目录>"
    echo "例："
    echo "  convert_model.sh /app.fast/projects/models/ctpn-2019-05-28-22-32-39-2901.ckpt ./model"
    exit
fi

if [ "$save_mod_dir" = "" ]; then
    echo "ckpt模型目录不能为空: conver_model <原始模型的名称> <目标pb模型的生成目录>"
    exit
fi

python -m utils.convert_model \
    --ckpt_mod_path=$ckpt_mod_path \
    --save_mod_dir=$save_mod_dir \
    --charset=charset.3770.txt