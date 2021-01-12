from setuptools import setup

VERSION = '1.10.1'

def readme():
    with open("README.md") as file:
        return file.read()

setup(
    name="aws-sg",
    version=VERSION,
    description="Allows activities directly in your AWS securities groups",
    long_description_content_type="text/makrdown",
    long_description=readme(),
    keywords="Amazon AWS security-group cloud",
    url="https://github.com/danilocgsilva/aws-sg",
    author="Danilo Silva",
    author_email="contact@danilocgsilva.me",
    packages=["awssg"],
    entry_points={"console_scripts": ["awssg=awssg.__main__:main"],},
    include_package_data=True
)
