import flet as ft
import mysql.connector
from mysql.connector import Error

host_name = "localhost"
user_name = "root"
user_password = "" 
db_name = "siclev2"

def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            password=user_password,
            database=db_name
        )
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection

def dataDocente_view(page: ft.Page):

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
                                 ft.Text('Seleccionar Modulo'),ft.Dropdown(label='Modulo'),
                                        ft.FilledButton('Aceptar',style=ft.ButtonStyle(bgcolor='#0D257C'))
                             ]),
                             ft.Column([
                                 ft.Text('Seleccionar Grupo'),ft.Dropdown(label='Grupo'),
                                 ft.FilledButton('Aceptar',style=ft.ButtonStyle(bgcolor='#0D257C'))

                             ])
                         ],alignment=ft.MainAxisAlignment.CENTER,spacing=40),
                ft.Row([
                    ft.Column([
                        ft.FilledButton('Continuar',style=ft.ButtonStyle(bgcolor='#0D257C'))
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