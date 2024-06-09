import flet as ft

def dataAlumno_view(page: ft.Page, id_usuario):
    numControl = "21350301"
    extension = "(TX) TUX"
    coordinador = " Lic. Alberto Bravo Nava"
    nombre = "Victor Axel Rodriguez Ocampo"
    modalidad = "Presencial"
    carrera = "ISC"

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

    datos = ft.Container(
        ft.Column([
                ft.Row([
                        ft.Container(
                            content=ft.Text(
                                "Datos Personales",
                                color="white",
                                text_align="center",
                                size=20,
                            ),
                            bgcolor="#0D257C",
                            width=page.width * 0.18,
                            height=page.height * 0.07,
                            alignment=ft.alignment.center,
                            border_radius=30,
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,),
                ft.Row(
                    [
                        ft.DataTable(
                            columns=[
                                ft.DataColumn(ft.Text("")),
                                ft.DataColumn(ft.Text("")),
                            ],
                            rows=[
                                ft.DataRow(
                                    cells=[
                                        ft.DataCell(ft.Text("No. Control: ")),
                                        ft.DataCell(ft.Text(numControl)),
                                    ]
                                ),
                                ft.DataRow(
                                    cells=[
                                        ft.DataCell(ft.Text("Extencion: ")),
                                        ft.DataCell(ft.Text(extension)),
                                    ]
                                ),
                                ft.DataRow(
                                    cells=[
                                        ft.DataCell(ft.Text("Coordinador: ")),
                                        ft.DataCell(ft.Text(coordinador)),
                                    ]
                                ),
                                ft.DataRow(
                                    cells=[
                                        ft.DataCell(ft.Text("Nombre: ")),
                                        ft.DataCell(ft.Text(nombre)),
                                    ]
                                ),
                                ft.DataRow(
                                    cells=[
                                        ft.DataCell(ft.Text("Modalidad: ")),
                                        ft.DataCell(ft.Text(modalidad)),
                                    ]
                                ),
                                ft.DataRow(
                                    cells=[
                                        ft.DataCell(ft.Text("Carrera: ")),
                                        ft.DataCell(ft.Text(carrera)),
                                    ]
                                ),
                            ],
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

    tablas = ft.Container(
        ft.Column(
            [
                ft.Row(
                    [
                        ft.Container(
                            content=ft.Text(
                                "Calificaciones",
                                color="white",
                                text_align="center",
                                size=20,
                            ),
                            bgcolor="#0D257C",
                            width=250,
                            height=50,
                            alignment=ft.alignment.center,
                            border_radius=30,
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
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
                                                    ft.DataCell(ft.Text("")),
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
                            ft.Row([
                                ft.Text("Calificacion Final: ")
                            ], alignment= ft.MainAxisAlignment.CENTER),
                        ]
                    )
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )
    
    calificaciones = ft.Container(
        content=tablas,
        expand= True,
        alignment= ft.alignment.center
    )
    def opciones(e):
        global session
        datos.visible = e.control.selected_index == 0
        calificaciones.visible = e.control.selected_index == 1
        if e.control.selected_index == 2:
            session = False
            page.go("/")  # Redirigir al inicio de sesión
        page.update()

    navigation_rail = ft.NavigationRail(
        selected_index=0,
        destinations=[
            ft.NavigationRailDestination(icon=ft.icons.PERSON, label="Datos Personales"),
            ft.NavigationRailDestination(icon=ft.icons.FORMAT_LIST_NUMBERED, label="Calificaciones"),
            ft.NavigationRailDestination(icon=ft.icons.EXIT_TO_APP, label="Salir"),
        ],
        on_change=opciones,
        visible=False
    )

    calificaciones.visible = False

    layout = ft.Row(
        [
            navigation_rail,
            ft.VerticalDivider(width=1),
            ft.Container(
                ft.Stack([datos, calificaciones]),
                expand=True
            )
        ],
        expand=True
    )
    navigation_rail.visible = True
    return ft.View("/estudiante", [barra,layout])
    