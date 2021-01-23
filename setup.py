from setuptools import setup, find_packages

setup(name='trvo_utils',
      version='0.1.2',
      description='Series of functions i found useful',
      url='https://github.com/Trevol/trvo_utils',
      author='Trevol',
      author_email='iamvovan@mail.ru',
      license='MIT',
      packages=find_packages(exclude=["tests"]),
      install_requires=[
          'numpy', 'scikit-image', 'opencv-python'
      ],
      zip_safe=False)
