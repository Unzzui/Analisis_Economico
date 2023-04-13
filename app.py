import streamlit as st
import pandas as pd
import plotly.express as px
import pycountry_convert as pc
import locale

st.set_page_config(page_title="Análisis Económico")

st.markdown(("""
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""),unsafe_allow_html=True)
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

# Carga los datos desde el archivo CSV
data = pd.read_csv("Data.csv", delimiter=";")

# Agrupa los datos por país y año y calcula los promedios
data = data.groupby(['PAIS', 'AÑO']).mean().reset_index()

# Define el año seleccionado en el sidebar
years = st.sidebar.multiselect("Selecciona los años", options=data['AÑO'].unique(), default=data['AÑO'].unique())

# Filtra los datos por el año seleccionado
filtered_data = data[data['AÑO'].isin(years)]


st.title("Análisis Económico: Más Allá del PIB")
st.write("Bienvenido a este complemento del informe de análisis económico, donde se analizan diversos indicadores para medir la economía de los países de América Latina, más allá del tradicional Producto Interno Bruto (PIB). Aquí se podra visualizar gráficos de mapa con indicadores como PIB, PIB per cápita, gasto público, gasto público per cápita, IPC y población, y ver cómo se distribuyen en la región. El color en el mapa determinará qué países tienen los valores más altos y cuáles los más bajos.")


# Convierte los nombres de países a códigos ISO Alpha-3
def get_alpha_3(country_name):
    try:
        return pc.country_name_to_country_alpha3(country_name, cn_name_format="default")
    except:
        return None

filtered_data['alpha_3'] = filtered_data['PAIS'].apply(get_alpha_3)


st.subheader("PIB Latinoamérica")

# Crea el mapa con los valores del PIB
fig_pib = px.choropleth(data_frame=filtered_data,
                    locations='alpha_3',
                    color='PIB M$',
                    animation_frame='AÑO',
                    title='PIB en América Latina')

fig_pib.update_layout(
    geo=dict(
        scope="south america",
        showframe=False,  # Oculta el borde del mapa
        showcoastlines=False,  # Oculta las costas
        projection_type='equirectangular'  # Tipo de proyección del mapa
    ),
    margin=dict(t=0, b=0, l=0, r=0),  # Configura los márgenes del mapa
    title=dict(x=0.5)  # Centra el título del mapa
)

st.plotly_chart(fig_pib)

# Crea la tabla con el PIB
pib_table = pd.pivot_table(filtered_data, index='PAIS', columns='AÑO', values='PIB M$', aggfunc='first')
pib_table['Promedio'] = pib_table.mean(axis=1)
pib_table = pib_table.sort_values(by='Promedio', ascending=False)
pib_table = pib_table.applymap(lambda x: f"${x:,.0f}")


st.table(pib_table)
st.subheader("PIB per Cápita")

fig_pib_per_capita = px.choropleth(data_frame=filtered_data,
                    locations='alpha_3',
                    color='PIB PER CAPITA',
                    animation_frame='AÑO',
                    title='PIB per cápita en América Latina')

fig_pib_per_capita.update_layout(
    geo=dict(
        scope="south america",
        showframe=False,  # Oculta el borde del mapa
        showcoastlines=False,  # Oculta las costas
        projection_type='equirectangular'  # Tipo de proyección del mapa
    ),
    margin=dict(t=0, b=0, l=0, r=0),  # Configura los márgenes del mapa
    title=dict(x=0.5)  # Centra el título del mapa
)

st.plotly_chart(fig_pib_per_capita)

# Crea la tabla con el PIB per capita
pib_per_table = pd.pivot_table(filtered_data, index='PAIS', columns='AÑO', values='PIB PER CAPITA', aggfunc='first')
pib_per_table['Promedio'] = pib_per_table.mean(axis=1)
pib_per_table = pib_per_table.sort_values(by='Promedio', ascending=False)
pib_per_table = pib_per_table.applymap(lambda x: f"${x:,.0f}")
st.table(pib_per_table)

st.subheader("Gasto Público")

fig_public_expense = px.choropleth(data_frame=filtered_data,
                    locations='alpha_3',
                    color='GASTO PUBLICO M$',
                    animation_frame='AÑO',
                    title='Gasto Público en América Latina')

fig_public_expense.update_layout(
    geo=dict(
        scope="south america",
        showframe=False,  # Oculta el borde del mapa
        showcoastlines=False,  # Oculta las costas
        projection_type='equirectangular'  # Tipo de proyección del mapa
    ),
    margin=dict(t=0, b=0, l=0, r=0),  # Configura los márgenes del mapa
    title=dict(x=0.5)  # Centra el título del mapa
)

st.plotly_chart(fig_public_expense)

# Crea la tabla con el PIB per capita
expense_table = pd.pivot_table(filtered_data, index='PAIS', columns='AÑO', values='GASTO PUBLICO M$', aggfunc='first')
expense_table['Promedio'] = expense_table.mean(axis=1)
expense_table = expense_table.sort_values(by='Promedio', ascending=False)
expense_table = expense_table.applymap(lambda x: f"${x:,.0f}")
st.table(expense_table)


st.subheader("Gasto Público per Cápita")

fig_public_expense_per = px.choropleth(data_frame=filtered_data,
                    locations='alpha_3',
                    color='GASTO PER CAPITA',
                    animation_frame='AÑO',
                    title='Gasto Público per cápita en América Latina')

fig_public_expense_per.update_layout(
    geo=dict(
        scope="south america",
        showframe=False,  # Oculta el borde del mapa
        showcoastlines=False,  # Oculta las costas
        projection_type='equirectangular'  # Tipo de proyección del mapa
    ),
    margin=dict(t=0, b=0, l=0, r=0),  # Configura los márgenes del mapa
    title=dict(x=0.5)  # Centra el título del mapa
)

st.plotly_chart(fig_public_expense_per)

# Crea la tabla con el PIB per capita
expense_per_table = pd.pivot_table(filtered_data, index='PAIS', columns='AÑO', values='GASTO PER CAPITA', aggfunc='first')
expense_per_table['Promedio'] = expense_per_table.mean(axis=1)
expense_per_table = expense_per_table.sort_values(by='Promedio', ascending=False)
expense_per_table = expense_per_table.applymap(lambda x: f"${x:,.0f}")
st.table(expense_per_table)


st.subheader("Indice Precio del Consumidor")


fig_ipc = px.choropleth(data_frame=filtered_data,
                    locations='alpha_3',
                    color='IPC %',
                    animation_frame='AÑO',
                    title='IPC en América Latina')

fig_ipc.update_layout(
    geo=dict(
        scope="south america",
        showframe=False,  # Oculta el borde del mapa
        showcoastlines=False,  # Oculta las costas
        projection_type='equirectangular'  # Tipo de proyección del mapa
    ),
    margin=dict(t=0, b=0, l=0, r=0),  # Configura los márgenes del mapa
    title=dict(x=0.5)  # Centra el título del mapa
)

st.plotly_chart(fig_ipc)

# Crea la tabla con el PIB per capita

ipc_table = pd.pivot_table(filtered_data, index='PAIS', columns='AÑO', values='IPC %', aggfunc='first')
ipc_table['Promedio'] = ipc_table.mean(axis=1)
ipc_table = ipc_table.sort_values(by='Promedio', ascending=False)
ipc_table = ipc_table.applymap(lambda x: "{:.2f}%".format(x*100))

st.table(ipc_table)


st.subheader("Población")

fig_pupulation = px.choropleth(data_frame=filtered_data,
                    locations='alpha_3',
                    color='POBLACION',
                    animation_frame='AÑO',
                    title='Población')

fig_pupulation.update_layout(
    geo=dict(
        scope="south america",
        showframe=False,  # Oculta el borde del mapa
        showcoastlines=False,  # Oculta las costas
        projection_type='equirectangular'  # Tipo de proyección del mapa
    ),
    margin=dict(t=0, b=0, l=0, r=0),  # Configura los márgenes del mapa
    title=dict(x=0.5)  # Centra el título del mapa
)

st.plotly_chart(fig_pupulation)

# Crea la tabla con el PIB per capita

population_table = pd.pivot_table(filtered_data, index='PAIS', columns='AÑO', values='POBLACION', aggfunc='first')
population_table = population_table.applymap(lambda x: x * 1000000)  # convierte a millones
population_table['Promedio'] = population_table.mean(axis=1)
population_table = population_table.sort_values(by='Promedio', ascending=False)
population_table = population_table.applymap(lambda x: f"{x:,.0f}")


st.table(population_table)
