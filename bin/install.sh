echo "将CTPN安装到本地"
python setup.py install
python setup.py clean --all
rm -rf ctpn.egg-info ctpn_bbox.egg-info dist