#!/usr/bin/python

from setuptools import setup, find_packages

with open('README.rst') as f:
    long_description = f.read()

setup(packages=find_packages(),
      version='0.1.3',
      maintainer='Mark Levy',
      name='mrec',
      package_dir={'':'.'},
      maintainer_email='mark.levy@mendeley.com',
      description='mrec recommender systems library',
      long_description=long_description,
      url='https://github.com/mendeley/mrec',
      download_url='https://github.com/mendeley/mrec/tarball/master#egg=mrec-0.1.3',
      classifiers=['Development Status :: 4 - Beta',
                   'Environment :: Console',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: Unix',
                   'Programming Language :: Python',
                   'Topic :: Scientific/Engineering',],
      install_requires=['numpy','scipy','scikit-learn','ipython'],
      entry_points={
          'console_scripts':[
              'mrec_prepare = mrec.examples.prepare:main',
              'mrec_train = mrec.examples.train:main',
              'mrec_predict = mrec.examples.predict:main',
              'mrec_evaluate = mrec.examples.evaluate:main',
              'mrec_tune = mrec.examples.tune_slim:main',
              'mrec_convert = mrec.examples.convert:main',
              'mrec_factors = mrec.examples.factors:main',
          ]})
