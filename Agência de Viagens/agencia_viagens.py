# -*- coding: utf-8 -*-
import pandas as pd

TRANSPORTES_VALIDOS = ["Avião", "Comboio", "Autocarro", "Carro", "Barco", "Bicicleta"]

def inicializar_sistema():
    """Cria a estrutura base do DataFrame para evitar erros de variável não definida."""
    return pd.DataFrame(columns=[
        "user_id", "origem", "destino", "transporte", 
        "custo_transporte", "custo_alojamento", "custo_alimentacao", 
        "custo_total", "data_inicio", "data_fim"
    ])

# HU01: Registo de Viagem com Validação e Cálculo de Custos
def adicionar_viagem(df, viagem_dict):
    if viagem_dict["transporte"] not in TRANSPORTES_VALIDOS:
        raise ValueError(f"Transporte inválido. Escolha entre: {TRANSPORTES_VALIDOS}")

    # Cálculo do Custo Total (HU03)
    viagem_dict["custo_total"] = (
        viagem_dict.get("custo_transporte", 0) + 
        viagem_dict.get("custo_alojamento", 0) + 
        viagem_dict.get("custo_alimentacao", 0)
    )

    inicio_nova = pd.to_datetime(viagem_dict["data_inicio"])
    fim_nova = pd.to_datetime(viagem_dict["data_fim"])

    if fim_nova < inicio_nova:
        raise ValueError("A data de fim não pode ser anterior à data de início.")

    viagens_utilizador = df[df["user_id"] == viagem_dict["user_id"]].copy()
    if not viagens_utilizador.empty:
        viagens_utilizador["data_inicio"] = pd.to_datetime(viagens_utilizador["data_inicio"])
        viagens_utilizador["data_fim"] = pd.to_datetime(viagens_utilizador["data_fim"])

        sobreposicao = viagens_utilizador[
            (inicio_nova <= viagens_utilizador["data_fim"]) & 
            (fim_nova >= viagens_utilizador["data_inicio"])
        ]

        if not sobreposicao.empty:
            raise ValueError(f"Erro: O utilizador {viagem_dict['user_id']} já tem uma viagem neste período!")

    return pd.concat([df, pd.DataFrame([viagem_dict])], ignore_index=True)

# HU02: Análise de Destinos
def destinos_mais_frequentes(df):
    return df["destino"].value_counts()

# HU03: Funções de Custos
def calcular_custo_total(df):
    return df["custo_total"].sum()

def custo_medio_por_transporte(df):
    return df.groupby("transporte")["custo_transporte"].mean()

# HU04: Filtro por Período
def filtrar_por_periodo(df, data_inicio, data_fim):
    df_temp = df.copy()
    df_temp["data_inicio"] = pd.to_datetime(df_temp["data_inicio"])
    inicio = pd.to_datetime(data_inicio)
    fim = pd.to_datetime(data_fim)
    return df_temp[(df_temp["data_inicio"] >= inicio) & (df_temp["data_inicio"] <= fim)]

# Zona de Teste (Não é executada quando importada como pacote)
if __name__ == "__main__":
    viagens = inicializar_sistema() # CRUCIAL: Inicializar antes de usar
    
    v1 = {
        "user_id": 3, "origem": "Porto", "destino": "Lisboa", "transporte": "Avião",
        "custo_transporte": 50.0, "custo_alojamento": 100.0, "custo_alimentacao": 60.0,
        "data_inicio": "2026-05-01", "data_fim": "2026-05-10"
    }
    
    try:
        viagens = adicionar_viagem(viagens, v1)
        print("Sistema: Viagem 1 registada com sucesso.")
        
        # Teste de bloqueio (v2 sobrepõe v1)
        v2 = {
            "user_id": 3, "origem": "Lisboa", "destino": "Faro", "transporte": "Comboio",
            "custo_transporte": 20.0, "custo_alojamento": 40.0, "custo_alimentacao": 30.0,
            "data_inicio": "2026-05-05", "data_fim": "2026-05-15"
        }
        viagens = adicionar_viagem(viagens, v2)
    except ValueError as e:
        print(f"Bloqueio de segurança: {e}")

    print("\n--- Estado Atual das Viagens ---")
    print(viagens)
