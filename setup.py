"""
Setup and installation for the package.
"""

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name="wadsworth",
    version="0.1",
    url="http://github.com/zachwill/wadsworth_constant",
    author="Zach Williams",
    author_email="hey@zachwill.com",
    description="The Wadsworth Constant CLI",
    keywords=['reddit', 'wadsworth constant', 'zachwill'],
    license='MIT',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
    scripts=[
        'wadsworth'
    ]
)
