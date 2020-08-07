from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="pyreview",
    version="0.0.8",
    description="Deploy tool for Heroku Review App using Bitbucket Pipelines",
    long_description=long_description,
    url="https://github.com/franciscoafonsoo/pyreview",
    author="Francisco Pires",
    author_email="f.pires.dev@icloud.com",
    license="gpl-3.0",
    packages=["pyreview"],
    install_requires=["requests", "python-dotenv"],
    entry_points={"console_scripts": ["pyra=pyreview.__main__:main"]},
    zip_safe=False,
    python_requires=">=3.6",
)