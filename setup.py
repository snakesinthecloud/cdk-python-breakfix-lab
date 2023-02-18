import setuptools

with open("README.md") as fp:
    long_description = fp.read()


setuptools.setup(
    name="cdk_python_breakfix",
    version="0.0.1",
    description="CDK Breakfix Labs.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Erik HOrton",
    package_dir={"": "stacks/"},
    packages=setuptools.find_packages(where="cdk_"),
    install_requires=[
        "aws-cdk-lib>=2.0.0",
        "constructs>=10.0.0",
    ],
    python_requires=">=3.9",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development :: Code Generators",
        "Topic :: Utilities",
        "Typing :: Typed",
    ],
)
