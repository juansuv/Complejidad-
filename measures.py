import pandas as pd


def measures(name):
    list_data = []
    for i in range(1, 10):
        if i != 0:
            data = pd.read_csv(f"{name}{i}.txt", header=None)
        else:
            data = pd.read_csv(f"{name}.txt", header=None)
        data = data.drop(data.index[[0]])
        data = data[[0, 1]]
        list_data.append(data)

    list_data_concat = pd.concat(list_data, ignore_index=True)
  
    list_data_concat.rename(columns={list_data_concat.columns[0]: 'iteraciones',list_data_concat.columns[1]: 'tiempo' },inplace=True)
    

    data_agrupada_mean = list_data_concat.groupby("iteraciones",as_index=False).mean()
    data_agrupada_median = list_data_concat.groupby("iteraciones",as_index=False).median()
    data_agrupada_count = list_data_concat.groupby("iteraciones",as_index=False).count()

    df_todos_los_datos = pd.merge(data_agrupada_mean, data_agrupada_median, on="iteraciones")
    df_todos_los_datos = pd.merge(df_todos_los_datos, data_agrupada_count, on ="iteraciones")
    df_todos_los_datos.columns= ["iteraciones", "promedio", "mediana", "total_de_muestras"]
    df_todos_los_datos[['iteraciones']]=df_todos_los_datos[['iteraciones']].astype(int)

    df_todos_los_datos.set_index("iteraciones",inplace=True)
    df_todos_los_datos.sort_index(inplace=True)
    
    return df_todos_los_datos


def save_xlsx():
    files=["merge","burbuja","quicksort"]
    for file in files:
        data=measures(f"{file}")
        data.to_excel(f"{file}.xlsx")
        print(f"{file} , {data}")


save_xlsx()
    

