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



def estudiante_view(page: ft.Page):
        global session
        id = ft.TextField(hint_text='Usuario Estudiante', bgcolor='white', border_radius=10, width=380, height=50, adaptive=True)
        pin = ft.TextField(hint_text='Clave de acceso', bgcolor='white', border_radius=10, width=380, height=50,password = True, adaptive=True)
        barra = ft.Container(ft.ResponsiveRow([
            ft.Text('Sistema Integrador de calificaciones de lenguas extranjeras (SICLE)',
                font_family='Open-Sans',
                weight=ft.FontWeight.BOLD,
                size={"xs": 20, "sm": 25, "md": 30, "lg": 35},  # Ajuste responsivo del tamaño del texto
                color='white', text_align='center'
            )], alignment=ft.MainAxisAlignment.CENTER, spacing=1,  # Espacio entre elementos en la fila
        run_spacing={"xs": 5, "sm": 10, "md": 15, "lg": 20} ), bgcolor='#0D257C', padding=10, height=60,)

        container = ft.Container(
            ft.Column([
                ft.Container(
                    ft.Row([
                        ft.Text(
                            'Inicio de Sesion', 
                            color='#0D257C', 
                            weight=ft.FontWeight.BOLD, 
                            size=20,
                            font_family='OpenSans',
                            text_align='center'
                        )
                    ], alignment=ft.MainAxisAlignment.CENTER), bgcolor='white', width=450,  height=50, border_radius=60, padding=10
                ),
                ft.Row([
                    ft.Image('https://i.postimg.cc/rszvbGS4/4.png', border_radius=100)
                ], alignment=ft.MainAxisAlignment.CENTER, height=100),
                ft.Divider(height=30, color='transparent'),
                ft.Column([
                    id, pin,
                ]),
                ft.Row([
                    ft.FilledButton('Aceptar',on_click = lambda e: loginAlumno(id.value, pin.value), style=ft.ButtonStyle(bgcolor='#3F844B'))
                ], alignment=ft.MainAxisAlignment.CENTER),
            ]),
            padding=20,
            width=page.width*0.9 if page.width < 600 else page.width*0.3,
            height=page.width*0.9 if page.width < 600 else page.width*0.3,
            bgcolor='#0D257C',
            border_radius=40,
            margin=ft.margin.only(top=80, left=page.width*0.05 if page.width < 600 else page.width*0.35)
        )

        def menu(e):
                page.drawer.open = True
                page.drawer.update()

        def opciones(e):
            global session
            print("opcionesd")  # Podrías quitar este print si no es necesario
            datos.visible = e.control.selected_index == 0
            calificaciones.visible = e.control.selected_index == 1
            if e.control.selected_index == 2:
                session = False
                page.remove(page.drawer)
                page.drawer = None
                page.go("/")  # Redirigir al inicio de sesión
            page.update()

        page.drawer = ft.NavigationDrawer(
            controls=[
                ft.Divider(thickness=2),
                ft.NavigationDrawerDestination(
                    icon_content=ft.Icon(ft.icons.PERSON), label="Datos Personales"
                ),
                ft.NavigationDrawerDestination(
                    icon_content=ft.Icon(ft.icons.FORMAT_LIST_NUMBERED),
                    label="Calificaciones",
                ),
                ft.Divider(thickness=2),
                ft.NavigationDrawerDestination(
                    icon_content=ft.Icon(ft.icons.HIGHLIGHT_OFF), label="Salir"
                ),],
                on_change=opciones,
            )

        page.add(page.drawer)

        bar = ft.Container(
                ft.Column(
                    [
                        ft.Container(
                            content=ft.IconButton(
                                ft.icons.MENU, padding=20, on_click=menu
                            ),
                            margin=ft.margin.only(left=-10),
                        )
                    ]
                )
            )
        
        datos = ft.Container(
                ft.Column(
                    [
                        ft.Row(
                            [
                                ft.Container(
                                    content=ft.Text(
                                        "Datos Personales",
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
                                                ft.DataCell(ft.Text("control")),
                                            ]
                                        ),
                                        ft.DataRow(
                                            cells=[
                                                ft.DataCell(ft.Text("Extencion: ")),
                                                ft.DataCell(ft.Text("(TX) TUX")),
                                            ]
                                        ),
                                        ft.DataRow(
                                            cells=[
                                                ft.DataCell(ft.Text("Coordinador: ")),
                                                ft.DataCell(ft.Text("")),
                                            ]
                                        ),
                                        ft.DataRow(
                                            cells=[
                                                ft.DataCell(ft.Text("Nombre: ")),
                                                ft.DataCell(ft.Text("nombreCompleto")),
                                            ]
                                        ),
                                        ft.DataRow(
                                            cells=[
                                                ft.DataCell(ft.Text("Modalidad: ")),
                                                ft.DataCell(ft.Text("Presencial")),
                                            ]
                                        ),
                                        ft.DataRow(
                                            cells=[
                                                ft.DataCell(ft.Text("Carrera: ")),
                                                ft.DataCell(ft.Text("carrera")),
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
        
        calificaciones = ft.Container(
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
                        ft.Row(
                            [
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
                                    ],
                                    column_spacing=20,
                                ),
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
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                        ft.Row(
                            [ft.Text("Calificacion Final: ")],
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                    ]
                )
            )
        

        def loginAlumno(username, password):
            conexiondb = create_connection(host_name, user_name, user_password, db_name)
            cursor = conexiondb.cursor()

            # Verificar si el ID d usuario existe
            cursor.execute('''
            SELECT id_alumno FROM login WHERE id_alumno = %s
            ''', (username,)) 
            
            user = cursor.fetchone()
            
            if not user:
                page.snack_bar = ft.SnackBar(ft.Text("ID de alumno no existe"), open=True)
                page.update()
            else:
                # Si el ID existe, verificar el PIN
                cursor.execute('''
                SELECT * FROM login WHERE id_alumno = %s AND pin = %s
                ''', (username, password))
                
                user = cursor.fetchone()
                
                if user:
                    session = True
                    datos.visible = True
                    calificaciones.visible = False
                    bar.visible = True
                    container.visible = False
                    page.update()
                    print("Inicio de sesión exitoso")
                else:
                    page.snack_bar = ft.SnackBar(ft.Text("PIN incorrecto"), open=True)
                    page.update()
            
            conexiondb.close()
        return ft.View("/estudiante", [barra, bar, page.drawer, container, datos, calificaciones])
    