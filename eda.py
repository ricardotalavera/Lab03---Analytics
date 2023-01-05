import pandas as pd
import utils

files = ["ACCES-A-INTER-FIJO-POR","CONEC-AL-SERVI-DE-INTER","INGRE-POR-LA-OPERA-DEL",
"PENET-DEL-INTER-FIJO-51614","TOTAL-NACIO-DE-ACCES-48866","VELOC-PROME-DE-BAJAD-DE"]

for file in files:
    #lectura personalizada
    if file in ["CONEC-AL-SERVI-DE-INTER"]:
        data=pd.read_csv("PowerBI/"+file+".csv",encoding="latin-1", decimal=".")
    else:
        if file in ["PENET-DEL-INTER-FIJO-51614"]:
            data=pd.read_csv("PowerBI/"+file+".csv",encoding="latin-1", decimal=",")
        else:
            if file in ["INDIC-MACRO"]:
                data=pd.read_csv("PowerBI/"+file+".csv",encoding="latin-1", decimal=",",thousands=".")
            else:
                data=pd.read_csv("PowerBI/"+file+".csv",encoding="latin-1", thousands=".")

    print("Observación inicial directa del file")
    print("***"*10)
    print(data.head(5))

    print("Tipo de datos :")
    print("***"*10)
    print(data.info())

    print("Observación de Na´s")
    print("***"*10)
    print(data.isna().sum(axis=0))

    #Personalizaciones
    if file == "CONEC-AL-SERVI-DE-INTER":
        utils.elimina_col(data,"link")
        data[["Latitud","Longitud"]]=data[["Latitud","Longitud"]].astype(float)
        print("Modificaciones efectuadas :")
        print("***"*10)
        print(data.info())

    if file == "ACCES-A-INTER-FIJO-POR":
        data["Año"].replace("\D","",regex=True,inplace=True)
        data["Trimestre"].replace("\D","",regex=True,inplace=True)
        utils.elimina_row(data,data.shape[0]-1)
        data.tail
        for i,j in enumerate(data["Año"]):
            data[["Año","Trimestre"]]=data[["Año","Trimestre"]].astype(int)
            
        
        print("Modificaciones efectuadas :")
        print("***"*10)
        print(data.info())
        
    
    
    data.to_csv("PowerBI/"+file.lower()+"_EDA.csv",index=False)

#Añadiendo formato vertical

file="acces-a-inter-fijo-por_EDA"
data=pd.read_csv("PowerBI/"+file+".csv")
data.head(3)

utils.elimina_col(data,"Total")
data= data.melt(id_vars =['Año','Trimestre','Provincia'], value_vars =['ADSL','Cablemodem',
'Fibra óptica','Wireless','Otros'], var_name = 'Tecnología')
data.to_csv("PowerBI/"+file.lower()+"_EDA_Ver.csv",index=False)

