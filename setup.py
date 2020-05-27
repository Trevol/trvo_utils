from setuptools import setup

setup(name='trvo_utils',
      version='0.1',
      description='Series of functions i found useful',
      url='https://github.com/Trevol/trvo_utils',
      author='Trevol',
      author_email='iamvovan@mail.ru',
      license='MIT',
      packages=['trvo_utils', 'trvo_utils.voc_annotation'],
      install_requires=[
          'numpy', 'scikit-image', 'opencv-python'
      ],
      zip_safe=False)
