import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from datetime import datetime

st.set_option('deprecation.showPyplotGlobalUse', False)

st.title("Would you be stroke?")
st.sidebar.image("strokegraphic.jpeg",width=200)

st.markdown("""
Accidente cerebrovascular
- Un accidente cerebrovascular sucede cuando el flujo de sangre a una parte del cerebro se detiene. Algunas veces, se denomina "ataque cerebral".
- Si el flujo sanguíneo se detiene por más de pocos segundos, el cerebro no puede recibir nutrientes y oxígeno. Las células cerebrales pueden morir, lo que causa daño permanente.
- Un accidente cerebrovascular se presenta cuando un vaso sanguíneo en el cerebro se rompe, causando un sangrado dentro de la cabeza.
    """)


df = pd.read_csv('stroke_dataset.csv')
df["age"] = df["age"].astype(float).astype(int)
df["smoking_status"].replace("Unknown",np.nan,inplace=True)
#用众数填充缺失值 Rellena los valores que faltan con la moda
df["smoking_status"].fillna(df["smoking_status"].mode()[0],inplace=True)
df = df.drop_duplicates()

st.sidebar.write("1. Presentación Equipo Cerebro")
st.subheader(" 1.Presentación Equipo Cerebro")
# df

st.sidebar.write("2. Análisis y Visualización de dataset")
st.subheader(" 2. Análisis y Visualización de dataset")
st.write("a.stroke")

#设置可视化数据列的百分比 Establecer el porcentaje de una columna de datos de visualización
def annot_plot(ax):
    ax.spines["top"].set_visible(False)#设置顶部边框为空
    ax.spines["right"].set_visible(False) #设置右侧边框为空
    for p in ax.patches:
        ax.annotate(f"{p.get_height()*100/df.shape[0]:.2f}%",(p.get_x()+p.get_width()/2,p.get_height()),
                   ha="center",va="center",fontsize=11,color="black",rotation=0,xytext=(0,10),textcoords="offset points")

fig, subplot_arr = plt.subplots(3,4,figsize=(50,40))

ax1 = plt.subplot(321)
ax1 = sns.countplot(x="stroke",hue="gender",data=df, palette="gist_rainbow_r")
plt.xlabel("stroke-gender", fontsize=20)
annot_plot(ax1)

ax2 = plt.subplot(322)
ax2 = sns.countplot(x = df.stroke,  hue= df.hypertension,data=df, palette='gist_rainbow_r')
plt.xlabel("stroke - hypertension", fontsize=20)
annot_plot(ax2)

ax3 = plt.subplot(323)
ax3  = sns.countplot(x="stroke",hue="heart_disease",data=df, palette="gist_rainbow_r")
plt.xticks(fontsize=20)
plt.xlabel("stroke-heart_disease", fontsize=20)
annot_plot(ax3)

ax4 = plt.subplot(324)
ax4 = sns.countplot(x="stroke",hue="ever_married",data=df, palette="gist_rainbow_r")
plt.xticks(fontsize=20)
plt.xlabel("stroke-ever_married", fontsize=20)
annot_plot(ax4)

ax5 = plt.subplot(325)
ax5 = sns.countplot(x = df.Residence_type,  hue= df.stroke,data=df, palette='gist_rainbow_r')
plt.xticks(fontsize=20)
plt.xlabel("stroke - Residence_type", fontsize=20)
annot_plot(ax5)

st.pyplot()

st.write("b.glocose")

fig = px.scatter_3d(df, x='age', y='avg_glucose_level', z='bmi',
              color='stroke', color_continuous_scale='bluered', opacity=0.5)
st.plotly_chart(fig)

st.write("b.cat")

coveriables=["smoking_status","work_type"]
fig,axes=plt.subplots(nrows=1,ncols=2,figsize=(15,5))
for i,item in enumerate(coveriables): #enumerate()函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。
    plt.subplot(1,2,(i+1))
    ax = sns.countplot(x=item,hue="stroke",data=df,palette="Pastel2")
    plt.xlabel(str(item))
    plt.title("stroke by "+str(item))
    i=i+1
    annot_plot(ax)
st.pyplot()

st.sidebar.write("3. Selección algoritmo de clasificación")
st.subheader(" 3. Selección algoritmo de clasificación")

st.sidebar.write("4. Programa Predictor (CLI)")
st.subheader(" 4. Programa Predictor (CLI)")
# if st.sidebar.button('Al cuestionario'):
col01, col02, col03 = st.columns(3)
with col02:
        st.markdown(f'<h1 style="color:#33ff33;font-size:24px;">{"cuestionario"}</h1>', unsafe_allow_html=True)
        # st.subheader("cuestionario")
col1, col2, col3 = st.columns(3)
with col1:
    genero = st.radio( 'tu genero es',('mujer', 'hombre'))
    edad = st.radio( 'tu edad entre',('>30', '30~50',"<50"))
    heart_disease = st.radio( 'tu heart_disease es',('yes', 'no'))
    ever_married = st.radio( 'tu estado civil',('soltero', 'Casado'))
with col2:
    work_type = st.radio( 'tu work_type es',('Private', 'employed',"Govt_job","children"))
    Residence_type = st.radio( 'tu Residence_type es',('Urban', 'Rural'))
    smoking_status = st.radio( 'tu smoking_status es',('formerly smoked', 'never smoked',"smokes"))
with col3:
    avg_glucose_level= st.radio( 'tu glucemia en ayunas entre',('>3.9', '3.9～6.1',"<6.1"))
    bmi= st.radio( 'tu bmi entre',('>10', '10～33',"<33"))
    stroke = st.radio( 'tu stroke es',('yes', 'no'))

# st.sidebar.write("3. ¿El último comentario comenzó en...?")
# start_time = st.sidebar.slider(
#      "¿El último comentario comenzó en...?",
#      min_value = datetime(2018, 1, 1),
#      max_value = datetime(2020, 1, 1),
#      value = datetime(2018, 1, 2),
#      format="MM/DD/YY")
# st.sidebar.write(start_time)
# if start_time != datetime(2018, 1, 2):
#     if datos.loc[datos['last_review']==start_time].empty:
#         st.subheader(f" 3. Pobrecito, no hay comentarios en este día {start_time}😭")
#     else:
#         st.subheader(f" 3. Todos los comentarios del día {start_time}")
#         st.write(datos.loc[datos['last_review']==start_time])

# st.sidebar.write("4.1 Análisis por host_name")
# st.subheader(" 4.1 Se puede ver que host_name está relativamente concentrado, lo que puede confirmar la conclusión extraída en las listas de host_calculadas en el tipo continuo anterior.Vamos a verlo en detalle.")
# arr = datos[['host_name','name']].groupby('host_name').count().sort_values(by='name', ascending=False)
# st.line_chart(arr)

# st.sidebar.write("4.2 Análisis por vnumericas")
# st.subheader(" 4.2 Evaluando correlación entre precio, número de noches mínimas, número de revisiones, calificación por mes (0 -100).")
# vnumericas = datos[["price", "minimum_nights","number_of_reviews","reviews_per_month"]]
# sns.heatmap(vnumericas.corr(), annot=True, cmap='Blues')
# st.pyplot()

# st.markdown("""
# Conclusión:
# -  R= 0.029 Existe nula correlación entre precio y número de noches mínimas.
# -  R= 0.00084 Existe nula correlación entre precio y número de revisiones.
# -  R= 0.023 Existe nula correlación entre precio y valoraciones por mes.
# -  R= 0.16 Existe nula correlación entre número de noches mínimas y valoraciones por mes.
# -  R= 0.0073 Existe nula correlación entre número de noches mínimas y número de revisiones.
# -  R= 0.48 Existe debil correlación entre número de revisiones y valoraciones por mes.
#     """)

# st.sidebar.write("5. Tokyo Alojamiento Mapa")
# st.subheader("5. Tokyo Alojamiento Mapa")
# map_data = pd.DataFrame(datos,columns=['latitude', 'longitude'])
# st.map(map_data)

# st.sidebar.write("6. Mapa distribución zona B&B")
# st.subheader("5. Mapa distribución zona B&B")
# values = datos.neighbourhood.value_counts()
# names = datos.neighbourhood.unique().tolist()
# fig = px.pie(datos, values=values, names=names)
# fig.update_traces(textposition='inside', textinfo='percent+label')
# st.plotly_chart(fig)

# st.subheader("Descubre explorando:")
# st.markdown("""
#             - Más del 40 % de las alojamientos se concentran en las tres áreas centrales de Tokyo, el distrito de 'Shibuya Ku', 'Sumida Ku' y 'Nerima Ku'.
#             - Para las áreas alrededor del distrito de  'Shibuya Ku', 'Sumida Ku' y 'Nerima Ku', la distribución de casas de familia también está cerca de los límites de estas tres áreas, especialmente 'Setagaya Ku' y 'Arakawa Ku'.
#             - Las áreas restantes están distribuidas de manera relativamente uniforme y no hay un centro obvio.
#             """)

# st.sidebar.write("7. Análisis por price")
# st.subheader(" 7. A continuación, continuaremos observando si el precio de las habitaciones en diferentes áreas será diferente")
# sns.histplot(datos['price'],color='b')
# st.pyplot()

# st.sidebar.write("8. Consulta los precios en cada región")
# st.subheader(" 8. Consulta los precios en cada región")
# a = datos[['neighbourhood','price']].groupby(['neighbourhood','price']).count().reset_index()
# option = st.sidebar.selectbox(
# '¿En qué región le gustaría ver un histograma de "Área -- Precios"?',names)
# plt.hist(a[a['neighbourhood']==option].price,color='pink')
# plt.ylabel("precios")
# plt.xlabel(option)
# st.pyplot() 

# st.sidebar.write("9. Categorizar precios")
# st.subheader(" 9. Categorizar precios")
# b = pd.DataFrame(datos['neighbourhood'].unique(),columns=['área'])
# b['precio alto'] = datos[['price','neighbourhood']].groupby('neighbourhood').max().price.tolist()
# b['precio bajo'] = datos[['price','neighbourhood']].groupby('neighbourhood').min().price.tolist()
# b['precio mediano'] = datos[['price','neighbourhood']].groupby('neighbourhood').median().price.tolist()
# b['25% de precio'] = datos[['price','neighbourhood']].groupby('neighbourhood').quantile(0.25).price.tolist()
# b['75% de precio'] = datos[['price','neighbourhood']].groupby('neighbourhood').quantile(0.75).price.tolist()
# b['cuartil'] = np.array(datos[['price','neighbourhood']].groupby('neighbourhood').quantile(0.75).price.tolist()) - np.array(datos[['price','neighbourhood']].groupby('neighbourhood').quantile(0.25).price.tolist())
# st.write(b)
# b['precio mediano'].max()

# st.sidebar.write("10. topc 10 más populares Airbnb")
# st.subheader(" 10. top 10 más populares Airbnb")
# avg_review = datos['number_of_reviews'].quantile(0.9)
# avg_month_review = datos['reviews_per_month'].quantile(0.9)
# print(avg_review)
# print(avg_month_review)
# popular_house = datos[(datos['number_of_reviews']>avg_review) & (datos['reviews_per_month']>avg_month_review)]
# st.write(popular_house.sort_values(by=['number_of_reviews','reviews_per_month'],ascending=False).head(10))
# st.markdown("""
# Del análisis anterior, se puede concluir que:
# -  La mayoría de las casas de familia más populares están en Shinjuku Ku (4 casas), algunas están en Katsushika Ku y Katsushika Ku y Taito Ku (2 cada una).
# -  Las 10 casas de familia más populares son Entire. Se considera temporalmente que si desea hacer casas de familia, el Entire puede ser una buena opción.
#     """)

# st.sidebar.write("11. Conclusiones")
# st.subheader("Conclusiones")
# st.markdown("""
# - Después de realizar el estudio por barrios, podemos determinar que más del 60% de los alojamientos se concentran en las tres áreas centrales de Tokyo, el distrito de 'Shibuya Ku', 'Sumida Ku' y 'Nerima Ku'. Zonas donde abundan museos, zonas de ocio y muy comerciales. 
# - Observamos que, por tipo de alojamiento, son alquilados por el siguiente orden:
# el 65,09% (7463) apartamentos completos
# 8.71% (999) habitaciones compartidas
# 26.20% (3004) habitaciones privadas 
# - Deducimos que el propietario prefiere alquilar un apartamento o casa completa. 
# - En cuanto al precio, hemos observado que existen 4 barrios donde su precio máximo coincide, siendo de 1000046 yenes:

# - Toshima Ku  1000046
# - Taito Ku  1000046
# - Chiyoda Ku  1000046
# - Nakano Ku  1000046
# -  Nos faltó descubrir si es casualidad o por normativa en Japón los precios máximos podrían coincidir,
# - El barrio más barato nos aparece Higashiyamato Shi 3013
#     """)

# if st.sidebar.button('gracias'):
#     st.balloons()
# else:
#     st.write(' gracias a todos!!!')
