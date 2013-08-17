#!/usr/bin/env python

from distutils.core import setup

setup(name='kakaotalk',
      version='1.1.0',
      description='python wrapper for LOCO protaol of KakaoTalk',
      author='Taehoon Kim',
      author_email='carpedm20@gmail.com',
      url='http://carpedm20.blogspot.kr/',
      packages=['kakaotalk'],
      install_requires=[
        "pymongo >= 2.5.2",
        "rsa >= 3.1.1",
        "pycrypto >= 2.6",
      ],
     )
