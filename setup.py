from setuptools import setup

setup(
    name         = 'migemo',
    version      = '0.2.0',
    description  = 'Python Binding for Migemo',
    author       = 'Kazuya Takeshima',
    author_email = 'mail@mitukiii.jp',
    license      = 'MIT',
    url          = 'https://github.com/mitukiii/migemo-python',
    test_suite   = 'migemo.test',
    packages = [
        'migemo',
    ],
    install_requires = [
        'cffi',
    ],
    classifiers = [
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Topic :: Text Processing',
    ]
)
