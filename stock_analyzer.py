#Imports
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

#Launching the application
app = dash.Dash()

#Use Alpha Vantage API to search up TSX stocks by adding .TO

#First div will contain input for the stock and the graph
app.layout = html.Div(children=[
    html.H1("My Stock Analyzer"),
    html.Div("Stock Price"),
    dcc.Graph(id='price',
        figure={'data': [
            go.Scatter(
                x=[1,2,3],
                y=[4,1,2],
                mode='lines',
                name='Price'
            )],
            'layout': go.Layout(title="Stock Price")
            })
])


#Runs the server
if __name__ == '__main__':
    app.run_server(debug=True, port=3004)