import dash
import dash_bootstrap_components as dbc
from dash import html
import dash_leaflet as dl
from dash import Input, Output
from sympy import true

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

PLOTLY_LOGO = "https://images.plot.ly/logo/new-branding/plotly-logomark.png"

basemap = dl.Map(dl.TileLayer(), style={'width': '1000px', 'height': '500px'})


search_bar = dbc.Row(
    [
        dbc.Col(dbc.Input(type="search", placeholder="Search")),
        dbc.Col(
            dbc.Button(
                "Search", color="primary", className="ms-2", n_clicks=0,
            ),
            width="auto",
        ),
    ],)
navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.Col(html.Img(src=PLOTLY_LOGO, height="30px")),
                        dbc.Col(dbc.NavbarBrand("Land Monitoring Products Visualizer", className="ms-2")),
                    ],
                    align="center",
                    className="g-0",
                ),
                href="https://plotly.com",
                style={"textDecoration": "none"},
            ),
            dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
            dbc.Collapse(
                # search_bar,
                id="navbar-collapse",
                is_open=False,
                navbar=True,
            ),
        ],
    ),
    color="#032b0d",
    dark=True,)




base = html.Div(
    dl.Map(
        [dl.LocateControl(options={'locateOptions': {'enableHighAccuracy': True}}),

        dl.MeasureControl(position="topleft", primaryLengthUnit="kilometers", primaryAreaUnit="hectares",
                              activeColor="#214097", completedColor="#972158"),
        # dl.WMSTileLayer(url="http://66.42.82.143:8600/geoserver/workspace/wms",
        #      layers="SC_RESAMPLED_RECLASS",format="image/png",transparent=true,),
            dl.LayersControl(
                [
                    dl.BaseLayer(
                        dl.TileLayer(),
                        name="OpenStreetMaps",
                        checked=True,
                    ),
             dl.BaseLayer(
                        dl.TileLayer(
                            url="https://www.ign.es/wmts/mapa-raster?request=getTile&layer=MTN&TileMatrixSet=GoogleMapsCompatible&TileMatrix={z}&TileCol={x}&TileRow={y}&format=image/jpeg",
                            attribution="IGN",
                        ),
                        name="IGN",
                        checked=False,
                    ),
                ],
            ),
            # get_data(),
        ],
        zoom=4,
        center=(0.0236, 37.9062),    
    ),
    style={
        "top":0,
        "bottom":0,
        "right":0,
        "left":0,
        "height": "100vh",
        "order":1,
        "z-index":"500",
    },
)

map =  html.Div(dl.Map([dl.TileLayer(), dl.WMSTileLayer(url='http://66.42.82.143:8600/geoserver/workspace/wms?service=WMS&version=1.1.0&request=GetMap&layers=workspace%3ACE_2020_RESAMPLED_RECLASS&bbox=21.811095098000237%2C-20.517387270765752%2C57.815521893970754%2C23.140534422176678&width=633&height=768&srs=EPSG%3A4326&styles=&format=image%2Fpng',
                                            layers="SC_RESAMPLED_RECLAS", format="image/png", transparent=False)],
           center=[0.0236, 37.9062], zoom=4,
           style= { "top":0,
        "bottom":0,
        "right":0,
        "left":0,
        "height": "100vh",
        "order":1,
        "z-index":"500",}),
)






#####SIDEBAR BOOTSTRAP

SIDEBAR_STYLE = {

    "position": "absolute",
    "top": 330,
    "left": 20,
    "bottom":80,
    "height":300,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#8ebf9c",
    "order":1,
    "z-index": "1000",
    "round":"80",
    "border-radius":"25px",
}

sidebar = html.Div(
      [
        html.P("Factors", className="display-6"),
        dbc.Checklist(
            options=[
                {"label": "Climate Erosivity", "value": "CE",},
                {"label": "Erodible Fraction", "value": "EF"},
                {"label": "Soil Crust", "value": "SC",},
                {"label": "Vegetation Sensitivity", "value": "VC"},
                {"label": "Surface Roughness", "value": "SR"},
            ],
            value=['CE'],
            id="checklist",
            switch=True,
            
        ),
   html.Div(id='out'),
    ],
    style=SIDEBAR_STYLE,
)

# html.Div(base,id='out')

# spinners = html.Div(
#     [
#         dbc.Spinner(color="primary"),
#         dbc.Spinner(color="secondary"), 
#     ]
# )



app.layout = html.Div([
navbar,
# spinners,
# map,
base,

sidebar,
],)



# @app.callback(
#     Output('out','children'),
#     Input('checklist', 'n-clicks'))
# def update_value(click):
#     if click=="CE":
#      return dl.Map([dl.TileLayer(),
#      dl.WMSTileLayer(url="http://66.42.82.143:8600/geoserver/workspace/wms",
#      layers="CE_2020_RESAMPLED_RECLASS",format="imgae/png",transparent=true,)]),

#     else:
#         None

    



if __name__ == '__main__':
    app.run_server(debug=True)