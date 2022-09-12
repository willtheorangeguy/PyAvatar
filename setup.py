from setuptools import setup, find_packages

def readme():
    with open('README.md') as f:
        return f.read()

setup(
	name='py-avatar',
	version='0.2.0',
    description="Easily display all of your creative avatars to keep them consistent across websites.",
    long_description=readme(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Topic :: Utilities',
    ],
    keywords='avatar web accounts gui',
    url='https://github.com/Dog-Face-Development/PyAvatar',
    author='willtheorangeguy',
    packages=find_packages(where="PyAvatar"),
    package_dir={"": "PyAvatar"},
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'pyavatar=main:avatars'
        ]
    },
)
