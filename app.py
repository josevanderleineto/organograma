import streamlit as st
import pydot
from PIL import Image
import io

# Função para criar o organograma com pydot
def criar_organograma():
    graph = pydot.Dot(graph_type='digraph')

    # Adicionando nós e arestas
    graph.add_node(pydot.Node("Instituto", label="Instituto Histórico Geográfico da Bahia", style="filled", fillcolor="lightcoral"))
    graph.add_node(pydot.Node("Biblioteca", label="Biblioteca Ruy Barbosa", style="filled", fillcolor="lightgoldenrod1"))
    graph.add_edge(pydot.Edge("Instituto", "Biblioteca"))

    # Continuar adicionando nós e arestas como no seu código anterior...
    # ...

    return graph

# Função para gerar e salvar a imagem do organograma
def gerar_imagem(graph, formato='png'):
    img_bytes = graph.create(format=formato)
    return img_bytes

# Interface com Streamlit
st.title('Organograma da Biblioteca do Instituto Histórico Geográfico da Bahia')

# Gerar organograma
organograma = criar_organograma()

# Exibir organograma no aplicativo
st.graphviz_chart(organograma.to_string())

# Opção para escolher o formato da imagem
formato_imagem = st.selectbox('Escolha o formato para baixar a imagem:', ['png', 'jpeg'])

# Gerar a imagem no formato escolhido
img_bytes = gerar_imagem(organograma, formato=formato_imagem)

# Adicionar botão de download
st.download_button(
    label="Baixar Organograma",
    data=img_bytes,
    file_name=f'organograma.{formato_imagem}',
    mime=f'image/{formato_imagem}'
)
