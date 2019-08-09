import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='hello',
    version='0.2.6',
    author='John',
    author_email='jlarson@idbydna.com',
    description='Says \'Hello, World\'.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/johnlarson/hello_conda',
    packages=setuptools.find_packages(),
    install_requires=[
        'numpy==1.17.0',
        'sympy==1.4',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
