i = 0
# exit()
# Read all CSV files
# if i == 0:
#     df = read_csv()
#     df = df.drop_duplicates(subset=df.columns.difference(['Volgnummer']))
#     i = 1

# df = pandas.read_csv(dir_path, sep=";", decimal=',', keep_default_na=False, dayfirst=True, parse_dates=[1])
# print(df.dtypes)
# print(df.shape)

# file_manager.writer(df)
# exit()
# print(df.shape)
# df.to_csv('test2.csv')

# for numbers in df['Rekeningnummer'].unique():
#     df[numbers] = df[df['Rekeningnummer'] == numbers]['Bedrag']
#     #df[numbers] = df[numbers].fillna(0)[::-1].cumsum()
#
# df['Total'] = df['Bedrag'].fillna(0)[::-1].cumsum()
# # ax.plot(df['Uitvoeringsdatum'], df[numbers])
#
# dt = df.groupby(['Uitvoeringsdatum'])[df['Rekeningnummer'].unique()].agg(['first']).reset_index()
# print(dt.dtypes)

# # ax1.plot(dt[dt.columns[0]],dt[dt.columns[1]],linewidth=0.5,zorder=1, label = "Force1")
# # ax1.plot(dt[dt.columns[0]],dt[dt.columns[2]],linewidth=0.5,zorder=1, label = "Force2")
# # ax1.plot(dt[dt.columns[0]],dt[dt.columns[3]],linewidth=0.5,zorder=1, label = "Force2")
# trace1 = go.Scatter(
#     x=dt.columns[0],
#     y=dt.columns[1],
#     yaxis="y1"
# )
# trace2 = go.Scatter(
#     x=dt.columns[0],
#     y=dt.columns[2],
#     yaxis="y2"
# )
# trace3 = go.Scatter(
#     x=dt.columns[0],
#     y=dt.columns[3],
#     yaxis="y3"
# )
# data = [trace1, trace2, trace3]
# layout = go.Layout(
#     yaxis=dict(
#         domain=[0, 0.33]
#     ),
#     legend=dict(
#         traceorder="reversed"
#     ),
#     yaxis2=dict(
#         domain=[0.33, 0.66]
#     ),
#     yaxis3=dict(
#         domain=[0.66, 1]
#     )
# )
# fig = go.Figure(data=data)
# fig.show()
# dg = df[df['Rekeningnummer'] == df['Rekeningnummer'].unique()[0]]
#
# # print(df.shape[0])
# #
# print(df.dtypes)
# # dt=df.groupby(['Rekeningnummer'])
# print('─' * 76)
# print(df.groupby(['Uitvoeringsdatum', 'Rekeningnummer'])['Bedrag'].agg('sum'))
# dt = df.groupby(['Uitvoeringsdatum', 'Rekeningnummer'])['Bedrag'].agg('sum')
# print('─' * 76)
# print(df.groupby(['Rekeningnummer'])['Bedrag'].sum())
# print('─' * 76)
# # time.sleep(5)
# # for x in range(0, df.shape[0]-1):
# #     print('─' * 76)
# #     print(df.loc[x, :])
# #     time.sleep(2)
#
# print(df['Rekeningnummer'].unique()[0])
# dj = df[df['Details'].str.contains("Pfizer", na=False)]
# ds = df.groupby([pd.Grouper(key='Uitvoeringsdatum', freq='M'), 'Rekeningnummer']).sum().reset_index()
# fig = ds.plot()
# fig.show()
#
# ds = df.groupby(pd.Grouper(key='Uitvoeringsdatum', freq='Y')).sum()
# fig = ds.plot()
# fig.show()
# plt.plot(df.loc[:,'Uitvoeringsdatum'],df.loc[:,'Bedrag']
# df.convert_dtypes()
# print(df.dtypes)
# print(df.describe())
# plt.show()
#
# Verrichting.f()

# csv.reader()
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/


# -------------------------------------------------------------------------------------------------------------------------------
# app = dash.Dash(__name__)
#
# app.layout = html.Div(
#     style={
#         'backgroundColor': 'lightgrey'
#     },
#     children=[
#         html.Div([
#             html.H1("Personal Finance Application", style={'font-family': 'Verdana'}),
#             dcc.Tabs(id="tabs-example-graph", value='tab-1-example-graph', style={'font-family': 'Verdana', 'borderColor': 'gold'},
#                      children=[
#                          dcc.Tab(label='Bankrekening overzicht', value='tab-1-grafiek'),
#                          dcc.Tab(label='Settings', value='tab-2-settings'),
#                      ],
#                      colors={
#                          "border": "darkgrey",
#                          "primary": "blue",
#                          "background": "lightgrey"}),
#             html.Br(),
#         ]),
#         html.Div([
#
#             html.Div(id='tabs-content-example-graph'),
#             html.Br(),
#             html.Div(id='test', children=[
#                 # html.H4('Bankrekening overzicht', style={'font-family': 'Verdana'}),
#                 dcc.Graph(id="time-series-chart", style={'width': '90vh', 'height': '60vh', "backgroundColor": 'grey'}),
#                 html.P("Selecteer ING rekening:", style={'font-family': 'Verdana'}),
#                 dcc.Checklist(
#                     id="ticker",
#                     options=list(filter(lambda x: len(x) >= 14, df['Rekeningnummer'].unique())) + ['Totaal'],
#                     value=list(filter(lambda x: len(x) >= 14, df['Rekeningnummer'].unique())) + ['Totaal'],
#                     style={'font-family': 'Verdana'},
#                     inline=True
#                 ),
#                 html.Br(),
#                 html.P("Selecteer aggregatie niveau", style={'font-family': 'Verdana'}),
#                 dcc.RadioItems(
#                     id="ticker2",
#                     options=[
#                         {'label': 'Dag', 'value': 'D'},
#                         {'label': 'Week', 'value': 'W'},
#                         {'label': 'Maand', 'value': 'M'},
#                         {'label': 'Jaar', 'value': 'Y'},
#                     ],
#                     value='M',
#                     style={'font-family': 'Verdana'},
#                     inline=True
#                 ),
#             ]),
#         ]),
#         html.Br(),
#         html.Div(id='table', children=[
#             dash_table.DataTable(data=df_extended[df_extended['Volgnummer'] != 'NaN'].to_dict('records'), columns=[{"name": i, "id": i} for i in df_extended.columns],
#                                  style_data={
#                                      'whiteSpace': 'normal',
#                                      'height': 'auto',
#                                  }, )
#         ]),
#         html.Div(children=[
#             html.Br(),
#             dcc.Upload(
#                 id='upload-data',
#                 children=html.Div([
#                     'Drag and Drop or ',
#                     html.A('Select Files')
#                 ]),
#                 style={
#                     'width': '100%',
#                     'height': '60px',
#                     'lineHeight': '60px',
#                     'borderWidth': '1px',
#                     'borderStyle': 'solid',
#                     'borderColor': 'gold',
#                     'borderRadius': '5px',
#                     'textAlign': 'center',
#                     'margin': '10px',
#                     'font-family': 'Verdana'
#                 },
#                 # Allow multiple files to be uploaded
#                 multiple=True
#             ), ])
#     ])
#
#
# @app.callback(
#     Output("time-series-chart", "figure"),
#     Input("ticker", 'value'),
#     Input("ticker2", 'value')
# )
# def display_time_series(input_rekeningnummer, input_frequentie):
#     if input_rekeningnummer != 0:
#         # Calculate total
#         dr_total = df.groupby([pd.Grouper(key='Uitvoeringsdatum', freq=input_frequentie)]).sum().cumsum().reset_index()
#         # print(dr_total.dtypes)
#
#         dr = df.groupby([pd.Grouper(key='Uitvoeringsdatum', freq=input_frequentie), 'Rekeningnummer']).sum().groupby(level=1).cumsum().reset_index()
#         for rekeningnummers in df['Rekeningnummer'].unique():
#             # print(rekeningnummers)
#             dr = pd.concat([dr, dr.query('Rekeningnummer in @rekeningnummers').iloc[-1:]], ignore_index=True)
#             dr.loc[-1, 'Uitvoeringsdatum'] = date.today()
#             # dr['Bedrag'].iloc[-1] = 0
#
#         dr_sum = pd.concat([dr, dr_total]).fillna("Totaal")
#         dg = dr_sum.query('Rekeningnummer in @input_rekeningnummer')
#         # dr2= []
#         # for aantal_rekeningnummers in input_rekeningnummer:
#
#         fig = px.line(dg, x='Uitvoeringsdatum', y='Bedrag', color='Rekeningnummer',
#                       # hover_name='Uitvoeringsdatum',
#                       # hovertemplate='Bedrag: %{y:$.2f}',
#                       hover_data={'Uitvoeringsdatum': "|%d %B %Y", 'Bedrag': ":.2f"},
#                       line_shape="hv",
#                       # hover_data={dr['Uitvoeringsdatum'][dr['Rekeningnummer'] == ticker]: "|%d %B %Y", dr['Bedrag'][dr['Rekeningnummer'] == ticker]: "|%.2f"},
#                       )
#         fig.update_layout(hovermode="x unified",
#                           # transition_easing='bounce-in',
#                           # transition_duration=5000
#                           )
#         fig.update_traces(mode="lines")
#
#         fig.update_layout(paper_bgcolor="lightgrey")
#
#         fig.update_layout(legend=dict(
#             orientation="h",
#             yanchor="bottom",
#             y=1.01,
#             xanchor="center",
#             x=0.50
#         ))
#
#     return fig
# -------------------------------------------------------------------------------------------------------------------------------

# fig = px.line(dr, x=dr['Uitvoeringsdatum'][dr['Rekeningnummer'] == input_rekeningnummer], y=dr['Bedrag'][dr['Rekeningnummer'] == input_rekeningnummer]

# fig = px.line(dr, x=dr['Uitvoeringsdatum'][dr['Rekeningnummer'].apply(lambda x: any(item for item in input_rekeningnummer if item in x))], y=dr['Bedrag'][dr['Rekeningnummer'].apply(lambda x: any(item for item in input_rekeningnummer if
# item in x))]
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SUPERHERO])

# Sidebar style
sidebar_style = {
}

sidebar = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H2('Sidebar', className='display-4'),
                html.Hr(),
                html.P('Different pages of the program', className='text-muted'),
                dbc.Nav(
                    [
                        dbc.NavLink('Page 1', href='/page-1', active='exact'),
                        dbc.NavLink('Page 2', href='/page-2', active='exact')
                    ],
                    vertical=True,
                    pills=True),
                html.Hr(),
            ]
        )

    ],
    style={'height': '100vh', 'width': '16rem', 'position': 'fixed'}
)
# tab1_content = dbc.Card(
#     dbc.CardBody(
#         [
#             html.P("This is tab 1!", className="card-text"),
#             dbc.Button("Click here", color="success"),
#         ]
#     ),
#     className="mt-3",
# )
#
# tab2_content = dbc.Card(
#     dbc.CardBody(
#         [
#             html.P("This is tab 2!", className="card-text"),
#             dbc.Button("Don't click here", color="danger"),
#         ]
#     ),
#     className="mt-3",
# )

# app.layout = dbc.Container(
#     # https://www.youtube.com/watch?v=1nEL0S8i2Wk
#     # https://dash-bootstrap-components.opensource.faculty.ai/docs/components/layout/
#     # https://getbootstrap.com/docs/5.0/utilities/sizing/
#     dbc.Row(
#         [
#             dbc.Col(
#                 [
#                     dcc.Location(id='sidebar_location'),
#                     sidebar
#                 ],
#                 width=3
#             ),
#             dbc.Col(
#                 [
#                     dbc.Row(
#                         [
#                             html.H1('Personal Finance'),
#                             html.Hr(),
#                         ]),
#                     dbc.Row(
#                         [
#                             dcc.Graph(id="time-series-chart", figure={}, style={'width': '90vh', 'height': '60vh', "backgroundColor": 'grey'}),
#                             html.P("Selecteer ING rekening:", style={'font-family': 'Verdana'}),
#                             dcc.Checklist(
#                                 id="ticker",
#                                 options=list(filter(lambda x: len(x) >= 14, df['Rekeningnummer'].unique())) + ['Totaal'],
#                                 value=list(filter(lambda x: len(x) >= 14, df['Rekeningnummer'].unique())) + ['Totaal'],
#                                 style={'font-family': 'Verdana'},
#                                 inline=True
#                             ),
#                             html.Br(),
#                             html.P("Selecteer aggregatie niveau", style={'font-family': 'Verdana'}),
#                             dcc.RadioItems(
#                                 id="ticker2",
#                                 options=[
#                                     {'label': 'Dag', 'value': 'D'},
#                                     {'label': 'Week', 'value': 'W'},
#                                     {'label': 'Maand', 'value': 'M'},
#                                     {'label': 'Jaar', 'value': 'Y'},
#                                 ],
#                                 value='M',
#                                 style={'font-family': 'Verdana'},
#                                 inline=True
#                             ),
#                         ]),
#                     dbc.Row(
#                         [
#                             html.Br(),
#                             dbc.Table.from_dataframe(df_extended[df_extended['Volgnummer'] != 'NaN'], striped=True, bordered=True, hover=True, size='sm', responsive=True)
#                         ]
#                     )
#                 ],
#                 width=9,
#                 style={'margin-left': '18rem'}
#             )
#         ],
#     ),
#     fluid=True,
#     style={'backgroundColor': 'secondary'}
#     # dbc.Row([
#     #     dbc.Col([
#     #         html.H1('Navigation', style={'textAlign': 'center'}),
#     #         dbc.Tabs([
#     #             dbc.Tab(tab1_content, label="Tab 1"),
#     #             dbc.Tab(tab2_content, label="Tab 2")
#     #         ]),
#     #     ], width=3),
#     #     dbc.Col([
#     #         html.H1('Personal Finance', style={'textAlign': 'center'})
#     #     ], width=9),
#     # ]), style={'backgroundColor': 'secondary'},
#     #
#     # # dbc.Col([
#     # #     dcc.Tabs(id="tabs-example-graph", value='tab-1-example-graph',
#     # #              children=[
#     # #                  dcc.Tab(label='Tabel', value='tab-1-example-graph'),
#     # #                  dcc.Tab(label='Grafiek', value='tab-2-example-graph'),
#     # #              ]),
#     # #     html.Div(id='tabs-content-example-graph')])
#     # fluid=True
# )
#
#
# # @app.callback(Output('time-series-chart', 'figure'),
# #               Input('tabs-example-graph', 'value'))
# # def render_content(tab):  # https://www.youtube.com/watch?v=S8ZcErBpfYE
# #     if True:  # tab == 'tab-1-example-graph':
# #         return html.Div([
# #             html.H3('Tab content 1'),
# #             html.Div(
# #                 id='table',
# #                 style={'width': '60vw', 'margin': 'auto', 'background-color': 'yellow', 'height': '50vh'},
# #                 children=[
# #                     dash_table.DataTable(
# #                         id='mydatatable',
# #                         data=df_extended[df_extended['Volgnummer'] != 'NaN'].to_dict('records'),
# #                         columns=[{"name": column, "id": column, 'format': Format().group(True)} for column in ['Uitvoeringsdatum', 'Rekeningnummer', 'Volgnummer', 'Bedrag', 'Categorie']],
# #                         style_data={
# #                             'whiteSpace': 'normal',
# #
# #                         },
# #                         style_cell={
# #                             'minWidth': '5%',
# #                             'width': '5%',
# #                             'maxWidth': '5%'
# #                         },
# #                         style_table={'overflowX': 'auto', 'overflowY': 'auto', 'height': '40vh', 'margin': 'auto'},
# #                         # fill_width=True,
# #                         # page_size=20,
# #                         filter_action="native")
# #                 ]),
# #         ])
# #     elif tab == 'tab-2-example-graph':
# #         return html.Div([
# #             html.H3('Tab content 2'),
# #             dcc.Graph(
# #                 id='graph-2-tabs-dcc',
# #                 figure={
# #                     'data': [{
# #                         'x': [1, 2, 3],
# #                         'y': [5, 10, 6],
# #                         'type': 'bar'
# #                     }]
# #                 }
# #             )
# #         ])
#
# @app.callback(
#     Output("time-series-chart", "figure"),
#     Input("ticker", 'value'),
#     Input("ticker2", 'value')
# )
# def display_time_series(input_rekeningnummer, input_frequentie):
#     if input_rekeningnummer != 0:
#         # Calculate total
#         dr_total = df.groupby([pd.Grouper(key='Uitvoeringsdatum', freq=input_frequentie)]).sum().cumsum().reset_index()
#         # print(dr_total.dtypes)
#
#         dr = df.groupby([pd.Grouper(key='Uitvoeringsdatum', freq=input_frequentie), 'Rekeningnummer']).sum().groupby(level=1).cumsum().reset_index()
#         for rekeningnummers in df['Rekeningnummer'].unique():
#             # print(rekeningnummers)
#             dr = pd.concat([dr, dr.query('Rekeningnummer in @rekeningnummers').iloc[-1:]], ignore_index=True)
#             dr.loc[-1, 'Uitvoeringsdatum'] = date.today()
#             # dr['Bedrag'].iloc[-1] = 0
#
#         dr_sum = pd.concat([dr, dr_total]).fillna("Totaal")
#         dg = dr_sum.query('Rekeningnummer in @input_rekeningnummer')
#         # dr2= []
#         # for aantal_rekeningnummers in input_rekeningnummer:
#
#         fig = px.line(dg, x='Uitvoeringsdatum', y='Bedrag', color='Rekeningnummer',
#                       # hover_name='Uitvoeringsdatum',
#                       # hovertemplate='Bedrag: %{y:$.2f}',
#                       hover_data={'Uitvoeringsdatum': "|%d %B %Y", 'Bedrag': ":.2f"},
#                       line_shape="hv",
#                       # hover_data={dr['Uitvoeringsdatum'][dr['Rekeningnummer'] == ticker]: "|%d %B %Y", dr['Bedrag'][dr['Rekeningnummer'] == ticker]: "|%.2f"},
#                       )
#         fig.update_layout(hovermode="x unified",
#                           # transition_easing='bounce-in',
#                           # transition_duration=5000
#                           )
#         fig.update_traces(mode="lines")
#
#         fig.update_layout(paper_bgcolor="primary")
#
#         fig.update_layout(legend=dict(
#             orientation="h",
#             yanchor="bottom",
#             y=1.01,
#             xanchor="center",
#             x=0.50
#         ))
#
#     return fig
