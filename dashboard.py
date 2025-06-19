import dash
import dash_core_components as dcc
import dash_html_components as html

#create a dash application

app = dash.Dash(__name__)

#Define the application layout.

app.layout = html.Div(
    
    children=[
        html.H1('My Dashboard'),
        dcc.Graph(
            id = 'My-Graph',
            figure ={
                'Data' : [
                    {'X': [1,2,3],'Y':[4,1,2],'type':'bar','name':'Bar Chart'},
                    {'X': [1,2,3],'Y':[2,4,5],'type':'line','name':'Line Chart'},
                ],
                'layout': {
                    'title': 'Graph title',
                    'xaxis': {'title':'x-axis'},
                    'yaxis': {'title':'y-axis'}
                }
            }
        )
        
           ]
            
        )
    

#run the application

if __name__ == ' __main__ ':
 app.run_server(debug=True)
    