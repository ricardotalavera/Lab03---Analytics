import requests
import bs4

api_key = "phhRStNRniQFCD2vwWnPWTIRbNWKglAVJjvRfCLD"

def download_csv(link):
    response = requests.get(link)
    GUI=link.replace("http://api.datosabiertos.enacom.gob.ar/api/v2/datastreams/","")
    GUI=GUI.replace("/data.csv/?auth_key="+api_key,"")
    if response.status_code==200:
        bytes = response.content
        bytes = bytes.decode("utf-8")
        file = open("PowerBI/" + GUI + ".csv","w")
        file.write(bytes)
        file.close()
        print(f"Archivo grabado {GUI}.csv")
    else:
        print(f"Error en bajada de API {response.status_code} no se grabo archivo {GUI}.csv")

def get_final_link(url):
    response=requests.get(url)
    soup = bs4.BeautifulSoup(response.text,"html.parser")
    lista = soup.find_all('article', class_="examples")
    for child in lista:
        link = str(child.code).replace("<code>","")
        link = link.replace("json","csv")
        link = link.replace("YOUR_API_KEY&amp",api_key)
        link = link.replace(";limit=50</code>","")
    return link


def get_init_all(pagina=2):
    host = "https://datosabiertos.enacom.gob.ar/search/?q=%25&page=0&category=Acceso%20a%20Internet&resource=ds&account="
    lis = []
    pag = 0
    final = False
    while not final:
        pag+=1
        if pag <= pagina :
            pag_ant = "page="+str(pag-1)
            pag_now = "page="+str(pag)
            host=host.replace(pag_ant,pag_now)
            response=requests.get(host)
        

            if response.status_code==200:
                    soup = bs4.BeautifulSoup(response.text,"html.parser")
                    links  = soup.find_all("a",class_="ic_Data")
                    for child in links:
                        lis.append(child["href"])
            else:
                final = True
                print(f"No existe {pag_now} r.status_code = {response.status_code}")
        else:
            final = True
    
    return(lis)

def elimina_col(data,col):
    data.drop([col],axis=1,inplace = True)

def elimina_row(data,rownum):
    data.drop([rownum],axis=0,inplace=True)