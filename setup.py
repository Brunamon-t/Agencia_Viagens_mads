from setuptools import setup, find_packages

setup(
    name="agencia-viagens-mads-2026-v-final-total", # NOME NOVO
    version="1.1.0",                                # VERSÃO NOVA
    description="Sistema de gestão de viagens",
    long_description="Sistema de gestão de viagens com validação de custos e geolocalização",
    long_description_content_type="text/plain",     # MAIS SIMPLES
    author="Bruna Monteiro, Helder Monteiro, Liliana Gonçalves, Rácia Atanásio",
    author_email="A045875@ipmaia.pt",
    url="https://github.com/Brunamon-t/Agencia_Viagens_mads",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "pandas>=2.0.0",
        "geopy>=2.3.0",
    ],
    python_requires=">=3.8",
)
