from bottle import route, run, template, post, request

@route('/api/heartbeat')
def index():
    return {"heartbeat":"ok"}

@route('/api/evento',  method='POST')
def index():
    param_value = request.json    
    if evento_valido(param_value, eventos_contact_id): 
        zona = str(param_value['zona']) if param_value['zona'] in range(0, 999) else ''        
        return {
            "status": "ok", 
            "mensagem":"evento recebido pelo receptor ip", 
            "evento": eventos_contact_id[param_value['evento']][param_value['qualificador']].replace('#', zona)
            }
    else: 
        return {
            "status": "erro", 
            "mensagem":"evento nao reconhecido", 
            "evento": ""
            }

def evento_valido(params, eventos):    
    return params['evento'] in eventos and \
    params['qualificador'] in eventos[params['evento']] and \
    params['zona'] in range(0, 999)

eventos_contact_id = {
        100: {'*': "Emergencia medica"},
        110: {'*': "Alarme de incendio"},
        120: {'*': "Panico"},
        121: {'*': "Ativacao/desativacao sob coacao"},
        122: {'*': "Panico silencioso"},
        130: {
            'aber': "Disparo de zona #}",
            'rest': "Restauracao de zona #"
             },
        133: {'*': "Disparo de zona 24h #"},
        146: {'*': "Disparo silencioso #"},
        301: {
            'aber': "Falta de energia AC",
            'rest': "Retorno de energia AC"
             },
        342: {
             'aber': "Falta de energia AC em componente sem fio #",
             'rest': "Retorno energia AC em componente sem fio #"
             },
        302: {
            'aber': "Bateria do sistema baixa",
            'rest': "Recuperacao bateria do sistema baixa"
             },
        305: {'*': "Reset do sistema"},
        306: {'*': "Alteracao programacao"},
        311: {
            'aber': "Bateria ausente",
            'rest': "Recuperacao bateria ausente"
             },
        351: {
            'aber': "Corte linha telefonica",
            'rest': "Restauro linha telefonica"
             },
        354: {'*': "Falha ao comunicar evento"},
        147: {
            'aber': "Falha de supervisao #",
            'rest': "Recuperacao falha de supervisao #"
             },
        145: {
             'aber': "Tamper em dispositivo expansor #",
             'rest': "Restauro tamper em dispositivo expansor #"
              },
        383: {
              'aber': "Tamper em sensor #",
              'rest': "Restauro tamper em sensor #"
              },
        384: {
            'aber': "Bateria baixa em componente sem fio #",
            'rest': "Recuperacao bateria baixa em componente sem fio #"
             },
        401: {
             'rest': "Ativacao manual",
             'aber': "Desativacao manual"
             },
        403: {
             'rest': "Ativacao automatica",
             'aber': "Desativacao automatica"
             },
        404: {
            'rest': "Ativacao remota",
            'aber': "Desativacao remota",
             },
        407: {
            'rest': "Ativacao remota II",
            'aber': "Desativacao remota II",
             },
        408: {'*': "Ativacao por uma tecla"},
        410: {'*': "Acesso remoto"},
        461: {'*': "Senha incorreta"},
        570: {
             'aber': "Bypass de zona #",
             'rest': "Cancel bypass de zona #"
             },
        602: {'*': "Teste periodico"},
        621: {'*': "Reset do buffer de eventos"},
        601: {'*': "Teste manual"},
        616: {'*': "Solicitacao de manutencao"},
        422: {
            'aber': "Acionamento de PGM #",
            'rest': "Desligamento de PGM #"
             },
        625: {'*': "Data e hora reiniciados"}
    }

run(host='localhost', port=8080)
