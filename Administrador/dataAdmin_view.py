
import flet as ft

def dataAdmin_view(page: ft.Page, id):
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
            grupos.visible = True
            calificaciones.visible = False
            page.update()

        elif(e.control.selected_index == 1):
            calificaciones.visible = True
            grupos.visible = False
            page.update()
        elif(e.control.selected_index == 2):
            page.go("/")

    navigation_rail = ft.NavigationRail(
        selected_index=0,
        destinations=[
            ft.NavigationDrawerDestination(
                icon_content=ft.Icon(ft.icons.SCHEDULE),
                label="Grupos"
            ),
            ft.NavigationDrawerDestination(
                icon_content=ft.Icon(ft.icons.FORMAT_LIST_NUMBERED),
                label="Auditorias"
            ),
            ft.NavigationDrawerDestination(
                icon_content=ft.Icon(ft.icons.HIGHLIGHT_OFF),
                label="Salir"
            ),
        ],
        on_change=opciones,
        visible=False
    )


    grupos = ft.Container(
        ft.Row([
            ft.Container(content=ft.Text('Grupos',color='white',text_align='center',size=20),bgcolor='#0D257C',
                         width=250,height=50,alignment=ft.alignment.center,border_radius=30)
        ],alignment=ft.MainAxisAlignment.CENTER),
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
                ft.Stack([grupos,calificaciones]),
                expand=True
            )
        ],
        expand=True
    )

    calificaciones.visible = False
    navigation_rail.visible = True
    return ft.View("/admin", [barra,layout])