# Reexecutar tudo após reset do ambiente
import folium
from folium.plugins import HeatMap
import random

# Lista de 20 cidades próximas à capital São Paulo
cidades_sp = [
    "São Paulo", "Guarulhos", "Santo André", "São Bernardo do Campo", "Osasco",
    "Barueri", "Carapicuíba", "Diadema", "Mauá", "Taboão da Serra",
    "Itapevi", "Suzano", "Mogi das Cruzes", "Cotia", "Itapecerica da Serra",
    "Ribeirão Pires", "Caieiras", "Franco da Rocha", "Ferraz de Vasconcelos", "Poá"
]

# Coordenadas aproximadas das cidades
coordenadas = {
    "São Paulo": (-23.55052, -46.63331),
    "Guarulhos": (-23.4545, -46.5333),
    "Santo André": (-23.6737, -46.5436),
    "São Bernardo do Campo": (-23.6914, -46.5646),
    "Osasco": (-23.5329, -46.7917),
    "Barueri": (-23.5057, -46.8798),
    "Carapicuíba": (-23.5226, -46.8356),
    "Diadema": (-23.6816, -46.6205),
    "Mauá": (-23.6677, -46.4613),
    "Taboão da Serra": (-23.6261, -46.7916),
    "Itapevi": (-23.5488, -46.9323),
    "Suzano": (-23.5446, -46.3109),
    "Mogi das Cruzes": (-23.5208, -46.1854),
    "Cotia": (-23.6026, -46.919),
    "Itapecerica da Serra": (-23.7161, -46.8498),
    "Ribeirão Pires": (-23.7073, -46.4058),
    "Caieiras": (-23.3646, -46.7394),
    "Franco da Rocha": (-23.322, -46.729),
    "Ferraz de Vasconcelos": (-23.5411, -46.3694),
    "Poá": (-23.5333, -46.35)
}

# Criar um mapa centrado em São Paulo
mapa = folium.Map(location=[-23.55052, -46.63331], zoom_start=10)

# Criar pontos com dados fictícios de vendas e adicionar ao mapa
heat_data = []
for cidade, coord in coordenadas.items():
    vendas = random.randint(100, 1000)
    folium.Marker(
        location=coord,
        popup=f"{cidade}<br>Vendas: {vendas}",
        tooltip=cidade,
        icon=folium.Icon(color='blue')
    ).add_to(mapa)
    heat_data.append([coord[0], coord[1], vendas])

# Adicionar camada de mapa de calor
HeatMap(heat_data, blur=5, radius=15).add_to(mapa)

# Salvar HTML
caminho_html = "/mnt/data/mapa_lojas_sp.html"
mapa.save(caminho_html)

# Salvar código Python em arquivo
codigo_python = """
import folium
from folium.plugins import HeatMap
import random

cidades_sp = [
    "São Paulo", "Guarulhos", "Santo André", "São Bernardo do Campo", "Osasco",
    "Barueri", "Carapicuíba", "Diadema", "Mauá", "Taboão da Serra",
    "Itapevi", "Suzano", "Mogi das Cruzes", "Cotia", "Itapecerica da Serra",
    "Ribeirão Pires", "Caieiras", "Franco da Rocha", "Ferraz de Vasconcelos", "Poá"
]

coordenadas = {
    "São Paulo": (-23.55052, -46.63331),
    "Guarulhos": (-23.4545, -46.5333),
    "Santo André": (-23.6737, -46.5436),
    "São Bernardo do Campo": (-23.6914, -46.5646),
    "Osasco": (-23.5329, -46.7917),
    "Barueri": (-23.5057, -46.8798),
    "Carapicuíba": (-23.5226, -46.8356),
    "Diadema": (-23.6816, -46.6205),
    "Mauá": (-23.6677, -46.4613),
    "Taboão da Serra": (-23.6261, -46.7916),
    "Itapevi": (-23.5488, -46.9323),
    "Suzano": (-23.5446, -46.3109),
    "Mogi das Cruzes": (-23.5208, -46.1854),
    "Cotia": (-23.6026, -46.919),
    "Itapecerica da Serra": (-23.7161, -46.8498),
    "Ribeirão Pires": (-23.7073, -46.4058),
    "Caieiras": (-23.3646, -46.7394),
    "Franco da Rocha": (-23.322, -46.729),
    "Ferraz de Vasconcelos": (-23.5411, -46.3694),
    "Poá": (-23.5333, -46.35)
}

mapa = folium.Map(location=[-23.55052, -46.63331], zoom_start=10)
heat_data = []
for cidade, coord in coordenadas.items():
    vendas = random.randint(100, 1000)
    folium.Marker(
        location=coord,
        popup=f"{cidade}<br>Vendas: {vendas}",
        tooltip=cidade,
        icon=folium.Icon(color='blue')
    ).add_to(mapa)
    heat_data.append([coord[0], coord[1], vendas])

HeatMap(heat_data, blur=5, radius=15).add_to(mapa)
mapa.save("mapa_lojas_sp.html")
print("Mapa salvo como 'mapa_lojas_sp.html'")
"""

caminho_py = "/mnt/data/gerar_mapa_lojas_sp.py"
with open(caminho_py, "w") as f:
    f.write(codigo_python)

caminho_py

