from setuptools import setup, find_packages

setup(
    name='django-userprofile',
    version='0.0.5',
    description='Django user profile app.',
    long_description = open('README.rst', 'r').read() + open('AUTHORS.rst', 'r').read() + open('CHANGELOG.rst', 'r').read(),
    author='Praekelt Foundation',
    author_email='dev@praekelt.com',
    license='BSD',
    url='http://github.com/praekelt/django-userprofile',
    packages = find_packages(),
    dependency_links = [
        'http://github.com/praekelt/django-photologue/tarball/master#egg=django-photologue',
    ],
    install_requires = [
        'django-photologue',
        'django-registration',
    ],
    tests_require=[
        'django-setuptest>=0.0.6',
    ],
    test_suite="setuptest.SetupTestSuite",
    include_package_data=True,
    classifiers = [
        "Programming Language :: Python",
        "License :: OSI Approved :: BSD License",
        "Development Status :: 4 - Beta",
        "Operating System :: OS Independent",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    zip_safe=False,
)
