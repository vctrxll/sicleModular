import flet as ft

def dataDocente_view(page: ft.Page,id):
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
    options_numeros = [
    ft.dropdown.Option("1"), ft.dropdown.Option("2"), ft.dropdown.Option("3"), ft.dropdown.Option("4"),
    ft.dropdown.Option("5"), ft.dropdown.Option("6"), ft.dropdown.Option("7"), ft.dropdown.Option("8"),
    ft.dropdown.Option("9"), ft.dropdown.Option("10")
]


    numeros = list(range(1, 11))


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
                    ]
                )
                 ],alignment=ft.MainAxisAlignment.CENTER)
            ])

    )

    calificaciones = ft.Container(
        ft.Row([
            ft.Container(content=ft.Text('Calificaciones',color='white',text_align='center',size=20),bgcolor='#0D257C',
                         width=250,height=50,alignment=ft.alignment.center,border_radius=30)
        ],alignment=ft.MainAxisAlignment.CENTER),
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
