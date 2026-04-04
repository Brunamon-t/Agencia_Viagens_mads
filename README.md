# Agência de Viagens (MADS)

## Enquadramento
Este repositório contém um módulo em Python para **gestão logística de viagens**, desenvolvido no contexto da unidade curricular de MADS (UMaia). O objetivo é disponibilizar um conjunto de funções simples para:

- **Registar viagens** com validações essenciais.
- **Analisar o histórico** (destinos mais frequentes e custos).
- **Filtrar viagens por período**.
- **Apoiar visualização geográfica** (mapa/rotas) de forma opcional.

## Funcionalidades (Histórias de Utilizador)
As funcionalidades implementadas seguem as histórias de utilizador definidas no diário de bordo:

- **HU01 — Registo de viagem**
  - Registo de viagens com validação do meio de transporte e consistência de datas.
  - Cálculo do custo total com base nos custos parciais.

- **HU02 — Análise de destinos frequentes**
  - Contabilização e ordenação dos destinos mais visitados.

- **HU03 — Comparação/visão de custos**
  - Soma do custo total e cálculo de métricas (ex.: custo médio por transporte).

- **HU04 — Filtros cronológicos**
  - Filtragem do histórico por intervalo temporal.

- **HU05 / P4 — Geolocalização e mapa (opcional)**
  - Cálculo de distâncias entre cidades (quando existem coordenadas conhecidas).
  - Geração de um ficheiro HTML com um mapa das rotas (requer `folium`).

## Estrutura do repositório
- **`agencia_de_viagens/`**
  - `agencia_viagens.py`: registo, validações, análise e filtros.
  - `geolocalizacao.py`: coordenadas, distância e mapa (opcional).
  - `__init__.py`: expõe funções principais para importação.
- **`setup.py`**: configuração do empacotamento/instalação.
- **`LICENSE`**: licença estilo MIT.

## Requisitos
- **Python**: 3.8+
- **Dependências principais** (instaladas automaticamente via `setup.py`):
  - `pandas`
- **Dependência opcional (mapa)**:
  - `folium` (apenas necessária para gerar mapa HTML)

## Instalação
Tens duas opções comuns:

### Opção A — Instalação local (a partir do repositório)
No diretório do projeto:

```bash
pip install -e .
```

### Opção B — Instalação direta do GitHub
(Útil para testes rápidos)

```bash
pip install git+https://github.com/Brunamon-t/Agencia_Viagens_mads.git
```

## Exemplo de utilização
O módulo usa um `pandas.DataFrame` como estrutura de dados principal.

```python
from agencia_de_viagens import adicionar_viagem, destinos_mais_frequentes, calcular_custo_total, filtrar_por_periodo
from agencia_de_viagens.agencia_viagens import inicializar_sistema

df = inicializar_sistema()

viagem = {
    "user_id": 1,
    "origem": "Porto",
    "destino": "Lisboa",
    "transporte": "Avião",
    "custo_transporte": 50.0,
    "custo_alojamento": 120.0,
    "custo_alimentacao": 40.0,
    "data_inicio": "2026-03-01",
    "data_fim": "2026-03-03",
}

df = adicionar_viagem(df, viagem)

print(destinos_mais_frequentes(df))
print("Custo total:", calcular_custo_total(df))

df_periodo = filtrar_por_periodo(df, "2026-03-01", "2026-03-31")
print(df_periodo)
```

### Mapa (opcional)
Para gerar um mapa HTML com rotas, instala `folium`:

```bash
pip install folium
```

Exemplo:

```python
from agencia_de_viagens import gerar_mapa_viagens

gerar_mapa_viagens(df, ficheiro="mapa_viagens.html")
```

## Notas importantes
- **Validação de datas**: o sistema impede viagens onde `data_fim` é anterior a `data_inicio`.
- **Transportes válidos**: o meio de transporte é validado por uma lista interna.
- **Sobreposição de viagens por utilizador**: o registo pode bloquear viagens sobrepostas no mesmo intervalo temporal para o mesmo `user_id`.

## Licença
Este projeto é distribuído sob a **Licença MIT**. Consulta o ficheiro `LICENSE` para mais detalhes.

## Equipa
- Liliana Gonçalves — A049692
- Bruna Monteiro — A045875
- Hélder Monteiro — A039652
- Racia Atanásio — A045514
