# pylint: disable=line-too-long
"""
Escriba el codigo que ejecute la accion solicitada.
"""


def pregunta_01():
    """
    El archivo `files//shipping-data.csv` contiene información sobre los envios
    de productos de una empresa. Cree un dashboard estático en HTML que
    permita visualizar los siguientes campos:

    * `Warehouse_block`

    * `Mode_of_Shipment`

    * `Customer_rating`

    * `Weight_in_gms`

    El dashboard generado debe ser similar a este:

    https://github.com/jdvelasq/LAB_matplotlib_dashboard/blob/main/shipping-dashboard-example.png

    Para ello, siga las instrucciones dadas en el siguiente video:

    https://youtu.be/AgbWALiAGVo

    Tenga en cuenta los siguientes cambios respecto al video:

    * El archivo de datos se encuentra en la carpeta `data`.

    * Todos los archivos debe ser creados en la carpeta `docs`.

    * Su código debe crear la carpeta `docs` si no existe.

    """
    import pandas as pd
    import matplotlib.pyplot as plt
    import os

    #Leer los datos
    df = pd.read_csv('files/input/shipping-data.csv')

    # Asegurar carpeta de salida
    os.makedirs("docs", exist_ok=True)

    #-----Gráfico para Shipping per Warehouse (Compras por bodega)---
    plt.figure()
    counts = df.Warehouse_block.value_counts()
    counts.plot.bar(                    #grafico de barras
        title='Shipping per Warehouse',
        xlabel='Warehouse Block',
        ylabel='Record Count',
        color='tab:blue',
        fontsize = 8,
    ) 
    #Bordes invisibles
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.savefig("docs/shipping_per_warehouse.png") #guardar grafico
    plt.close()

    #----Gráfico para Mode of Shipment----
    plt.figure()    
    counts = df.Mode_of_Shipment.value_counts()
    counts.plot.pie(            #grafico de torta
        title='Mode of Shipment',   
        wedgeprops= dict(width=0.35),  #ancho del grafico
        ylabel='',
        color=['tab:blue', 'tab:orange', 'tab:green'],
    )
    plt.savefig("docs/mode_of_shipment.png") #guardar grafico
    plt.close()

    #----Gráfico para Average Customer Rating----
    plt.figure()    
    resume_rating = df[["Mode_of_Shipment", "Customer_rating"]].groupby("Mode_of_Shipment").describe()
    resume_rating.columns = resume_rating.columns.droplevel()
    resume_rating = resume_rating[['mean', 'min', 'max']]

    plt.barh(                       #grafico de barras horizontales
        y=resume_rating.index.values,
        width=resume_rating['max'].values - 1,
        left = resume_rating['min'].values,
        height=0.9,
        color='lightgray',
        alpha=0.7,
    )

    colors = ['tab:green' if value >=3.0 else 'tab:orange' for value in resume_rating['mean'].values]

    plt.barh(                       
        y=resume_rating.index.values,
        width=resume_rating['mean'].values - 1,
        left= resume_rating['min'].values,
        color = colors,
        height=0.5,
        alpha=1.0,
    )

    plt.title('Average Customer Rating')
    plt.gca().spines['left'].set_color('gray')
    plt.gca().spines['bottom'].set_color('gray')
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.savefig("docs/average_customer_rating.png") #guardar grafico
    plt.close()
        
    #----Gráfico para Weight Distribution----
    plt.figure()
    counts = df.Weight_in_gms.plot.hist(   #grafico de histograma
        title='Shipped Weight Distribution',
        color='tab:orange',
        edgecolor='white',
    )
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.savefig("docs/weight_distribution.png") #guardar grafico
    plt.close()

    # --- HTML del dashboard ---
    html = """<!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>Shipping Data Dashboard Example</title>
    </head>
    <body>
        <h1>Shipping Data Dashboard</h1>

        <h2>Shipping per Warehouse</h2>
        <img src="shipping_per_warehouse.png" alt="Shipping per Warehouse">

        <h2>Mode of Shipment</h2>
        <img src="mode_of_shipment.png" alt="Mode of Shipment">

        <h2>Average Customer Rating</h2>
        <img src="average_customer_rating.png" alt="Average Customer Rating">

        <h2>Weight Distribution</h2>
        <img src="weight_distribution.png" alt="Weight Distribution">
    </body>
    </html>
    """
    with open("docs/index.html", "w", encoding="utf-8") as f:
        f.write(html)

if __name__ == "__main__":
    pregunta_01()