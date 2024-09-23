import streamlit as st
from graphviz import Digraph
import base64

# Função para criar o organograma
def criar_organograma():
    org = Digraph(comment='Organograma da Biblioteca do Instituto Histórico Geográfico da Bahia')

    # Definições gerais de estilo
    org.attr('node', shape='box', style='filled', fontcolor='black')

    # Nível 1: Instituto
    org.node('Instituto', 'Instituto Histórico Geográfico da Bahia', color='lightcoral', 
             tooltip='Instituição mantenedora da Biblioteca Ruy Barbosa.')

    # Nível 2: Biblioteca Ruy Barbosa
    org.node('Biblioteca', 'Biblioteca Ruy Barbosa', color='lightgoldenrod1', 
             tooltip='Biblioteca especializada em estudos históricos e geográficos da Bahia.')
    org.edge('Instituto', 'Biblioteca')

    # Nível 3: Staff da Biblioteca (Chefe, Júnior)
    org.node('Chefe', 'Bibliotecária Chefe', color='lightgray', 
             tooltip='Gestor da biblioteca, responsável pelo processamento técnico da unidade.')
    org.edge('Biblioteca', 'Chefe')

    org.node('Junior', 'Bibliotecário Júnior', color='lightgray', 
             tooltip='Responsável pelo serviço de referência e coordenação dos auxiliares.')
    org.edge('Chefe', 'Junior')

    # Nível 4: Auxiliares de Biblioteca
    for i in range(1, 5):
        org.node(f'Auxiliar{i}', f'Auxiliar de Biblioteca {i}', color='lightgray', 
                 tooltip='Auxilia a equipe técnica e os pesquisadores.')
        org.edge('Junior', f'Auxiliar{i}')

        # Estagiários
        for j in range(1, 3):
            org.node(f'Estagiario{i}_{j}', f'Estagiário {i}-{j}', color='lightgray', 
                     tooltip='Apoia em diversas tarefas sem responsabilidades específicas.')
            org.edge(f'Auxiliar{i}', f'Estagiario{i}_{j}')

    # Nível 4: Paleógrafo
    org.node('Paleografo', 'Paleógrafo', color='lightgray', 
             tooltip='Responsável pela análise e transcrição de manuscritos históricos.')
    org.edge('Junior', 'Paleografo')

    # Nível 4: Restaurador como Consultor
    org.node('Restaurador', 'Restaurador (Consultor)', color='lightgray', 
             tooltip='Consultor responsável pela restauração de obras danificadas.')
    org.edge('Junior', 'Restaurador')

    return org

# Função para gerar e baixar a imagem do organograma
def gerar_imagem(org):
    img_bytes = org.pipe(format='png')  # Gera a imagem no formato PNG
    return img_bytes

# Interface com Streamlit
st.title('Organograma da Biblioteca do Instituto Histórico Geográfico da Bahia')

# Gerar organograma
organograma = criar_organograma()

# Exibir organograma
st.graphviz_chart(organograma.source)

# Gerar a imagem para download
img_bytes = gerar_imagem(organograma)

# Converter bytes em base64 para download
b64 = base64.b64encode(img_bytes).decode()
href = f'<a href="data:file/png;base64,{b64}" download="organograma.png">Baixar Organograma</a>'
st.markdown(href, unsafe_allow_html=True)
