# Lint as: python3
from pathlib import Path

from setuptools import find_packages, setup


README_TEXT = (Path(__file__).parent / "README.md").read_text(encoding="utf-8")

MAINTAINER = "Esraa Madi, Saud Altamimi"

INTEGRATIONS_REQUIRE = ["optuna"]
REQUIRED_PKGS = ["datasets>=2.3.0", "sentence-transformers>=2.2.1", "evaluate>=0.3.0"]
QUALITY_REQUIRE = ["black", "flake8", "isort", "tabulate"]
TESTS_REQUIRE = ["pytest", "pytest-cov"]


setup(
    name="biomerida",
    version="0.0.1",
    description="Efficient few-shot learning with Bio Transformers",
    long_description=README_TEXT,
    long_description_content_type="text/markdown",
    maintainer=MAINTAINER,
    package_dir={"": "src"},
    packages=find_packages("src"),
    install_requires=REQUIRED_PKGS,
    keywords="bioinformatics, machine learning, fewshot learning, transformers",
)