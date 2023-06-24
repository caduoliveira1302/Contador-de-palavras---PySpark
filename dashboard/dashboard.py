import pandas as pd
import plotly.express as px
import dash
from dash import Dash
from dash import dcc 
from dash import html
from dash.dependencies import Input, Output

app = Dash(__name__)

#import data
def read_csv(name):
    df_name = f"df_{name}"
    df_name = pd.read_csv(f"C:/Users/cedua/CDIA - PUCSP/PROJETO PySpark - SAVINO/Contador-de-palavras---PySpark/dashboard/final_df_{name}.csv")
    return df_name

df_fitnessandpower = read_csv("fitnessandpower")
df_gsup = read_csv("gsup")
df_healthline = read_csv("healthline")
df_maxtitanium = read_csv("maxtitanium")
df_myproteinblog = read_csv("myproteinblog")
df_nutritotal = read_csv("nutritotal")
df_nutrufy = read_csv("nutrufy")
df_proteinlicious = read_csv("proteinlicious")
df_reddit = read_csv("reddit")
df_sanavita = read_csv("sanavita")
df_suplementacao = read_csv("suplementacao")
df_tnation = read_csv("tnation")
df_tuasaude = read_csv("tuasaude")
df_twitter = read_csv("twitter")
df_general = read_csv("general")

#APP_LAYOUT
app.layout = html.Div([

    html.H1("WORD COUNT - PYSPARK", style={'text-align':'center'}),

    dcc.Dropdown(id='select_site_social',
                 options=[
                     {"label": "fitnessandpower", "value":df_fitnessandpower},
                     {"label": "gsup", "value":df_gsup},
                     {"label": "healthline", "value":df_healthline},
                     {"label": "maxtitanium", "value":df_maxtitanium},
                     {"label": "myproteinblog", "value":df_myproteinblog},
                     {"label": "nutritotal", "value":df_nutritotal},
                     {"label": "nutrufy", "value":df_nutrufy},
                     {"label": "proteinlicious", "value":df_proteinlicious},
                     {"label": "sanavita", "value":df_sanavita},
                     {"label": "SuplementAcao", "value":df_suplementacao},
                     {"label": "tnation", "value":df_tnation},
                     {"label": "tuasaude", "value":df_tuasaude},
                     {"label": "Reddit", "value":df_reddit},
                     {"label": "Twitter", "value":df_twitter}],
                multi = False,
                value = df_fitnessandpower,
                style={"width":"40%"}
                ),

    html.Div(id='output_container', children=[]),
    html.Br(),

    dcc.Graph(id='my_map', figure={}) 
])

#CONNECT THE PLOTLY GRAPHS WITH THE DASH COMPONENTS
@app.callback(
    [Output(component_id='output_container', component_property='children'),
     Output(component_id='my_map', component_property='figure')],
    [Input(component_id='select_site_social', component_property='value')]
)

def update_graph(option_slctd):
    print(option_slctd)
    print(type(option_slctd))

    # container = f"The site or social media chosen by user was: {option_slctd}"

    df_gen = df_general.copy()
    df_gen = df_gen[df_gen['site_social']==option_slctd]

    #Plotly Express
    fig = px.bar(df_gen, x='words', y='count', color='site_social')

    return fig







 






















if __name__ == '__main__':
    app.run_server(debug=True)