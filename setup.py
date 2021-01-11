import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cryptozys-krajzys", # Replace with your own username
    version="0.0.1",
    author="Krajzys",
    author_email="kryzyyspl@gmail.com",
    description="My package for playing with cryptography",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Krajzys/CryptoZys",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)