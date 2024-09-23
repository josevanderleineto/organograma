import streamlit as st
import pydot
import base64
from io import BytesIO
import networkx as nx

# Função para criar o organograma
def criar_organograma():
    G = nx.DiGraph()

    # Adicionando nós
    G.add_node('Instituto', tooltip='Instituição mantenedora da Biblioteca Ruy Barbosa.')
    G.add_node('Biblioteca', tooltip='Biblioteca especializada em estudos históricos e geográficos da Bahia.')
    G.add_node('Chefe', tooltip='Gestor da biblioteca, responsável pelo processamento técnico da unidade.')
    G.add_node('Junior', tooltip='Responsável pelo serviço de referência e coordenação dos auxiliares.')
    
    for i in range(1, 5):
        G.add_node(f'Auxiliar{i}', tooltip='Auxilia a equipe técnica e os pesquisadores.')
        G.add_node(f'Estagiario{i}', tooltip='Apoia em diversas tarefas sem responsabilidades específicas.')
    
    G.add_node('Paleografo', tooltip='Responsável pela análise e transcrição de manuscritos históricos.')
    G.add_node('Restaurador', tooltip='Consultor responsável pela restauração de obras danificadas.')

    # Adicionando arestas
    G.add_edges_from([
        ('Instituto', 'Biblioteca'),
        ('Biblioteca', 'Chefe'),
        ('Chefe', 'Junior'),
        ('Junior', 'Auxiliar1'),
        ('Junior', 'Auxiliar2'),
        ('Junior', 'Auxiliar3'),
        ('Junior', 'Auxiliar4'),
        ('Junior', 'Paleografo'),
        ('Junior', 'Restaurador'),
        ('Auxiliar1', 'Estagiario1'),
        ('Auxiliar1', 'Estagiario2'),
        # Adicione mais estagiários conforme necessário
    ])

    return G

# Função para gerar a imagem do organograma
def gerar_imagem(G):
    dot = nx.drawing.nx_pydot.to_pydot(G)
    img_bytes = dot.create(format='png')
    return img_bytes

# Interface com Streamlit
st.title('Organograma da Biblioteca do Instituto Histórico Geográfico da Bahia')

# Criar organograma
organograma = criar_organograma()

# Gerar a imagem
img_bytes = gerar_imagem(organograma)

# Exibir imagem no Streamlit
st.image(img_bytes, caption='Organograma', use_column_width=True)

# Converter bytes em base64 para download
b64 = base64.b64encode(img_bytes).decode()
href = f'<a href="data:file/png;base64,{b64}" download="organograma.png">Baixar Organograma</a>'
st.markdown(href, unsafe_allow_html=True)
