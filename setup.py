from setuptools import setup

setup(
    # Other setup arguments...
    entry_points={
        'console_scripts': [
            'test = test.dialoget:update_repo_on_github2',
        ],
    },
)