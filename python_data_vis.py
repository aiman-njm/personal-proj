import dash
from dash import dcc, html, Input, Output, State
import pandas as pd
import plotly.express as px
import io
import base64
import dash_bootstrap_components as dbc

# Initialize the Dash app with a modern theme
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])

# Default dataset (placeholder)
default_data = pd.read_csv(r'C:\Users\USER\Downloads\Most Popular Youtube Vids\cleaned_youtube_videos.csv')
print("Loaded dataset preview:")
print(default_data.head())  # Debugging step

def parse_contents(contents):
    try:
        content_type, content_string = contents.split(',')
        decoded = base64.b64decode(content_string)
        df = pd.read_csv(io.StringIO(decoded.decode('utf-8')))
        return df
    except Exception as e:
        print(f"Error reading uploaded file: {e}")
        return default_data  # Fall back to default data if there's an error

# Sidebar with filters
sidebar = dbc.Offcanvas([
    dbc.Label("Filter by Category:"),
    dcc.Dropdown(id='category-filter', options=[], placeholder="Select a Category", searchable=True,
                 style={"width": "100%", "padding": "5px", "borderRadius": "10px"}),
    dbc.Label("Filter by Year:"),
    dcc.RangeSlider(id='year-slider', min=2000, max=2025, step=1, 
                    marks={i: str(i) for i in range(2000, 2026) if i % 5 == 0},
                    value=[2000, 2025]),
], id="sidebar", title="Filters", is_open=False)

# Layout
app.layout = dbc.Container(fluid=True, children=[
    html.H1("YouTube Popular Videos Dashboard", className='text-center mb-4',
            style={'backgroundColor': '#1e1e2f', 'color': 'white', 'padding': '20px', 'borderRadius': '10px'}),
    
    dcc.Upload(
        id='upload-data',
        children=html.Button('Upload New CSV', className='btn btn-primary'),
        multiple=False,
        className='mb-4'
    ),
    
    html.Button("Toggle Filters", id="toggle-sidebar", className="btn btn-secondary mb-4"),
    
    sidebar,
    
    dbc.Row([
        dbc.Col(html.Div([
            html.H3("Total Views", className="text-center"),
            html.H4(id='total-views', className="text-center text-primary")
        ]), width=3),
        dbc.Col(html.Div([
            html.H3("Total Likes", className="text-center"),
            html.H4(id='total-likes', className="text-center text-success")
        ]), width=3),
        dbc.Col(html.Div([
            html.H3("Most Popular Category", className="text-center"),
            html.H4(id='popular-category', className="text-center text-warning")
        ]), width=3),
    ], className='mb-4 justify-content-center'),
    
    dbc.Row([
        dbc.Col(dcc.Graph(id='top-views-chart', style={'height': '650px'}), width=6),
        dbc.Col(dcc.Graph(id='category-pie-chart', style={'height': '650px'}), width=6),
    ], className='mb-4'),
    
    dbc.Row([
        dbc.Col(dcc.Graph(id='views-likes-trend', style={'height': '650px'}), width=6),
        dbc.Col(dcc.Graph(id='likes-vs-views', style={'height': '650px'}), width=6),
    ], className='mb-4'),
    
    html.Button("Download CSV", id='download-button', className='btn btn-success mt-4'),
    dcc.Download(id='download-dataframe-csv')
])

@app.callback(
    Output("sidebar", "is_open"),
    Input("toggle-sidebar", "n_clicks"),
    State("sidebar", "is_open"),
    prevent_initial_call=True
)
def toggle_sidebar(n_clicks, is_open):
    return not is_open

@app.callback(
    [Output('top-views-chart', 'figure'),
     Output('category-pie-chart', 'figure'),
     Output('views-likes-trend', 'figure'),
     Output('likes-vs-views', 'figure'),
     Output('category-filter', 'options'),
     Output('total-views', 'children'),
     Output('total-likes', 'children'),
     Output('popular-category', 'children')],
    [Input('upload-data', 'contents'),
     Input('category-filter', 'value'),
     Input('year-slider', 'value')]
)
def update_graphs(contents, selected_category, year_range):
    if contents:
        df = parse_contents(contents)
    else:
        df = default_data
    
    df = df[(df['published'] >= year_range[0]) & (df['published'] <= year_range[1])]
    if selected_category:
        df = df[df['Category'] == selected_category]
    
    total_views = f"{df['Video views'].sum():,.0f}"
    total_likes = f"{df['Likes'].sum():,.0f}"
    popular_category = df['Category'].mode()[0] if not df['Category'].empty else "N/A"
    
    # Restore Graphs
    fig_top_10 = px.bar(df.nlargest(10, 'Video views'), x='Video views', y='Video', orientation='h', title="Top 10 Most Viewed Videos")
    fig_category = px.pie(df, names='Category', title="Category Distribution")
    fig_trend = px.line(df.groupby('published').sum().reset_index(), x='published', y=['Video views', 'Likes'], title="Views and Likes Trend")
    fig_likes_vs_views = px.scatter(df, x='Video views', y='Likes', title="Likes vs Views Correlation")
    
    return fig_top_10, fig_category, fig_trend, fig_likes_vs_views, [{'label': cat, 'value': cat} for cat in df['Category'].unique()], total_views, total_likes, popular_category

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
