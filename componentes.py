import dash
import dash_core_components as dcc 
import dash_html_components as html 
import numpy as np 
from datetime import datetime as dt 
import plotly.graph_objects as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.H1("Componentes Principales"),

    # Dropdown y Slider
    html.Div([
        dcc.Dropdown(
            id = 'dropdown-component',
            options = [
            {'label':'Big Data', 'value':'bigdata'},
            {'label':'Data Science', 'value':'datascience'}, #, 'disabled':True
            {'label':'Base de Datos', 'value':'database'},
            {'label':'Web', 'value':'web'}
        ],
        placeholder="Selecciona una categoria",
        multi=True,
        searchable=True,
        value='bigdata',
        disabled=False,
        className='six columns'
        )
    ], className="row"),
    # RangeSlider e Input
    html.Div([
        dcc.Slider(
            id='slider-component',
            min=0,
            max=100,
            step=5,
            value=0,
            updatemode='mouseup',
            marks={int(i):f'{i}%' for i in np.arange(0,101,5)},
            className='nine columns'
        )
    ], style={'padding-top':'5%'}, className="row"),
    
    html.Div([
        dcc.RangeSlider(
            id='rangeslider-component',
            min=0,
            max=100,
            step=5,
            marks={int(i):f'{i}%' for i in np.arange(0,101,5)},
            value=[50, 100],
            pushable=10,
            allowCross=False
        )
    ], className='nine columns', style = {'padding-top':'5%'}),
    # RangeSlider e Input
    html.Div([
        dcc.Input(
            id='my-input',
            placeholder="Escribe tu nombre",
            type="text", #"password"
            value='',
            autoFocus=True,
            disabled=False,
            maxLength=20
        )
    ], className = 'three columns', style = {'padding-top':'5%'}),


    # Text Area, Checkbox y Radio item
    html.Div(id = 'text-check-radio', children = [
        html.H3("Text Area, Checkbox y Radio item"),
        dcc.Textarea(
            id = 'textarea',
            placeholder = 'Escribe aquí tu texto',
            value = '',
            cols = 10,
            rows = 10,
            autoFocus = 'True',
            disabled = False,
            lang = 'es',
            draggable = True,
            readOnly = False,
            title = "Titulo"
        ),
        dcc.Checklist(
            id = 'checklist',
            options = [
                    {'label':'Big data', 'value':'bigdata'},
                    {'label':'Data Science', 'value':'datascience', 'disabled':True},
                    {'label':'Bases de datos', 'value':'database'},
                    {'label':'Web', 'value':'web'}
                ],
            value = ['bigdata', 'database'],
            # labelStyle = {'display':'inline-block'}
        ),
        dcc.RadioItems(
            id = 'radio-items',
            options = [
                    {'label':'Big data', 'value':'bigdata'},
                    {'label':'Data Science', 'value':'datascience', 'disabled':True},
                    {'label':'Bases de datos', 'value':'database'},
                    {'label':'Web', 'value':'web'}
                ],
            value = 'bigdata',
            className = 'six columns',
            labelStyle = {'display':'inline-block'}
        )
    ], className = 'row'),
    #Buttom, Dates y Markdown
    html.Div(id='buttom-dates-markdown', children = [
        html.H3("Buttom, dates y markdown"),
        html.Button(
            'Enviar',
            id = 'buttom'
        ),
        dcc.DatePickerSingle(
            id = 'date-single',
            min_date_allowed=dt(1900, 1, 1),
            max_date_allowed=dt.today(),
            initial_visible_month=dt.today(),
            date=str(dt.today()),
            clearable = False,
            with_portal = False,
            display_format = 'YYYY-MM-DD',
            stay_open_on_select = False
        ),
        html.Div([
            dcc.DatePickerRange(
                id = 'date-range',
                start_date_placeholder_text = "Seleccione ida",
                end_date_placeholder_text = "Seleccione vuelta",
                minimum_nights=5,
                display_format = 'YYYY MM DD',
                with_portal = True
            )
        ], className = 'row', style = {'padding-top':'4%'}),
        dcc.Markdown(
            '''
            ##### Markdown
            Este es un texto en **markdown**, el cual es *interpretado*.
            '''
        )
    ]),
    # Upload, pestanyas y graficos
    html.Div(id = 'upload-tabs-graph', children = [
        dcc.Upload(
            id='upload-data',
            children=html.Div([
                'Arrastra tus ficheros o ',
                html.A('Selecciona')
            ]),
            style={
                'width': '50%',
                'height': '60px',
                'lineHeight': '60px',
                'borderWidth': '1px',
                'borderStyle': 'dashed',
                'borderRadius': '5px',
                'textAlign': 'center',
                'margin': '10px'
            },
        # Allow multiple files to be uploaded
            multiple=True),
        html.Div(children = [
            dcc.Tabs(id = 'tabs', value = 'contenido', children = [
                dcc.Tab(
                    id = 'contenido', 
                    value = 'contenido', 
                    label = 'Contenido',
                    children = [
                        html.Div([
                            html.H5("Contenido de cursos"),
                            dcc.Markdown('''
                                Este contenido aparece en la pestaña 1.
                            ''')
                        ])
                    ]),
                dcc.Tab(
                    id = 'opiniones', 
                    value = 'opiniones', 
                    label = 'Opiniones',
                    children = [
                        dcc.Graph(
                            id = 'my-graph',
                            figure={
                                'data': [
                                    {'x': [1, 2, 3], 'y': [23, 15, 22], 'type': 'line', 'name': 'line'},
                                    {'x': [1, 2, 3], 'y': [5, 2, 8], 'type': 'bar', 'name': 'bar'},
                                ],
                                'layout': {
                                    'title': 'Mi primer grafico con Dash'
                                }
                            }
                        )
                    ])    
                ]),
            ])
        ], className = 'row'),

    # ])





])

if __name__ == "__main__":
    app.run_server(debug=True)