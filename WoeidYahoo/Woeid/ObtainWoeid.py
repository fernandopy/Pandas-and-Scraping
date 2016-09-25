'''
Created on 25/09/2016

@author: fer
'''

import pandas as pd
from bs4 import BeautifulSoup
import requests
import time
import sys


def abre_csv():
    codigos = pd.read_csv("codigoPostal.csv")
    #print (len(codigos))
    #print (cod.duplicated())#PARA SABER SI hay valores repetidos
    cod = codigos.drop_duplicates()#elimina los valores duplicados
    #nombreCol = cod.columns.values.tolist()#saca elnombre de la columna
    #var = cod[nombreCol].values.tolist()#convierte los valores del dataframe en un arreglo
    arr = pd.np.array(cod)#converte los valores de la columna en un arreglo con numpy
    limpia_Codigos(arr)
def limpia_Codigos (arr):
    arr_woedis = []
    for i in range(0,len(arr)):#este ciclo sirve para agregar un creo al inicio de los codigos que tuvieran 4 digitos
        cp = arr[i][0]
        cp = pd.np.asscalar(pd.np.int16(cp))#para convertir de numpy.int64 a tipo nativo int
        cp_s = str(cp)
        if len(cp_s) == 4:
            cp_s = cp_s.zfill(5)#agrega ceros hasta cumplir la longitud en este caso long = 5 
            arr_woedis.append(scraping(cp_s))#se guarda en un arreglo
        else:
            arr_woedis.append(scraping(cp_s))#se guarda en un arreglo
    print len(arr_woedis)
            

    
def scraping(cp):
    url = "http://woeid.rosselliot.co.nz/lookup/"+cp #se le pega el cpodigo postal al la url 
    req = requests.get(url)#hace la peticion a la pagina con cada codigo postal
    statusCode = req.status_code #recupero el valor de la peticion
    if statusCode == 200:#si me regresa un 200 quiere decir que todo estuvo bien
        html = BeautifulSoup(req.text)#obtengo el html de la peticion 
        tr = html.find_all('tr',{'class':'woeid_row'})#busco el tr que tiene la informacion 
        for pais in tr:#recorrro los tr 
            if pais['data-country'] == 'Mexico' and pais['data-province_state'] == "Distrito Federal": #solo necesito el tr de mexico
                woeid = pais['data-woeid']#extraigo el valor de woeid
                print ("------")
                return woeid
                 
                
if __name__ == '__main__':
    abre_csv()    