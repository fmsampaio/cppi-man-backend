import json
import requests

def generateJsonBody(header, cells):
    returnable = {}
    for i in range(0, len(header)):
        returnable[header[i]] = cells[i]
    return returnable

def parseData(buffer):
    isHeader = True
    jsonBodyList = []
    for line in buffer:
        line = line[:-1]
        cells = line.split('\t')
        if isHeader:
            header = cells
            isHeader = False
        else:
            jsonBodyList.append(generateJsonBody(header, cells))
        
    return jsonBodyList
        
URL = 'http://localhost:8000/api/discentes/'

if __name__ == "__main__":
    fp = open('/home/felipe/Google Drive/Atividades/Projetos diversos/Sistema Gerência Pesquisa/dados.tsv')
    jsonBodyList = parseData(fp.readlines())
    
    for jsonBody in jsonBodyList:

        result = requests.post(
            url = URL,
            json = jsonBody, 
            headers = {'Content-Type' : 'application/json'}
            )

        if result.status_code == 201:
            print('Post realizado com sucesso!')

    
