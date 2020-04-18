import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.H1("¡Hola Mundo!"),
    dcc.Graph(
        id='my_first_graph',
        figure={
            'data': [
                {'x':[1,2,3], 'y':[23,15,22], 'type':'line', 'name':'line'},
                {'x':[1,2,3], 'y':[5,2,8], 'type':'bar', 'name':'bar'}
            ],
            'layout':{
                'title':'Mi primer grafico con Dash'
            }
        }
        ),
        dcc.Input("Input")
])

if __name__ == "__main__":
    app.run_server(debug=True)