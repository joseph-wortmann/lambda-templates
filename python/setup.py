# To use a consistent encoding
from codecs import open
from os import path
from setuptools import setup, find_packages, Command


here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as readme:
    long_description = readme.read()

# TODO: Change the following variables to match your lambda function
lambda_name = 'example-lambda'

# Versions should comply with PEP440.  For a discussion on single-sourcing
# the version across setup.py and the project code, see
# https://packaging.python.org/en/latest/single_source_version.html
# TODO: Update the version number
lambda_version = '0.0.1'

# TODO: Change the description
lambda_description = 'A template lambda project'

# How mature is this project? Common values are
#   3 - Alpha
#   4 - Beta
#   5 - Production/Stable
# TODO: Change your project status
lambda_dev_status = '3 - Alpha'

# What does your project relate to?
# TODO: Add keywords
lambda_keywords = ''

# What is your project's license
# TODO: Change your project's license
lambda_license = ''

# Who is the author?
# TODO: Update the author
lambda_author=''
lambda_author_email=''

# List run-time dependencies here.  These will be installed by pip when
# your project is installed. For an analysis of "install_requires" vs pip's
# requirements files see:
# https://packaging.python.org/en/latest/requirements.html
# TODO: List the install requirements of the lambda function
lambda_install_requires = []

##############################################
# CHANGES BELOW HERE ARE MADE AT YOUR OWN RISK
##############################################

setup(
    name=lambda_name,

    version=lambda_version,

    description=lambda_description,
    long_description=long_description,

    author=lambda_author,
    author_email=lambda_author_email,

    # Choose your license
    license=lambda_license,

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: '+lambda_dev_status,

        # Pick your license as you wish (should match "license" above)
        'License :: '+lambda_license,

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2.7',
    ],

    keywords=lambda_keywords,

    install_requires=filter(lambda x : x not in ['boto3', 'botocore'], lambda_install_requires),

    package_dir={'': 'src'},
    packages=find_packages('src'),

    include_package_data=True,

    lambda_package='src/lambda_function',

    setup_requires=['lambda-setuptools'],
)
