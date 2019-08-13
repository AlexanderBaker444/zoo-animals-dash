import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

########### Set up the chart

myfavoritecolor='purple'
x_list=['Pie', 'Cake', 'Cupcakes']
y_list=y=[10, 15, 20]

data = [go.Bar(
            x=x_list,
            y=y_list,
            marker=dict(color=myfavoritecolor)
    )]

layout = go.Layout(
    title = 'Inventory in Bakery', # Graph title
    xaxis = dict(title = 'Type of dessert'), # x-axis label
    yaxis = dict(title = 'Number in the bakery'), # y-axis label

)
fig = go.Figure(data=data, layout=layout)


########### Display the chart

app = dash.Dash()
server = app.server

app.layout = html.Div(children=[
    html.H1('Desserts in Bakeries'),
    dcc.Graph(
        id='figure-1',
        figure=fig
    ),
    html.A('Code on Github', href='https://github.com/AlexanderBaker444/zoo-animals-dash'),
    html.Br(),
    html.A('HTML Color Codes', href='https://htmlcolorcodes.com'),


    ]
)

if __name__ == '__main__':
    app.run_server()
