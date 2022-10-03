import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from datetime import datetime
from st_aggrid import AgGrid, GridOptionsBuilder
from st_aggrid.shared import GridUpdateMode

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

def aggrid_interactive_table(df: pd.DataFrame):
    """Creates an st-aggrid interactive table based on a dataframe.
    Args:
        df (pd.DataFrame]): Source dataframe
    Returns:
        dict: The selected row
    """
    options = GridOptionsBuilder.from_dataframe(
        df, enableRowGroup=True, enableValue=True, enablePivot=True
    )

    options.configure_side_bar()

    options.configure_selection("single")
    selection = AgGrid(
        df,
        enable_enterprise_modules=True,
        gridOptions=options.build(),
        #theme="light",
        update_mode=GridUpdateMode.MODEL_CHANGED,
        allow_unsafe_jscode=True,
    )

    return selection

#with dataset:
df1 = pd.read_csv('./tabla_interactiva_metricas.csv')
st.header("🖱️ Métricas de Evaluación Algoritmos de Clasificación")
st.write("Métricas de Evaluación 10 Algoritmos de Clasificación con la aplicación de 7 métdoos de balanceo de datos")
st.write("Haz click en una fila de la tabla debajo para visualizar las métricas, algoritmos y balanceo de tu interés!")
data1 = pd.read_csv('./tabla_interactiva_metricas.csv')
selection = aggrid_interactive_table(data1)
st.write("Los valores corresponden a los valores medio de cada categoría de datos seleccionados.")
st.write("Número total de datos del data set 4981")
st.markdown('Encontramos este dataset en https://www.kaggle.com/gato2021/best-clf-model-ictus/edit')  

##Gráficos interactivos con scatterplots

#with features2:
st.write(' ')
st.write(' ')
st.write(' ')
st.write(' ')
st.header('Comportamientos de las métricas de evaluación')
st.subheader('Veamos unos scatterplots por barrios y tipo de habitación')
#Las gráficas más segun la relacion de correlación mas fuerte con un muestro por barrios
st.text('Recall : Sensibilidad a los falsos positivos correctamente identificados')
col11, col21 = st.columns(2)
with col11:
    fig1 = px.scatter(df1, x='balance_method', y='recall', color='gridSearch', hover_name='gridSearch')
    st.text('Balance Accuracy : Exactitud del modelo ajustado a datos desbalanceados')
    st.plotly_chart(fig1)
with col21:
    fig2 = px.scatter(df1, x='balance_method', y='balanced_accucracy', color='gridSearch', hover_name='gridSearch')
    st.text('Overfitting (%) : Sobre aprendizaje de nuestro modelo.')
    st.plotly_chart(fig2)

fig3 = px.scatter(df1, x='balance_method', y='overfitting %', color='gridSearch', hover_name='gridSearch')
st.text('Recall -  Balance Accuracy - Overfitting (%) ')
st.plotly_chart(fig3)
fig4 = px.scatter_3d(df1, x='balanced_accucracy', y='overfitting %', z='recall',
              color='balance_method', color_continuous_scale='bluered', opacity=0.5 , size_max=18,)
# tight layout
fig4.update_layout(margin=dict(l=0, r=0, b=0, t=0),scene = dict(
                    xaxis_title='Balance Accuracy',
                    yaxis_title='Overfitting %',
                    zaxis_title='Recall'), 
                 width=900) 
st.plotly_chart(fig4)

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
