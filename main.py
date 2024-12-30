import yaml

with open('info.yaml', 'r', encoding='utf-8') as infos_yaml:
    infos = yaml.safe_load(infos_yaml)

arquivo_modelo = "layout.html"
arquivo_saida = "output1.html"

# abre o layout
with open(arquivo_modelo, 'r', encoding='utf-8') as modelo:
    string_modelo = modelo.read()

# ano, numero e data
string_modelo = string_modelo.replace('${ANO}', str(infos['ano']))
string_modelo = string_modelo.replace('${NUMERO}', str(infos['numero']))
string_modelo = string_modelo.replace('${DATA}', infos['data'])

# separador, para quando precisar
with open('includes/separador.html', 'r', encoding='utf-8') as separador_arquivo:
    separador = separador_arquivo.read()

string_modelo = string_modelo.replace("${SEPARADOR}", separador + '\n')

# avisos, se for o caso
if len(infos['avisos']):
    avisos_string = ""
    
    # cabecalho dos avisos
    with open('includes/avisos_header.html', 'r', encoding='utf-8') as aviso_header:
        avisos_string = aviso_header.read() + "\n"

    # modelo de aviso
    with open('includes/avisos_modelo.html', 'r', encoding='utf-8') as aviso_modelo:
        aviso_modelo_string = aviso_modelo.read()

    # agora pega os avisos
    for aviso in infos['avisos']:
        avisos_string += aviso_modelo_string.replace("${TEXTO}", aviso) + '\n'

    # adiciona um separador
    avisos_string += separador + '\n'

    string_modelo = string_modelo.replace("${AVISOS}", avisos_string)


# cabecalho dos posts
string_modelo = string_modelo.replace("${BOLETIME_NUMERO}", str(infos['boletime_numero']))
string_modelo = string_modelo.replace("${BOLETIME_MES_ANO}", str(infos['boletime_mes_ano']))

# abre o layout de posts
with open('includes/post_modelo.html', 'r', encoding='utf-8') as post_modelo_arquivo:
    post_modelo = post_modelo_arquivo.read()

posts_string = ""

# agora cria os posts
for i,post in enumerate(infos['posts']):
    post_str = post_modelo.replace('${TITULO}', post['titulo'])
    post_str = post_str.replace('${AUTORIA}', post['autoria'])
    post_str = post_str.replace('${RESUMO}', post['resumo'])
    post_str = post_str.replace('${LINK}', post['link'])
    post_str = post_str.replace('${CAPA}', post['capa'])
    posts_string += post_str + '\n'

string_modelo = string_modelo.replace('${POSTS}', posts_string)

# formulario do boletime
string_modelo = string_modelo.replace("${LINK_FORMS_BOLETIME}", infos['link_forms_boletime'])

# html final
with open(arquivo_saida, 'w', encoding='utf-8') as output:
    output.write(string_modelo)