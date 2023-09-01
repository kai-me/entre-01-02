import requests
import csv

chaveAPI = "5ff7c844"

nomefilme = "Superman"
anolan = "2000"
ultano = "2010"

url = f"http://www.omdbapi.com/"

params = {
    "apikey": chaveAPI,
    "s": nomefilme,
    "y": f"{anolan}-{ultano}",
    "type": "movie"
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    if data["Response"] == "True":
        search_results = data["Search"]
        
        
        csv_file = "filmes.csv"
        csv_columns = ["Title", "Year", "imdbID", "Type", "Poster"]
        
        with open(csv_file, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=csv_columns)
            writer.writeheader()
            for result in search_results:
                writer.writerow(result)
        
        print(f"Dados dos filmes foram armazenados em '{csv_file}'.")
    else:
        print("Nenhum resultado encontrado.")
else:
    print("Erro na solicitação:", response.status_code)