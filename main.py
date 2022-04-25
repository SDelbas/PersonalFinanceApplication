import locale
from datetime import datetime, date

import df_manipulator
import file_manager
import dash
from dash import Dash, dcc, html, dash_table
import dash_bootstrap_components as dbc  # https://dash-bootstrap-components.opensource.faculty.ai/docs/themes/
from dash.dependencies import Input, Output
from dash.dash_table.Format import Format, Group, Scheme, Symbol
from dash import html
from configuration import Configuration

# ---------------------------------------------------------------------------------------------------
# Set Belgium locale


locale.setlocale(locale.LC_NUMERIC, 'nl_BE')
configuration = Configuration()
configuration.write()
exit()

# t1 = datetime.now()
df_raw = file_manager.importer()
df_raw_sIndex = df_raw.reset_index()
df_extended = df_manipulator.main(df_raw).reset_index()

# Change Uitvoeringsdatum en Valutadatum to only contain the date
df_raw_sIndex['Uitvoeringsdatum'] = df_raw_sIndex['Uitvoeringsdatum'].dt.date
df_raw_sIndex['Valutadatum'] = df_raw_sIndex['Valutadatum'].dt.date
# print(str((datetime.now() - t1).total_seconds()) + ' seconds have elapsed.')
# df = df_extended

# Start app instance and set external bootstrap theme
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SUPERHERO], suppress_callback_exceptions=True)

# References
# https://www.youtube.com/watch?v=1nEL0S8i2Wk
# https://dash-bootstrap-components.opensource.faculty.ai/docs/components/layout/
# https://getbootstrap.com/docs/5.0/utilities/sizing/
# https://bootswatch.com/ https://bootswatch.com/superhero/
# https://dashcheatsheet.pythonanywhere.com/
# https://community.plotly.com/t/highlighting-selected-rows/49595/4

# Determine sidebar element
sidebar = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H1('Personal Finance', className='fs-1 text fw-bold'),
                html.Hr(),
                html.P('Different pages of the program', className='text-muted'),
                dbc.Nav(
                    [
                        dbc.NavLink('Home', href='/', active='exact', style={'text-align': 'left'}),
                        dbc.NavLink('Graph', href='/graph', active='exact', style={'text-align': 'left'}),
                        dbc.NavLink('Transactions', href='/transactions', active='exact', style={'text-align': 'left'}),
                        dbc.NavLink('Settings', href='/settings', active='exact', style={'text-align': 'left'})
                    ],
                    vertical=True,
                    pills=True,
                    style={'margin': 'auto'}
                ),
                html.Hr(),
            ]
        )

    ],
    style={'height': '100vh', 'position': 'fixed', 'width': '17rem'},
    # className='ps-0'
)

# Determine main screen content
content = dbc.Container(id='main-screen-content', style={'padding': '2rem'}, fluid=True)

# App structure
app.layout = dbc.Container(
    [
        dcc.Location(id='url'),
        dbc.Row(
            [
                dbc.Col(
                    [
                        sidebar
                    ],
                    width=2,
                    className='bg-success ps-0'
                ),
                dbc.Col(
                    [
                        content
                    ],
                    width=10,
                    className='bg-dark'
                ),
            ],
            className='g-0'
        )
    ],
    fluid=True
)


@app.callback(
    Output("main-screen-content", "children"),
    Input('url', 'pathname')
)
def render_main_screen_content(pathname):
    if pathname == '/':
        return [
            html.H2('Overview', className='display-5 fw-bold'),
            html.Hr(),
            dbc.Row([]),
        ]
    elif pathname == '/graph':
        return [
            html.H1('Graph', className='display-5 fw-bold'),
            html.Hr()
        ]
    elif pathname == '/transactions':
        return [
            dbc.Row(
                [
                    html.H1('Transactions', className='display-5 fw-bold'),
                    html.Hr(),
                    dash_table.DataTable(
                        id='transactions-datatable',
                        columns=[
                            {'name': 'Uitvoeringsdatum', 'id': 'Uitvoeringsdatum', 'type': 'text', 'editable': False},
                            {'name': 'Rekeningnummer', 'id': 'Rekeningnummer', 'type': 'text', 'editable': False},
                            {'name': 'Volgnummer', 'id': 'Volgnummer', 'type': 'text', 'editable': False},
                            {'name': 'Bedrag', 'id': 'Bedrag', 'type': 'numeric', 'editable': False, 'format': Format(scheme=Scheme.fixed, precision=2, group=Group.yes, groups=3, group_delimiter='.', decimal_delimiter=',')},
                            {'name': 'Munteenheid', 'id': 'Munteenheid', 'type': 'text', 'editable': False},
                            {'name': 'Categorie', 'id': 'Categorie', 'type': 'numeric', 'editable': False},
                        ],
                        data=df_raw_sIndex.to_dict('records'),
                        style_data_conditional=(
                            [
                                # Format numeric type cells
                                {
                                    'if': {
                                        'column_type': 'numeric'
                                    },
                                    'textAlign': 'right',
                                    'paddingRight': '5%'
                                },

                                # Format selected cells
                                {
                                    'if': {
                                        'state': 'selected'
                                    },
                                    'backgroundColor': 'rgba(76, 155, 232, 1)',
                                    'border': '15px'
                                },
                                # Color uneven rows
                                {
                                    'if': {
                                        'row_index': 'odd'
                                    },
                                    'backgroundColor': 'rgba(255, 255, 255, 0.1)'
                                }
                            ]
                        ),
                        style_table={'overflowX': 'auto', 'overflowY': 'auto', 'height': '370px', 'margin': 'auto'},
                        style_cell={'backgroundColor': 'rgba(255, 255, 255, 0.05)', 'textAlign': 'center'},
                        style_header={'backgroundColor': 'rgba(255, 255, 255, 0.15)', 'textAlign': 'center', 'fontWeight': 'bold', 'border': '2px solid light grey'},
                        style_filter={'backgroundColor': 'rgba(255, 255, 255, 0.10)', 'textAlign': 'center'},
                        filter_action="native",
                        # row_selectable='single',
                        style_as_list_view=True,
                        page_action='none',
                        sort_action='native',
                        # page_size=10,
                        virtualization=True,
                    ),
                ],
                style={'paddingBottom': '2rem', 'height': '40vh', 'overflowY': 'auto'}
            ),
            dbc.Row(
                [
                    html.H1('Detail', className='display-5 fw-bold'),
                    html.Hr(),
                    dbc.Container(id='transactions-detail')
                ],
                style={'height': ''},
            )
        ]
    elif pathname == '/settings':
        return [
            html.H1('Settings', className='display-5 fw-bold'),
            html.Hr()
        ]
    # elif
    else:
        return [
            html.H1('404: Page not found.', className='display-4 fw-bold')
        ]


@app.callback(
    Output("transactions-detail", "children"),
    Input('transactions-datatable', 'active_cell'),
    # Input('transactions-datatable', 'page_current'),
    # Input('transactions-datatable', 'page_size'),
)
def render_main_screen_content(active_cell, ):
    detailed_view = []
    detailed_view_info = []

    if active_cell is not None:
        index = active_cell['row']

        # Create inputgroup for row 1 column 1
        input11 = [html.H5('Datum'), html.Hr()]
        input12 = [html.H5('Rekeningnummer'), html.Hr()]
        input13 = [html.H5('Waarde'), html.Hr()]
        input21 = []
        input22 = []
        input20 = [html.H5('Overige'), html.Hr(),
                   dbc.Col(input21, width=True),
                   # dbc.Col(input22, width=True)
                   ]

        for data_names, data_values in df_raw_sIndex.iloc[index].dropna().iteritems():
            if data_names in ['Uitvoeringsdatum', 'Valutadatum']:
                input11.append(
                    dbc.InputGroup(
                        [
                            dbc.InputGroupText(data_names, className='fw-bold w-50'), dbc.Input(placeholder=data_values, disabled=True, className='text-center')
                        ],
                        className='mb-3'
                    )
                )
            elif data_names in ['Rekeningnummer', 'ING-Rekening tegenpartij', 'BNP-Tegenpartij']:
                input12.append(
                    dbc.InputGroup(
                        [
                            dbc.InputGroupText(data_names.replace('ING-', '').replace('BNP-', ''), className='fw-bold w-25'), dbc.Input(placeholder=data_values, disabled=True, className='text-center')
                        ],
                        className='mb-3'
                    )
                )
            elif data_names in ['Bedrag', 'Munteenheid']:
                input13.append(
                    dbc.InputGroup(
                        [
                            dbc.InputGroupText(data_names, className='fw-bold w-50'), dbc.Input(placeholder=data_values, disabled=True, className='text-center')
                        ],
                        className='mb-3'
                    )
                )
            elif data_names not in ['Categorie']:
                if len(input21) < 4:
                    input21.append(
                        dbc.InputGroup(
                            [
                                dbc.InputGroupText(data_names, className='fw-bold w-25'), dbc.Input(placeholder=data_values, disabled=True, className='text-left')
                            ],
                            className='mb-3 d-flex flex-wrap'
                        )
                    )
                else:
                    input22.append(
                        dbc.InputGroup(
                            [
                                dbc.InputGroupText(data_names, className='fw-bold w-50'), dbc.Input(placeholder=data_values, disabled=True)
                            ],
                            className='mb-3'
                        )
                    )

        detailed_view = dbc.Container([
            dbc.Row(
                [
                    dbc.Col(
                        input11, width=3
                    ),
                    dbc.Col(
                        input12, width=6
                    ),
                    dbc.Col(
                        input13, width=3
                    ),
                ]
            ),
            html.Br(),
            dbc.Row(
                input20
            )
        ])
    return detailed_view


#     # if page_current is None:
#     #     page_current = 0
#     index = active_cell['row'] #+ page_current * page_size
#
#     for name, value in df_raw_sIndex.iloc[index].dropna().iteritems():
#         detailed_view_info.append(dbc.ListGroupItem(str(name) + ':' + '    ' + str(value)))
#         detailed_view_info.append(html.Hr(style={'margin': '3px'}))
#
#     detailed_view = dbc.Row(
#         [
#             dbc.Card(
#                 [
#                     dbc.ListGroup(
#                         detailed_view_info,
#                         flush=True
#                     )
#                 ]
#             )
#         ]
#     )


if __name__ == '__main__':
    app.run_server(debug=True)
