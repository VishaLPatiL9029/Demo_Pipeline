from setuptools import setup, find_packages

setup(name="census-income",
    version ='0.0.1',
    author = 'Sunny',
    author_email='Sunny.savita@ineuron.ai',
    packages= find_packages(),
    install_requires = ["pandas","numpy","flask"]
    )