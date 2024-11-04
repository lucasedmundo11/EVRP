import numpy as np
import pandas as pd

from config.params import params
from src.places_api import PlacesAPI


def export_data(df, path):
    df.to_csv(path, index=False, sep=";", decimal=".", encoding="utf-8")
    pass




def get_charging_stations():
    cities = [
        "São Paulo", "Osasco", "Carapicuíba", "Barueri", "Santana de Parnaíba", "Itapevi", "Jandira",
        "Cotia", "Embu das Artes", "Taboão da Serra", "Itapecerica da Serra", "Embu-Guaçu",
        "São Lourenço da Serra", "Juquitiba", "Caieiras", "Cajamar", "Franco da Rocha",
        "Francisco Morato", "Mairiporã", "Guarulhos", "Arujá", "Itaquaquecetuba", "Poá",
        "Ferraz de Vasconcelos", "Suzano", "Mogi das Cruzes", "Salesópolis", "Santa Isabel",
        "Biritiba Mirim", "São Bernardo do Campo", "Santo André", "São Caetano do Sul", "Diadema",
        "Mauá", "Ribeirão Pires", "Rio Grande da Serra"
    ]
    total_response = list()

    for city in cities:    
        api_key = params["API_KEY"]
        base_url = "https://places.googleapis.com/v1/places:searchText"
        maxResultCount = 5
        places = PlacesAPI(city, base_url, api_key, maxResultCount)
        response = places.post()
        total_response += response['places']
        #while "nextPageToken" in response.keys():
        #    places = PlacesAPI(city, base_url, api_key, maxResultCount, pageToken=response["nextPageToken"])
        #    response = places.post()
        #    total_response += response['places']

    return total_response

def process_data(response):
    charging_stations = {
        "Latitude": [],
        "Longitude": [],
        "Potência de Recarga": []
    }
    for place in response:
        charging_stations["Latitude"].append(place["location"]["latitude"])
        charging_stations["Longitude"].append(place["location"]["longitude"])
        try:
            charging_stations["Potência de Recarga"].append(place["evChargeOptions"]["connectorAggregation"][0]["maxChargeRateKw"])
        except KeyError:
            charging_stations["Potência de Recarga"].append(pd.NA)
    
    df = pd.DataFrame(charging_stations)
    df['ID'] = df.index+1
    df["ID"] = "R"+df["ID"].astype(str)
    df['Tipo'] = "Estação de Recarga"
    df["Potência de Recarga"] = df["Potência de Recarga"].fillna(df["Potência de Recarga"].mean())
    df["Potência de Recarga"] = df["Potência de Recarga"].astype(int)
    
    df = df[["ID", "Latitude", "Longitude", "Tipo", "Potência de Recarga"]].copy()
    export_data(df, "../data/input/charging_stations.csv")
    return df