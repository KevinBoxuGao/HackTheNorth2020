from distutils.core import setup

setup(name="PyExifTool",
      version="0.1",
      description="Python wrapper for exiftool",
      license="GPLv3+",
      author="Sven Marnach",
      author_email="sven@marnach.net",
      url="http://github.com/smarnach/pyexiftool",
      classifiers=[
          "Development Status :: 3 - Alpha",
          "Intended Audience :: Developers",
          "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
          "Programming Language :: Python :: 2.6",
          "Programming Language :: Python :: 2.7",
          "Programming Language :: Python :: 3",
          "Topic :: Multimedia"],
      py_modules=["exiftool"])
