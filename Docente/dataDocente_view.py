import flet as ft

def dataDocente_view(page: ft.Page,id):
    id_usuario= ft.TextField(hint_text='Numero de control', bgcolor='white', border_radius=20)
    options_letras = [
    ft.dropdown.Option("A"), ft.dropdown.Option("B"), ft.dropdown.Option("C"), ft.dropdown.Option("D"),
    ft.dropdown.Option("E"), ft.dropdown.Option("F"), ft.dropdown.Option("G"), ft.dropdown.Option("H"),
    ft.dropdown.Option("I"), ft.dropdown.Option("J"), ft.dropdown.Option("K"), ft.dropdown.Option("L"),
    ft.dropdown.Option("M"), ft.dropdown.Option("N"), ft.dropdown.Option("O"), ft.dropdown.Option("P"),
    ft.dropdown.Option("Q"), ft.dropdown.Option("R"), ft.dropdown.Option("S"), ft.dropdown.Option("T"),
    ft.dropdown.Option("U"), ft.dropdown.Option("V"), ft.dropdown.Option("W"), ft.dropdown.Option("X"),
    ft.dropdown.Option("Y"), ft.dropdown.Option("Z")]

    options_numeros = [
    ft.dropdown.Option("1"), ft.dropdown.Option("2"), ft.dropdown.Option("3"), ft.dropdown.Option("4"),
    ft.dropdown.Option("5"), ft.dropdown.Option("6"), ft.dropdown.Option("7"), ft.dropdown.Option("8"),
    ft.dropdown.Option("9"), ft.dropdown.Option("10")
]

    barra = ft.Container(
        ft.ResponsiveRow(
            [
                ft.Text(
                    "Sistema Integrador de calificaciones de lenguas extranjeras (SICLE)",
                    font_family="Open-Sans",
                    weight=ft.FontWeight.BOLD,
                    size={"xs": 25, "sm": 30, "md": 35, "lg": 40},
                    color="white",
                    text_align="center",
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=1,
            run_spacing={"xs": 5, "sm": 10, "md": 15, "lg": 20},
        ),
        bgcolor="#0D257C",
        padding=10,
        height=60,
    )

    def opciones(e):
        if(e.control.selected_index == 0):
            horario.visible = False
            grupos.visible = True
            calificaciones.visible = False
            page.update()

        elif(e.control.selected_index == 1):
            horario.visible = True
            grupos.visible = False
            calificaciones.visible = False
            page.update()

        elif(e.control.selected_index == 2):
            calificaciones.visible = True
            grupos.visible = False
            horario.visible = False
            page.update()
        elif(e.control.selected_index == 3):
            page.go("/")

    navigation_rail = ft.NavigationRail(
        selected_index=0,
        destinations=[
            ft.NavigationDrawerDestination(
                icon_content=ft.Icon(ft.icons.PERSON),
                label="Grupos"
            ),
            ft.NavigationDrawerDestination(
                icon_content=ft.Icon(ft.icons.SCHEDULE),
                label="Horario"
            ),
            ft.NavigationDrawerDestination(
                icon_content=ft.Icon(ft.icons.FORMAT_LIST_NUMBERED),
                label="Calificaciones"
            ),
            ft.NavigationDrawerDestination(
                icon_content=ft.Icon(ft.icons.HIGHLIGHT_OFF),
                label="Salir"
            ),
        ],
        on_change=opciones,
        visible=True
    )

    calificaciones_alumnos = {
    '21350265': {
    '1': {'unidad1': 9.00, 'unidad2': 9.20, 'calificacion_final': 9.10},
    '2': {'unidad1': 9.40, 'unidad2': 8.90, 'calificacion_final': 9.15},
    '3': {'unidad1': 9.00, 'unidad2': 9.10, 'calificacion_final': 9.05},
    '4': {'unidad1': 9.20, 'unidad2': 9.00, 'calificacion_final': 9.10},
    '5': {'unidad1': 9.10, 'unidad2': 9.30, 'calificacion_final': 9.20},
    '6': {'unidad1': 9.10, 'unidad2': 9.40, 'calificacion_final': 9.25},
    '7': {'unidad1': 9.30, 'unidad2': 9.20, 'calificacion_final': 9.25},
    '8': {'unidad1': 9.20, 'unidad2': 9.50, 'calificacion_final': 9.35},
    '9': {'unidad1': 9.40, 'unidad2': 9.30, 'calificacion_final': 9.35},
    '10': {'unidad1': 9.50, 'unidad2': 9.10, 'calificacion_final': 9.30},
},
    '21350273': {
        '1': {'unidad1': 9.30, 'unidad2': 8.60, 'calificacion_final': 8.95},
        '2': {'unidad1': 9.20, 'unidad2': 8.90, 'calificacion_final': 9.05},
        '3': {'unidad1': 8.90, 'unidad2': 9.10, 'calificacion_final': 9.00},
        '4': {'unidad1': 9.10, 'unidad2': 8.80, 'calificacion_final': 8.95},
        '5': {'unidad1': 8.80, 'unidad2': 9.50, 'calificacion_final': 9.15},
        '6': {'unidad1': 8.60, 'unidad2': 9.40, 'calificacion_final': 8.95},
        '7': {'unidad1': 9.40, 'unidad2': 8.70, 'calificacion_final': 9.05},
        '8': {'unidad1': 8.70, 'unidad2': 9.30, 'calificacion_final': 9.00},
        '9': {'unidad1': 9.00, 'unidad2': 8.50, 'calificacion_final': 8.75},
        '10': {'unidad1': 9.20, 'unidad2': 8.90, 'calificacion_final': 9.05}
    },
    '21350281': {
        '1': {'unidad1': 9.20, 'unidad2': 8.70, 'calificacion_final': 8.95},
        '2': {'unidad1': 9.50, 'unidad2': 8.80, 'calificacion_final': 9.15},
        '3': {'unidad1': 8.60, 'unidad2': 9.10, 'calificacion_final': 8.85},
        '4': {'unidad1': 9.30, 'unidad2': 8.90, 'calificacion_final': 9.10},
        '5': {'unidad1': 8.90, 'unidad2': 9.30, 'calificacion_final': 9.10},
        '6': {'unidad1': 8.20, 'unidad2': 9.50, 'calificacion_final': 8.85},
        '7': {'unidad1': 9.10, 'unidad2': 8.60, 'calificacion_final': 8.85},
        '8': {'unidad1': 8.80, 'unidad2': 9.20, 'calificacion_final': 9.00},
        '9': {'unidad1': 9.60, 'unidad2': 8.70, 'calificacion_final': 9.15},
        '10': {'unidad1': 8.90, 'unidad2': 9.40, 'calificacion_final': 9.15}
    },
    '21350301': {
        '1': {'unidad1': 8.80, 'unidad2': 9.00, 'calificacion_final': 8.90},
        '2': {'unidad1': 8.90, 'unidad2': 9.30, 'calificacion_final': 9.10},
        '3': {'unidad1': 9.20, 'unidad2': 8.90, 'calificacion_final': 9.05},
        '4': {'unidad1': 8.70, 'unidad2': 9.10, 'calificacion_final': 8.90},
        '5': {'unidad1': 9.30, 'unidad2': 8.70, 'calificacion_final': 9.00},
        '6': {'unidad1': 9.00, 'unidad2': 8.60, 'calificacion_final': 8.80},
        '7': {'unidad1': 8.60, 'unidad2': 9.40, 'calificacion_final': 9.00},
        '8': {'unidad1': 9.40, 'unidad2': 8.80, 'calificacion_final': 9.10},
        '9': {'unidad1': 7.00, 'unidad2': 7.00, 'calificacion_final': 7.00},
        '10': {'unidad1': 8.80, 'unidad2': 9.20, 'calificacion_final': 9.00},
    },
    '21350499': {
        '1': {'unidad1': 9.10, 'unidad2': 8.80, 'calificacion_final': 8.95},
        '2': {'unidad1': 9.30, 'unidad2': 8.90, 'calificacion_final': 9.10},
        '3': {'unidad1': 8.70, 'unidad2': 9.30, 'calificacion_final': 9.00},
        '4': {'unidad1': 9.50, 'unidad2': 8.60, 'calificacion_final': 9.05},
        '5': {'unidad1': 8.40, 'unidad2': 9.20, 'calificacion_final': 8.80},
        '6': {'unidad1': 8.90, 'unidad2': 9.10, 'calificacion_final': 9.00},
        '7': {'unidad1': 9.20, 'unidad2': 8.70, 'calificacion_final': 8.95},
        '8': {'unidad1': 8.80, 'unidad2': 9.40, 'calificacion_final': 9.10},
        '9': {'unidad1': 9.30, 'unidad2': 8.90, 'calificacion_final': 9.10},
        '10': {'unidad1': 8.50, 'unidad2': 9.20, 'calificacion_final': 8.85}
    }
}
    grupos = ft.Container(
        ft.Column([
            ft.Row([
                    ft.Container(content=ft.Text('Grupos',color='white',text_align='center',size=20),bgcolor='#0D257C',
                         width=250,height=50,alignment=ft.alignment.center,border_radius=30),
            ],alignment=ft.MainAxisAlignment.CENTER),
                         ft.Row([
                             ft.Column([
                                 ft.Text('Seleccionar Modulo'),ft.Dropdown(options= options_letras,label='Modulo'),
                                        ft.FilledButton('Aceptar',style=ft.ButtonStyle(bgcolor='#0D257C'))
                             ]),
                             ft.Column([
                                 ft.Text('Seleccionar Grupo'),ft.Dropdown(options= options_numeros,label='Grupo'),
                                 ft.FilledButton('Aceptar',style=ft.ButtonStyle(bgcolor='#0D257C'), disabled = True)

                             ])
                         ],alignment=ft.MainAxisAlignment.CENTER,spacing=40),
                ft.Row([
                    ft.Column([
                        ft.FilledButton('Continuar',style=ft.ButtonStyle(bgcolor='#0D257C'), disabled = True)
                            ])
                        ],alignment=ft.MainAxisAlignment.CENTER)
        ],alignment=ft.MainAxisAlignment.CENTER),

    )

    horario = ft.Container(
        ft.Column([
            ft.Row([
                ft.Container(content=ft.Text('Horario',color='white',text_align='center',size=20),bgcolor='#0D257C',
                            width=250,height=50,alignment=ft.alignment.center,border_radius=30)
                 ],alignment=ft.MainAxisAlignment.CENTER),
                 ft.Row([
                     ft.DataTable(
                    columns=[
                        ft.DataColumn(ft.Text("Grupo")),
                        ft.DataColumn(ft.Text("Dias")),
                        ft.DataColumn(ft.Text("Hora")),
                        ft.DataColumn(ft.Text("Codigo")),
                    ],
                    rows=[
                        ft.DataRow(
                            cells=[
                                ft.DataCell(ft.Text('----')),
                                ft.DataCell(ft.Text('----')),
                                ft.DataCell(ft.Text('----')),
                                ft.DataCell(ft.Text('----')),
                            ]
                        )
                        for i in range(1, 5)
                    ]
                )
                 ],alignment=ft.MainAxisAlignment.CENTER)
            ])

    )

    tabla = ft.Container(
        ft.Column([
                    ft.Container(
                    expand=True,
                    content= ft.Column(
                        scroll="auto",
                        controls=[

                            ft.ResponsiveRow([
                                ft.Container(
                                    ft.DataTable(
                                        columns=[
                                            ft.DataColumn(ft.Text("Modulo")),
                                            ft.DataColumn(ft.Text("   ")),
                                            ft.DataColumn(ft.Text("Parcial 1")),
                                            ft.DataColumn(ft.Text("Parcial 2")),
                                            ft.DataColumn(ft.Text("Final")),
                                        ],
                                        rows=[
                                            ft.DataRow(
                                                cells=[
                                                    ft.DataCell(ft.Text(f"Modulo {i}")),
                                                    ft.DataCell(ft.Text("")),
                                                    ft.DataCell(ft.Text("")),
                                                    ft.DataCell(ft.Text("")),
                                                    ft.DataCell(ft.Text("")),
                                                ]
                                            )
                                            for i in range(1, 6)
                                        ], column_spacing=20,
                                    ), col={"xs": 10, "sm": 10, "md": 6, "lg": 4}
                                ),

                                ft.Container(
                                    ft.DataTable(
                                        columns=[
                                            ft.DataColumn(ft.Text("Modulo")),
                                            ft.DataColumn(ft.Text("   ")),
                                            ft.DataColumn(ft.Text("Parcial 1")),
                                            ft.DataColumn(ft.Text("Parcial 2")),
                                            ft.DataColumn(ft.Text("Final")),
                                        ],
                                        rows=[
                                            ft.DataRow(
                                                cells=[
                                                    ft.DataCell(ft.Text(f"Modulo {i}")),
                                                    ft.DataCell(ft.Text('')),
                                                    ft.DataCell(ft.Text("")),
                                                    ft.DataCell(ft.Text("")),
                                                    ft.DataCell(ft.Text("")),
                                                ]
                                            )
                                            for i in range(6, 11)
                                        ],
                                        column_spacing=20,
                                    ), col={"xs": 10, "sm": 10, "md": 6, "lg": 4}
                                )
                            ],alignment=ft.MainAxisAlignment.CENTER,),
                        ]
                    )
                )
        ])
    )


    calificaciones = ft.Container(
        ft.Column([
            ft.Row([
            ft.Container(content=ft.Text('Calificaciones',color='white',text_align='center',size=20),bgcolor='#0D257C',
                         width=250,height=50,alignment=ft.alignment.center,border_radius=30)
        ],alignment=ft.MainAxisAlignment.CENTER),

        ft.Divider(height=page.height *0.06, color='transparent'),

        ft.ResponsiveRow([
            ft.Container(
                ft.Column([
                    id_usuario
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                ),
                col={"xs": 12, "sm": 6, "md": 4, "lg": 3}
            ),
            #ft.Divider(height=page.height *0.002, color='transparent'),

            ft.Container(
                ft.Column([
                ft.FilledButton('Aceptar', style=ft.ButtonStyle(bgcolor='#3F844B'))
                ],
                
                horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                col={"xs": 12, "sm": 6, "md": 4, "lg": 3}
            )
        ], alignment= ft.MainAxisAlignment.CENTER),

        tabla
        ])
    )

    
    
    layout = ft.Row(
        [
            navigation_rail,
            ft.VerticalDivider(width=1),
            ft.Container(
                ft.Stack([grupos,horario,calificaciones]),
                expand=True
            )
        ],
        expand=True
    )

    calificaciones.visible = False
    horario.visible = False
    return ft.View("/docente", [barra,layout])
