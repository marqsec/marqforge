import os
from setuptools import setup

readme_path = os.path.join(os.path.dirname(__file__), "README.md")
long_description = ""
if os.path.exists(readme_path):
    with open(readme_path, encoding="utf-8") as f:
        long_description = f.read()

setup(
    name="marqforge",
    use_scm_version={
        "local_scheme": "no-local-version", 
        "write_to": "metadata/git_version.py",
    },
    setup_requires=["setuptools_scm"],
    
    author="Marq (MarqSec)",
    author_email="marqlinux@gmail.com",
    description="Modular web security discovery framework",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    
    url="https://github.com",
    project_urls={
        "Repository": "https://github.com",
        "Bug Tracker": "https://github.com/issues",
        "Documentation": "https://marqforge.readthedocs.io",
    },
    
    packages=[
        "marqforge",
    ],
    package_dir={
        "marqforge": "metadata"
    },
    
    python_requires=">=3.8",
    install_requires=[
        # "requests>=2.31.0",
        # "urllib3>=2.0.0",
    ],
    
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Information Technology",
        "Intended Audience :: System Administrators",
        "Topic :: Security",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
)
