from setuptools import setup

version = open("version", 'r').read().removesuffix("\n")

setup(
    name='thehsi',
    version=version,
    packages=['thehsi'],
    license='MIT',
    description='A Python Package for coding a custom TheHSI Hub integrated Application',
    author='TheHSI',
    author_email='central.thehsi@gmail.com',
    url='https://github.com/hstoreinteractive/thehsi-python',
    download_url=f'https://github.com/hstoreinteractive/thehsi-python/archive/refs/tags/v{version}.tar.gz',
    keywords=['thehsi', 'application'],
    install_requires=[
        'requests'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.12',
    ],
)
