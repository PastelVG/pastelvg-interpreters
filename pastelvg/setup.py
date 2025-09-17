from setuptools import setup

setup(
    name="pastelvg",
    version="0.1.0",
    py_modules=["pastelvg_interpreter", "pastelvg_cli"],
    install_requires=[],
    entry_points={
        "console_scripts": [
            "pastelvg = pastelvg_cli:main"
        ]
    },
    author="Aeon Development Group",
    description="A CLI interpreter for converting SVG to PastelVG JSON",
    license="Apache 2.0",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License"
    ],
    python_requires=">=3.7",
)
