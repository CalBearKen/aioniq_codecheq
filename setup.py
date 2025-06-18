from setuptools import setup, find_packages

setup(
    name="codecheq",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "setuptools>=61.0.0",
        "openai>=1.0.0",
        "anthropic>=0.5.0",
        "pydantic>=2.0.0",
        "rich>=13.0.0",
        "typer>=0.9.0",
        "python-dotenv>=1.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "black>=23.0.0",
            "isort>=5.0.0",
            "mypy>=1.0.0",
            "ruff>=0.1.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "codecheq=codecheq.cli.main:app",
        ],
    },
    python_requires=">=3.8",
    scripts=["run_codecheq.py"],
) 