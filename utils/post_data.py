import json
import requests
import click

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
        
URL = 'http://localhost:8000/api/'

@click.command()
@click.option('-i', '--input',  default='data.tsv', show_default=True, help='File name with the input data (format TSV)' )
@click.option('-m', '--model', default='', show_default=True, help='API path to execute post requests')
@click.option('-h', '--http_method', default='post', show_default=True, help='HTTP method')

def runHttpRequests(input, model, http_method):
    fp = open(input)
    jsonBodyList = parseData(fp.readlines())
    
    for jsonBody in jsonBodyList:

        if http_method == 'post':

            result = requests.post(
                url = f'{URL}{model}/',
                json = jsonBody, 
                headers = {'Content-Type' : 'application/json'}
                )

            if result.status_code == 201:
                print('Post request done!')
            else:
                print(f'Error code {result.status_code}')

        if http_method == 'patch':

            id = jsonBody['id']
            del jsonBody['id']

            result = requests.patch(
                url = f'{URL}{model}/{id}/',
                json = jsonBody, 
                headers = {'Content-Type' : 'application/json'}
                )
            
            if result.status_code == 200:
                print('Patch request done!')
            else:
                print(f'Error code {result.status_code}')
            





if __name__ == "__main__":
    runHttpRequests()