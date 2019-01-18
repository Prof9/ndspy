import setuptools

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='ndspy',
    version='1.0.0',
    author='RoadrunnerWMC',
    author_email='roadrunnerwmc@gmail.com',
    description='ndspy is a Python library and suite of command-line tools that can help you read, modify and create many types of files used in Nintendo DS games.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/RoadrunnerWMC/ndspy',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Operating System :: OS Independent',
    ],
)