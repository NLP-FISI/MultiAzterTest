import pandas as pd

def get_text():
    print("Starting getText")
    df = pd.read_csv('/home/kenny/Documentos/repositories/MultiAzterTest/DatasetTrainEn/train.tsv', delimiter='\t')
    print("printing the first 5 rows")
    textArray = []      #this array is gonna contain al str texts
    #if you wanna try out only 5 rows, uncomment this: # textArray =  df.loc[:4, 'text'].tolist()  
    textArray =  df['text'].tolist() 
    return textArray





""" print("Starting application")
get_text()
print("Ending application") """