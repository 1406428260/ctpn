from setuptools import setup,find_packages
import numpy as np
from Cython.Build import cythonize
from setuptools.extension import Extension

setup(
	name="ctpn",
	version="1.0",
	description="ocr ctpn module",
	author="piginzoo",
	url="http://www.piginzoo.com",
	license="LGPL",
	platforms="posix",
	packages=find_packages(where='.', exclude=(), include=('*',))
)

numpy_include = np.get_include()

extensions1 = [
    Extension(
        "ctpn_bbox.bbox",
        ["ctpn/utils/bbox/bbox.pyx"],
		include_dirs=[numpy_include])
]
setup(name="ctpn_bbox",
	  version="1.0",
	  description="ocr ctpn module",
	  author="piginzoo",
	  url="http://www.piginzoo.com",
	  license="LGPL",
	  ext_modules=cythonize(extensions1))

extensions2 = [
    Extension(
        "ctpn_bbox.nms",
        ["ctpn/utils/bbox/nms.pyx"],
		include_dirs=[numpy_include])
]
setup(name="ctpn_bbox",
	  version="1.0",
	  description="ocr ctpn module",
	  author="piginzoo",
	  url="http://www.piginzoo.com",
	  license="LGPL",
	  ext_modules=cythonize(extensions2))









# setup(name="ctpn",
# 	  version="1.0",
# 	  description="ocr ctpn module",
# 	  author="piginzoo",
# 	  url="http://www.piginzoo.com",
# 	  license="LGPL",
# 	  platforms="posix",
# 	  ext_modules=cythonize("ctpn/utils/bbox/bbox.pyx"),
# 	  include_dirs=[numpy_include])
# setup(name="ctpn",
# 	  version="1.0",
# 	  description="ocr ctpn module",
# 	  author="piginzoo",
# 	  url="http://www.piginzoo.com",
# 	  license="LGPL",
# 	  platforms="posix",
# 	  ext_modules=cythonize("ctpn/utils/bbox/nms.pyx"),
# 	  include_dirs=[numpy_include])
