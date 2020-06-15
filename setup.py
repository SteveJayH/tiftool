from setuptools import setup, find_packages

with open('README.md') as f:
    long_description = f.read()

setup(
    name = 'tiftool',
    version = '0.1.9',
    description = 'tiftool',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    author = 'Seungjae',
    author_email = 'jay0118@yonsei.ac.kr',
    url = 'https://github.com/SteveJayH/tiftool',
    download_url = 'https://api.github.com/repos/SteveJayH/tiftool/tarball',
    install_requires = ['tifffile', 'Pillow', 'numpy', 'matplotlib', 'torch'],  # TODO
    packages = find_packages(exclude = []),
    keywords = ['tiftool', 'tiff', 'microscopy'],  # TODO
    python_requires = '>=3',
    package_data = {},
    zip_safe = False,
    classifiers = [
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)