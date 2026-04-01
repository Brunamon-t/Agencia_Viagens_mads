# P4 - Geolocalizacao das viagens
# Visualizacao geografica dos destinos num mapa

import math
import pandas as pd

# Coordenadas de algumas cidades portuguesas (lat, lon)
COORDENADAS_CIDADES = {
    "Lisboa": (38.7369, -9.1427),
    "Porto": (41.1496, -8.6110),
    "Faro": (37.0194, -7.9304),
    "Coimbra": (40.2056, -8.4196),
    "Braga": (41.5454, -8.4265),
    "Aveiro": (40.6405, -8.6538),
    "Evora": (38.5667, -7.9000),
    "Funchal": (32.6669, -16.9241),
    "Leiria": (39.7444, -8.8073),
    "Setubal": (38.5244, -8.8882),
    "Viseu": (40.6500, -7.9167),
    "Madeira": (32.6669, -16.9241),
}

# Procurar coordenadas de uma cidade
def obter_coordenadas(cidade):
  return COORDENADAS_CIDADES.get(cidade, None)

# Calcular distancia entre dois pontos (formula de Haversine)
def calcular_distancia(lat1, lon1, lat2, lon2):
  R = 6371
  dlat = math.radians(lat2 - lat1)
  dlon = math.radians(lon2 - lon1)
  a = (math.sin(dlat / 2) ** 2 +
       math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2) ** 2)
  c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
  return round(R * c, 2)

# Calcular distancia entre duas cidades pelo nome
def distancia_viagem(origem, destino):
  coords_o = obter_coordenadas(origem)
  coords_d = obter_coordenadas(destino)
  if coords_o is None or coords_d is None:
    return None
  return calcular_distancia(coords_o[0], coords_o[1], coords_d[0], coords_d[1])

# Gerar mapa com as rotas das viagens (precisa do folium: pip install folium)
def gerar_mapa_viagens(df, ficheiro="mapa_viagens.html"):
  import folium
  mapa = folium.Map(location=[39.5, -8.0], zoom_start=7)

  for _, viagem in df.iterrows():
    coords_o = obter_coordenadas(viagem["origem"])
    coords_d = obter_coordenadas(viagem["destino"])
    if coords_o is None or coords_d is None:
      continue

    # marcador origem (verde) e destino (vermelho)
    folium.Marker(location=coords_o, popup=viagem["origem"],
                  icon=folium.Icon(color="green")).add_to(mapa)
    folium.Marker(location=coords_d, popup=viagem["destino"],
                  icon=folium.Icon(color="red")).add_to(mapa)

    # linha da rota
    folium.PolyLine(locations=[coords_o, coords_d], color="blue", weight=2).add_to(mapa)

  mapa.save(ficheiro)
  print(f"Mapa guardado em: {ficheiro}")
  return mapa


#Zona de Teste

dist = distancia_viagem("Porto", "Lisboa")
print(f"Distancia Porto -> Lisboa: {dist} km")

dist2 = distancia_viagem("Lisboa", "Faro")
print(f"Distancia Lisboa -> Faro: {dist2} km")

coords = obter_coordenadas("Porto")
print(f"Coordenadas do Porto: {coords}")
