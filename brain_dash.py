from dash import Dash, dcc, html, dash_table
from dash.dependencies import Input, Output
import numpy as np
import pandas as pd
import plotly.express as px

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = Dash(__name__,suppress_callback_exceptions=True, external_stylesheets=external_stylesheets)

df = pd.read_csv('stroke_dataset.csv')
df["age"] = df["age"].astype(float).astype(int)
df["smoking_status"].replace("Unknown",np.nan,inplace=True)
df["smoking_status"].fillna(df["smoking_status"].mode()[0],inplace=True)
df = df.drop_duplicates()

df1 = pd.read_csv('./tabla_dash.csv')


# peso_variables = pd.read_csv('../peso_variables.csv')

# RocReport().run(Dataset(peso_variables, label='transformer_var_numer__stroke'), modelo_recuperado)

app.layout = html.Div([
    html.Div([
        html.Div(
            html.Img(src='/assets/CONNECTING-removebg-preview.png',height=600,className="logo_title")
            ),
            html.Div(html.H1('Could you have stroke?',className="header-title")),
            html.Div(
            html.Img(src='/assets/68499746e00ab264fe8fcea0894f8aca.gif',height=600,className="logo_title")
            ),
        ],className="wrap"),
    
    dcc.Tabs(id="tabs-example-graph", value='tab-0-example-graph', children=[
        dcc.Tab(label='Connecting', value='tab-0-example-graph'),
        dcc.Tab(label='Análisis y Visualización de dataset', value='tab-1-example-graph'),
        dcc.Tab(label='Selección Modelo Predictor', value='tab-2-example-graph'),
        dcc.Tab(label='Informe de Clasificación', value='tab-3-example-graph'),
        dcc.Tab(label='Programa Predictor (CLI)', value='tab-4-example-graph'),
        dcc.Tab(label='Repositorio Proyecto Ictus', value='tab-5-example-graph'),
    ]),
    html.Div(id='tabs-content-example-graph')
],
className="header-style"
,)

@app.callback(Output('tabs-content-example-graph', 'children'),
              Input('tabs-example-graph', 'value'))
def render_content(tab):
    if tab == 'tab-0-example-graph':
        return html.Div([
           html.H1("¿Quiénes somos Connecting?",className="header-title2"),
           html.P(
            children="Somos una empresa dedicada al análisis de datos"
             " en el sector de la medicina con el propósito de crear nuevas herramientas "
             "para ayudar a los profesionales de la salud y áreas afines al campo , "
             "en la detección, prevención y tratamiento de enfermedades.",
             className="header-present",
             ),
            html.Img(
            src='/assets/unknown.png',
            height=600
            ),
         dcc.Markdown('''
            - Begoña Ortiz    -------   Data Analyst
            - Celeste López  -------  graphic designer
            - Stephany Valderrama   -------  Data scientist
            - Wenya  Li   -------   Front-end Developer
            - Sebastian Degaudenci  -------   Back-end Developer
             #### IA Schooll
            ''', className="header-present"),
            html.Img(
            src='/assets/Imagen1.png',
            height=600,
            className="logo"
            ),
        ],className="center")
    if tab == 'tab-1-example-graph':
        return html.Div([
            html.P(
                children="En nuestro proyecto buscamos analizar la relación entre el accidente cerebrovascular (stroke) "
                 " y posibles factores de riesgo como el género, la edad, el azúcar en sangre, entre otros. ",
                  className="header-description",
                  ),
            html.P(
                children=" Accidente cerebrovascular ",
                  className="header-description2",
                  ),
            dcc.Markdown('''
            - Un accidente cerebrovascular sucede cuando el flujo de sangre a una parte del cerebro se detiene. Algunas veces, se denomina "ataque cerebral".
            - Si el flujo sanguíneo se detiene por más de pocos segundos, el cerebro no puede recibir nutrientes y oxígeno. Las células cerebrales pueden morir, lo que causa daño permanente.
            - Un accidente cerebrovascular se presenta cuando un vaso sanguíneo en el cerebro se rompe, causando un sangrado dentro de la cabeza.
            ''', className="header-present"),
            
            html.Div([
                dcc.Graph(figure=px.bar(df, x="gender",y="stroke", title="Relación Stroke por Género")),
                dcc.Graph(figure=px.bar(df, x="hypertension",y="stroke", title="Relación Stroke con Hipertensión")),
                dcc.Graph(figure=px.bar(df, x="heart_disease",y="stroke", title="Relación Stroke con enfermedades cardiacas")),
                dcc.Graph(figure=px.bar(df, x="ever_married",y="stroke", title="Relación Stroke con estado civil")),
                dcc.Graph(figure=px.bar(df, x="Residence_type",y="stroke", title="Relación Stroke con tipo de vivienda")),
                dcc.Graph(figure=px.bar(df, x="smoking_status",y="stroke", title="Relación Stroke con fumar")),
                dcc.Graph(figure=px.bar(df, x="work_type",y="stroke", title="Relación Stroke con vida laboral")),
                dcc.Graph(figure=px.scatter_3d(df, x='age', y='avg_glucose_level', z='bmi',
                color='stroke', color_continuous_scale='bluered', opacity=0.5)),
                ],style = {'columnCount':3})
        ])
    elif tab == 'tab-2-example-graph':
        return  html.Div([
            dash_table.DataTable(
            id='datatable-interactivity',
            data=df1.to_dict('records'),
            columns=[{'id': c, 'name': c, "selectable": True} for c in df1.columns],
            editable=True,
            # filter_action="native",
            # sort_action="native",
            # sort_mode="multi",
            # column_selectable="single",
            # row_selectable="multi",
            # row_deletable=True,
            # selected_columns=[],
            # selected_rows=[],
            # page_action="native",
            # page_current= 0,
            page_size=10,
            style_table={'overflowX': 'auto','padding-top':'30px'},
            ),
            html.Div(id='datatable-interactivity-container'),
            dcc.Graph(figure=px.scatter_3d(df1, x='Balanced Accuracy', y='Overfitting (%)', z='Recall',color='Método de Balanceo', color_continuous_scale='bluered', opacity=0.5 , size_max=18,))
            ])
    elif tab == 'tab-3-example-graph':
        return html.Div([
            html.Div([
                html.H6("Modelo de ML Predictor de Stroke"),
                html.Img(src='/assets/1.png')],style={"padding-top":"30px"}),
            html.Div([
                html.Div([
                    html.H6("Métricas de Evaluación del Modelo"),
                    html.Img(src='/assets/2.png'),]),
                html.Div([
                    html.H6("Matriz de Confusión del Modelo"),
                    html.Img(src='/assets/3.png')]), 
                html.Div([
                    html.H6("Relación de la exactitud y precisión "),
                     html.H6("de nuestro modelo (Área bajo la Curva: ROC_AUC)"),
                    html.Img(src='/assets/4.png')]),
                ],className="wrap",style={"padding":"30px"}), 
             html.Div([
                html.H6("Modelo de ML Predictor de Stroke"),
                 html.Img(src='/assets/6.png'),]),
        ],className="center")
    elif tab == 'tab-4-example-graph':
        return html.Div([
            html.H3("Preguntas actuales para predecir Ictus con nuestro modelo",className='content-title'),
            html.Div([
                html.Label('Género:',className="question_title"),
                html.Label('Indica tu edad en años:',className="question_title"),
                html.Label('¿Alguna vez has tenido un ataque al corazón?',className="question_title"),
                html.Label('Indica tú estado civil (si aplica o no):',className="question_title"),
                html.Label('Indica tú tipo de trabajo (si aplica o no):',className="question_title"),
                html.Label('Indica tú tipo de residencia:',className="question_title"),
                html.Label('Indica si fumas:',className="question_title"),
                html.Label('Indica tu índice de glucosa (preferiblemente en ayunas):',className="question_title"),
                html.Label('Indica tu altura (en centímetros) / peso (en kilogramos):',className="question_title"),
                html.Label('¿Has tenido un ictus?',className="question_title"),
                html.Label('Enviar información',className="question_title"),
            
                dcc.RadioItems(['Mujer', 'Hombre'],'mujer', inline=True,className="question"),
                dcc.Input(id="dfalse", type="number",placeholder="Debounce False",className=
                "input_margin"),
                # dcc.RadioItems([{'>30', '30~50',"<50"}], '>30',inline=True,className="question"),
                dcc.RadioItems(['Sí', 'No'], 'yes',inline=True,className="question"),
                dcc.RadioItems(['Soltero', 'Casado'], 'soltero',inline=True,className="question"),
                dcc.RadioItems(['Privado','Autónomo',"Gubernamental","No trabajas"], 'Private',inline=True,className="question"),
                dcc.RadioItems(['Urban', 'Rural'], 'Urban',inline=True,className="question"),
                dcc.RadioItems(['Fumador Ocasional ', 'No fuma',"Fumador"], 'formerly smoked',inline=True,className="question"),
                dcc.Input(id="dtrue", type="number", placeholder="Debounce False",className=
                "input_margin"),
                html.Br(),
                 dcc.Input(id="dfalse2", type="number",placeholder="Debounce False",className=
                "input_margin"),
                 dcc.Input(id="input_range_2", type="number", placeholder="Debounce False",className=
                "input_margin"),
                #dcc.RadioItems(['>3.9', '3.9~6.1',"<6.1"], '>3.9',inline=True,className="question"),
                #dcc.RadioItems(['>10', '10~33',"<33"], '>10',inline=True,className="question"), 
                dcc.RadioItems(['Sí', 'No'], 'yes',inline=True,className="question"),
                dcc.ConfirmDialogProvider(
                    children=html.Button('Click Me',className= "botton"),
                    id='danger-danger-provider',
                    message='Danger danger! Are you sure you want to continue?'
                    ),
            ],style = {'columnCount':2}),
             html.H3("Generación de nueva información para mejorar la predicción del Ictus en un futuro",className='content-title'),
            html.Div([
                dcc.Markdown('''
                - ¿Has sufrido un ictus antes?
                -¿Has sufrido pérdida de sensibilidad en uno de los dos lados de la cara?
                - ¿Cuándo sonríes la parte izquierda o derecha de la boca no se mueve?
                - ¿Has sentido hormigueo en el rostro?
                - ¿Te cuesta articular palabras?
                - Levanta los brazos al frente.  ¿Te ha quedado uno mas bajo que el otro o uno de los brazos cae desplomado?
                - ¿Has tenido perdida de vision repentina?
                - ¿Pierdes la visión de uno o de los dos ojos durante momentos?
                - ¿Sufres de migrañas?
                - ¿Tienes dificultad para caminar o sientes desequilibrio?
                - ¿Presentas o has presentado pérdida repentina de memoria?
                - ¿Ha empezado con la menopausia?
                - ¿Tomas anticonceptivos (hormonales o no hormonales?
                - ¿Presentas antecedentes familiares de ictus?
                - Si la respuesta es SI , indica si en padre, madre o abuelos.
                ''', className="header-present1"),
                html.Div(
                    html.Img(src='/assets/peter-griffin.gif',height=500,style={'margin-top':'30px'})
                    ),
            ],style = {'columnCount':2})
        
        ])
    elif tab == 'tab-5-example-graph':
        return html.Div([
             html.Div([
                html.Div([
                    html.Img(src='/assets/codigo.png'),]),
                html.Div([
                    html.Img(src='/assets/5.png')]), 
              
                ],className="wrap1",style={"padding":"30px"}), 
        ]),
# @app.callback(
#     Output('datatable-interactivity', 'style_data_conditional'),
#     Input('datatable-interactivity', 'selected_columns')
# )
# def update_styles(selected_columns):
#     return [{
#         'if': { 'column_id': i },
#         'background_color': '#D2F3FF'
#     } for i in selected_columns]

@app.callback(
    Output('datatable-interactivity-container', "children"),
    Input('datatable-interactivity', "derived_virtual_data"),
    Input('datatable-interactivity', "derived_virtual_selected_rows"))
def update_graphs(rows, derived_virtual_selected_rows):
    if derived_virtual_selected_rows is None:
        derived_virtual_selected_rows = []
    dff = df1 if rows is None else pd.DataFrame(rows)
    colors = ['#7FDBFF' if i in derived_virtual_selected_rows else '#0074D9'
              for i in range(len(dff))]
    return [
        dcc.Graph(id=column,figure=px.line(dff, x=dff["Método de Balanceo"], y=dff[column], color=dff["Algoritmo"],markers={"color": colors},))
        for column in ["Recall", "Overfitting (%)", "Balanced Accuracy","F1","ROC_AUC"] if column in dff
    ]

@app.callback(
    Output('output-provider', 'children'),
    Input('danger-danger-provider', 'submit_n_clicks'))
def update_output(submit_n_clicks):
    if not submit_n_clicks:
        return ''
    return """
        It was dangerous but we did it!
        Submitted {} times
    """.format(submit_n_clicks)

@app.callback(
    Output("number-out", "children"),
    Input("dfalse", "value"),
    Input("dfalse2", "value"),
    Input("dtrue", "value"),
    Input("input_range_2", "value"),
)
def number_render(fval, tval, rangeval):
    return "dfalse: {}, dtrue: {}, range: {}".format(fval, tval, rangeval)


if __name__ == '__main__':
    app.run_server(debug=True)