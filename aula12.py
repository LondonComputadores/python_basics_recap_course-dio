import requests

#res = requests.get('https://viacep.com.br/ws/01001000/json/')
# print(res.status_code)
# print(res.text)
# print(type(res.text))

# print(res.status_code)
# print(res.json())
# print(type(res.json()))

# print(res.status_code)
# print(res.json())
# dados_cep = res.json()
# print(dados_cep['logradouro'])
# print(dados_cep['complemento'])

def retorna_dados_cep(cep):
    res = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))
    print(res.status_code)
    print(res.json())
    dados_cep = res.json()
    print(dados_cep['logradouro'])
    print(dados_cep['complemento'])
    return dados_cep

def retorna_dados_pokemon(pokemon):
    res = requests.get('https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon))
    dados_pokemon = res.json()
    return dados_pokemon

def retorna_response(url):
    res = requests.get(url)
    return res.text

if __name__ == '__main__':
    res = retorna_response('https://globallabs.ventures/')
    print(res)
    #retorna_dados_cep('01001000')
    #dados_pokemon = retorna_dados_pokemon('pikachu')
    #print(dados_pokemon)
    #print(dados_pokemon['name'])
    #print(dados_pokemon['abilities'])
    #print(dados_pokemon['sprites'] ['front_shiny'])

    #Ver sobre virtualenv tbm a partir daqui, mas de preferência
    #antes de começar os projetos e instalar todos os pacotes/bibliotecas
    #para cada ambiente virtual criado.