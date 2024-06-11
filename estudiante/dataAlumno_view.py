import flet as ft
def dataAlumno_view(page: ft.Page, id_usuario):
    datos_alumnos = {
    '21350265': {'apellido_paterno': 'Jorgue', 'apellido_materno': 'Cruz', 'nombres': 'Susana Lizeth', 'carrera': 'ISC', 'genero': 'F'},
    '21350273': {'apellido_paterno': 'Martinez', 'apellido_materno': 'Ignacio', 'nombres': 'Guadalupe', 'carrera': 'ISC', 'genero': 'F'},
    '21350281': {'apellido_paterno': 'Palacios', 'apellido_materno': 'Cabrera', 'nombres': 'Lady Sthefany', 'carrera': 'ISC', 'genero': 'F'},
    '21350301': {'apellido_paterno': 'Rodriguez', 'apellido_materno': 'Ocampo', 'nombres': 'Victor Axel', 'carrera': 'ISC', 'genero': 'M'},
    '21350499': {'apellido_paterno': 'Cabrera', 'apellido_materno': 'Vidal', 'nombres': 'Angel David', 'carrera': 'ISC', 'genero': 'M'}
}
    
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
    
    alumno = datos_alumnos[id_usuario]
    cali = calificaciones_alumnos.get(id_usuario)
    # Extraer las calificaciones finales
    calificaciones_finales = [unidad['calificacion_final'] for unidad in cali.values()]

    # Calcular el promedio de las calificaciones finales
    promedio_calificaciones_finales = sum(calificaciones_finales) / len(calificaciones_finales)
    numControl = id_usuario
    extension = "(TX) TUX"
    coordinador = " Lic. Alberto Bravo Nava"
    nombre = f"{alumno['nombres']} {alumno['apellido_paterno']} {alumno['apellido_materno']}"
    modalidad = "Presencial"
    carrera = f"{alumno['carrera']}"

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
                                                    ft.DataCell(ft.Text(cali[f"{i}"]['unidad1'])),
                                                    ft.DataCell(ft.Text(cali[f"{i}"]['unidad2'])),
                                                    ft.DataCell(ft.Text(cali[f"{i}"]['calificacion_final'])),
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
                                                    ft.DataCell(ft.Text(cali[f"{i}"]['unidad1'])),
                                                    ft.DataCell(ft.Text(cali[f"{i}"]['unidad2'])),
                                                    ft.DataCell(ft.Text(cali[f"{i}"]['calificacion_final'])),
                                                ]
                                            )
                                            for i in range(6, 11)
                                        ],
                                        column_spacing=20,
                                    ), col={"xs": 10, "sm": 10, "md": 6, "lg": 4}
                                )
                            ],alignment=ft.MainAxisAlignment.CENTER,),
                            ft.Row([
                                ft.Text("Calificacion Final: " + str(promedio_calificaciones_finales))
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

    