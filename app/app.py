import streamlit as st

st.title('Percurso NLCC para a área requisitante')

st.subheader('Vamos começar:')


st.markdown('**Fase de Planejamento**')
st.text('Responsável: Gestor/Equipe de Planejamento')
x = 1
st.write('{}. O primeiro passo do processo de contratação consiste em inserir a demanda no Planejamento Anual de Compras. A necessidade foi planejada neste procedimento?'.format(x))


pac = st.radio(
    'Base Legal: Resolução Seplag n.° 14, de 14 de fevereiro de 2014.',    
    ('Não',
    'Sim')
)

if pac == 'Não':
    st.write('> 1.1. Justifique no ETP as razões de não inclusão da demanda no Planejamento Anual de Compras.')

x+=1
st.write('{}. O recurso necessário para a contratação deve ser previsto no orçamento anual. Há previsão orçamentária para a aquisição/fornecimento?'.format(x))

orcamento = st.radio(
    'Base Legal: Inciso VII do art. 12 da NLCC.',    
    ('Não',
    'Sim')
)

if orcamento == 'Não':
    st.write('> 2.1. Inclua o valor na proposta de lei orçamentária do exercício seguinte ou solicite remanejamento/suplementação no orçamento do exercício financeiro corrente.')

finalOrcamento = st.checkbox('Previsão orçamentária finalizada!')

if finalOrcamento or orcamento == 'Sim':

    x += 1
    st.write('')

    if pac != 'Selecione uma opção':
        st.markdown('**Fase Preparatória**')
        st. text('Responsável: Equipe de Planejamento e Unidade de Compras')
        st.write('{}. Estabeleça um cronograma para a contratação e inicie a elaboração do Estudo Técnico Preliminar (ETP) em tempo hábil. O ETP constitui um documento que delimita o problema a ser resolvido e a sua melhor solução, de modo a permitir a avaliação da viabilidade técnica e econômica da contratação. Este documento deve conter minimamente os elementos dispostos no §§1º e 2º do art. 18 da NLCC.'.format(x))
        st.text('Base legal: Resolução Seplag n°115, de 29 de dezembro de 2021.')


        finalEtp = st.checkbox('O ETP foi concluído!')

        if finalEtp:
            conclusaoEtp = st.radio(
            'O ETP apontou qual será a solução adequada?',    
            ('Não',
            'Sim')
        )
            x+=1

            if conclusaoEtp == 'Sim':
                st.write('{}. Elabore os demais documentos preparatórios: Matriz de Riscos; Termo de Referência; Declaração de Disponibilidade Orçamentária, se for o caso.'.format(x))
                st.text('Base Legal: §1º do art. 40 da NLCC. Art. 22 da NLCC.')
                x+=1
                st.write('{}. Proceda à pesquisa de preços.'.format(x))
                st.text('Base Legal: Art. 23 da NLCC. Resolução Seplag n° 102, de 29 de dezembro de 2022.')
                x+=1
                st.write('{}. Providencie os documentos de designação do gestor e do fiscal do contrato.'.format(x))
                st.text('Base Legal: Art. 117 da NLCC.')
                x+=1
                st.write('{}. Realize os procedimentos necessários no Portal de Compras: Solicitação de Compras, Pedido de Compras, Mapa Comparativo de Preços.'.format(x))

                finalDocumentos = st.checkbox('Documentos finalizados!')

                if finalDocumentos:
                    documentos = st.radio(
                        'Todos os documentos foram assinados pela autoridade competente?',    
                        ('Não',
                        'Sim')
                    )
                    x+=1

                    if documentos == 'Sim':
                        st.write('{}. Encaminhe o processo para a área de compras, que promoverá a instrução processual, de acordo com o tipo de licitação adequado.'.format(x))

                    
                        analiseCompras = st.radio(
                            'A área de compras solicitou alguma informação complementar?',    
                            ('Não',
                            'Sim')
                        )
                        x+=1
                        if analiseCompras == 'Sim':
                            
                            st.write('{}. Promova os ajustes solicitados pela área de compras e remeta o processo à área novamente.'.format(x))
                            x+=1
                        
                        st.write('{}. Se não existir mais pendência, o processo será encaminhado para análise jurídica.'.format(x))

                        x+=1
                        finalJuridico = st.checkbox('Parecer jurídico emitido!')

                        if finalJuridico:
                            parecerJuridico = st.radio(
                                'O parecer jurídico apontou alguma ressalva?',    
                                ('Não',
                                'Sim')
                            )

                            if parecerJuridico == 'Sim':
                                st.write('{}. Promova os ajustes solicitados pelo parecer jurídico e remeta o processo à área de compras.'.format(x))
                                x+=1
                                
                            
                            st.write('{}. Se não existir mais pendência, o processo será encaminhado para publicação.'.format(x))
                            finalEdital = st.checkbox('Edital Publicado!')



                            if finalEdital:
                                st.write('')
                                st.markdown('**Fase Externa**')
                                st.write('Responsável: Esta etapa é conduzida pelo Agente de Contratação ou pela Comissão de Contratação. À área demandante cabe acompanhar.')
                                x+=1

                                st.write('{}. Acompanhe a publicação do Edital e responda ao Agente de Contratação, se forem necessárias diligências ou se forem interpostos recursos.'.format(x))
                                x+=1
                                st.write('{}. Se for apresentada proposta, o Agente de Contratação promoverá a análise de conformidade, a negociação e a habilitação do vencedor. E encaminhará a Autoridade Competente para homologação.'.format(x))
            
                                
                                homologacao = st.checkbox('Processo de Compras homologado!')
                                
                                    
                                if homologacao:
                                    st.write('')
                                    st.markdown('**Fase de Contratação**')
                                    st.write('Responsável: Esta etapa é conduzida pela Unidade de Contratação. À área demandante cabe acompanhar.')
                                    x+=1
                                    st.write('{}. Acompanhe a assinatura da Ata/Contrato.'.format(x))

                                    assinatura = st.checkbox('Ata/Contrato assinada/o!')
                                                                    
                                    if assinatura:
                                        st.write('')
                                        st.markdown('**Fase de Gestão Contratual**')
                                        st.text('Responsáveis: Gestor e Fiscal de contrato')
                                        x+=1
                                        st.write('{}. O empenho e a ordem de fornecimento/serviço podem ser emitidos.'.format(x))
                                        x+=1
                                        st.write('{}. Promova o acompanhamento e a fiscalização da execução do contrato ou instrumento similar.'.format(x))

