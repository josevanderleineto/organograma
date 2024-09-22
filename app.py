import streamlit as st
from graphviz import Digraph

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

    # Nível 3: Staff da Biblioteca (Chefe, Sênior, Júnior)
    org.node('Chefe', 'Bibliotecária Chefe', color='lightgray', fontcolor='black', 
             tooltip='Gestor da biblioteca, responsável pelo processamento técnico da unidade.')
    org.node('Senior', 'Bibliotecário Sênior', color='lightgray', fontcolor='black', 
             tooltip='Auxilia o Chefe nas operações e coordena tarefas técnicas.')
    org.node('Junior', 'Bibliotecário Júnior', color='lightgray', fontcolor='black', 
             tooltip='Responsável pelo serviço de referência e coordenação dos auxiliares. Também auxilia na classificação de obras antigas e no suporte a pesquisadores.')
    org.node('Paleografo', 'Paleógrafo', color='lightgray', fontcolor='black', 
             tooltip='Responsável pela análise e transcrição de manuscritos históricos.')

    # Ligações entre o nível 2 e 3 (Chefe, Sênior, Júnior e Paleógrafo)
    org.edge('Biblioteca', 'Chefe')
    org.edge('Chefe', 'Senior')
    org.edge('Senior', 'Junior')
    org.edge('Junior', 'Paleografo')  # Paleógrafo ao lado do Júnior

    # Nível 4: Auxiliares de Biblioteca
    for i in range(1, 5):
        org.node(f'Auxiliar{i}', f'Auxiliar de Biblioteca {i}', color='lightgray', fontcolor='black', 
                 tooltip='Auxilia a equipe técnica, auxilia pesquisadores e classifica obras antigas.')
        org.edge('Junior', f'Auxiliar{i}')  # Auxiliares abaixo do Júnior
    
    # Nível 4: Restaurador
    org.node('Restaurador', 'Restaurador', color='lightgray', fontcolor='black', 
             tooltip='Trabalha no processo de restauração de obras danificadas.')
    org.edge(f'Auxiliar1', 'Restaurador')  # Restaurador ligado ao primeiro auxiliar

    # Nível 4: Estagiário
    org.node('Estagiario', 'Estagiário', color='lightgray', fontcolor='black', 
             tooltip='Apoia em diversas tarefas sem responsabilidades específicas.')
    org.edge(f'Auxiliar2', 'Estagiario')  # Estagiário ligado ao segundo auxiliar

    return org

# Interface com Streamlit
st.title('Organograma Colorido da Biblioteca do Instituto Histórico Geográfico da Bahia')

# Gerar organograma
organograma_colorido = criar_organograma()

# Exibir organograma
st.graphviz_chart(organograma_colorido.source)
