from setuptools import setup


setup(
    entry_points={
        'console_scripts': [
            'ktlint = lint.ktlint:run_ktlint',
        ],
    },
)