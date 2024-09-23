import streamlit as st
from graphviz import Digraph

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
             tooltip='Responsável pelo serviço de referência e coordenação dos auxiliares. Também auxilia na classificação de obras antigas e no suporte a pesquisadores.')
    org.edge('Chefe', 'Junior')

    # Nível 4: Auxiliares de Biblioteca e Estagiários
    for i in range(1, 5):
        org.node(f'Auxiliar{i}', f'Auxiliar de Biblioteca {i}', color='lightgray', 
                 tooltip='Auxilia a equipe técnica, auxilia pesquisadores e classifica obras antigas.')
        org.edge('Junior', f'Auxiliar{i}')

        # Adicionar dois estagiários para cada auxiliar
        for j in range(1, 3):
            org.node(f'Estagiario{i}_{j}', f'Estagiário {i}-{j}', color='lightgray', 
                     tooltip='Apoia em diversas tarefas sem responsabilidades específicas.')
            org.edge(f'Auxiliar{i}', f'Estagiario{i}_{j}')

    # Nível 4: Paleógrafo
    org.node('Paleografo', 'Paleógrafo', color='lightgray', 
             tooltip='Responsável pela análise e transcrição de manuscritos históricos.')
    org.edge('Auxiliar1', 'Paleografo')

    # Nível 4: Restaurador como Consultor
    org.node('Restaurador', 'Restaurador (Consultor)', color='lightgray', 
             tooltip='Consultor responsável pela restauração de obras danificadas.')
    org.edge('Junior', 'Restaurador')

    return org

# Função para gerar e baixar a imagem do organograma
def gerar_e_baixar_imagem(organograma, formato='png'):
    img_bytes = organograma.pipe(format=formato)  # Gera a imagem no formato especificado
    return img_bytes

# Interface com Streamlit
st.title('Organograma da Biblioteca do Instituto Histórico Geográfico da Bahia')

# Gerar organograma
organograma = criar_organograma()

# Exibir organograma
st.graphviz_chart(organograma.source)

# Botão para baixar a imagem
if st.button('Baixar Organograma'):
    img_bytes = gerar_e_baixar_imagem(organograma, formato='png')
    st.download_button(label='Download da Imagem', data=img_bytes, file_name='organograma.png', mime='image/png')
