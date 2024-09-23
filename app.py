import streamlit as st
from graphviz import Digraph
from PIL import Image
import io

# Função para criar o organograma com quadros coloridos e organizados, incluindo tooltips
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
    org.node('Chefe', 'Bibliotecária Chefe', color='lightgray', fontcolor='black', 
             tooltip='Gestor da biblioteca, responsável pelo processamento técnico da unidade.')
    
    # Adicionar Secretária para o Bibliotecário Chefe
    org.node('Secretaria', 'Secretária', color='lightgray', fontcolor='black', 
             tooltip='Secretária do Bibliotecário Chefe, auxiliando nas tarefas administrativas.')
    org.edge('Chefe', 'Secretaria')

    # Nível 3: Bibliotecário Júnior
    org.node('Junior', 'Bibliotecário Júnior', color='lightgray', fontcolor='black', 
             tooltip='Responsável pelo serviço de referência e coordenação dos auxiliares. Também auxilia na classificação de obras antigas e no suporte a pesquisadores.')
    
    # Ligações entre o Chefe e o Júnior
    org.edge('Biblioteca', 'Chefe')
    org.edge('Chefe', 'Junior')

    # Nível 4: Paleógrafo e Restaurador ao lado do Bibliotecário Júnior
    org.node('Paleografo', 'Paleógrafo', color='lightgray', fontcolor='black', 
             tooltip='Responsável pela análise e transcrição de manuscritos históricos.')
    
    org.node('Restaurador', 'Restaurador (Terceirizado)', color='lightgray', fontcolor='black', 
             tooltip='Consultor responsável pela restauração de obras danificadas.')

    # Conectar Paleógrafo e Restaurador ao Junior (lado a lado)
    org.edge('Junior', 'Paleografo')
    org.edge('Junior', 'Restaurador')

    # Nível 4: Auxiliares de Biblioteca e Estagiários
    for i in range(1, 5):
        org.node(f'Auxiliar{i}', f'Auxiliar de Biblioteca {i}', color='lightgray', fontcolor='black', 
                 tooltip='Auxilia a equipe técnica, auxilia pesquisadores e classifica obras antigas.')
        org.edge('Junior', f'Auxiliar{i}')  # Auxiliares abaixo do Júnior

        # Adicionar dois estagiários para cada auxiliar
        for j in range(1, 3):
            org.node(f'Estagiario{i}_{j}', f'Estagiário {i}-{j}', color='lightgray', fontcolor='black', 
                     tooltip='Apoia em diversas tarefas sem responsabilidades específicas.')
            org.edge(f'Auxiliar{i}', f'Estagiario{i}_{j}')  # Estagiários ligados aos Auxiliares

    return org

# Função para gerar e baixar a imagem do organograma
def gerar_e_baixar_imagem(organograma, formato='png'):
    # Renderizar o organograma para um arquivo binário no formato solicitado
    img_bytes = organograma.pipe(format=formato)

    # Retornar os bytes da imagem para o download
    return img_bytes

# Interface com Streamlit
st.title('Organograma da Biblioteca do Instituto Histórico Geográfico da Bahia')

# Gerar organograma
organograma = criar_organograma()

# Exibir organograma no aplicativo
st.graphviz_chart(organograma.source)

# Opção para escolher o formato da imagem
formato_imagem = st.selectbox('Escolha o formato para baixar a imagem:', ['png', 'jpeg'])

# Gerar a imagem no formato escolhido
img_bytes = gerar_e_baixar_imagem(organograma, formato=formato_imagem)

# Adicionar botão de download
st.download_button(
    label="Baixar Organograma",
    data=img_bytes,
    file_name=f'organograma.{formato_imagem}',
    mime=f'image/{formato_imagem}'
)
