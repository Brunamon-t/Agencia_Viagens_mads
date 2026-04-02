from pathlib import Path
from setuptools import find_packages, setup

# Define o diretório base e lê o README para a descrição longa
BASE_DIR = Path(__file__).parent.resolve()
README = (BASE_DIR / "README.md").read_text(encoding="utf-8")

setup(
    name="agencia-viagens-mads-grupo4", 
    version="1.0.0",
    description="Sistema de gestão de viagens com validação de custos e geolocalização",
    long_description=README,
    long_description_content_type="text/markdown",
    
    # Lista de todos os autores do grupo
    author="Bruna Monteiro, Helder Monteiro, Liliana Gonçalves, Rácia Atanásio",
    author_email="A045875@ipmaia.pt",
    url="https://github.com/agencia-viagens-mads",
    
    project_urls={
        "Source": "https://github.com/[teu-utilizador]/agencia-viagens-mads",
        "Issues": "https://github.com/[teu-utilizador]/agencia-viagens-mads/issues",
    },
    
    packages=find_packages(),
    include_package_data=True,
    python_requires=">=3.8",
    
    # Dependências necessárias para o teu código funcionar
    install_requires=[
        "pandas>=2.0.0",
        "geopy>=2.3.0",
    ],
    
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Scientific/Engineering :: Information Analysis",
    ],
    license="MIT",
    keywords="agencia viagens pandas geopy mads umaia",
)
