from setuptools import setup, find_packages

import django_postgres_extensions

setup(name='django_postgres_extensions',
    version=django_postgres_extensions.__version__,
    description="Extra features for django.contrib.postgres update for django 3",
    long_description=open('description.rst').read(),
    author='Parth Verma',
    author_email='v.parth98@gmail.com',
    url='https://github.com/primal100/django_postgres_extensions',
    packages=find_packages(exclude=['tests', 'tests.*']),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Database',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
      install_requires=["django>=3.0.0"],
    python_requires='>=3.5'
)