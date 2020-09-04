from setuptools import setup


setup(
    name="ktlint",
    version="0.0.0",
    packages=["lint"],
    install_requires=["requests"],
    entry_points={
        'console_scripts': [
            'ktlint = lint.ktlint:run_ktlint',
        ],
    },
)