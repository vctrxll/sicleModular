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

def docente_view(page: ft.Page):
    id_docente = ft.TextField(
        hint_text='Usuario Docente',
        bgcolor='white',
        border_radius=10,
        width=380,
        height=50,
        adaptive=True
    )
    pin_docente = ft.TextField(
        hint_text='Clave de acceso',
        bgcolor='white',
        border_radius=10,
        width=380,
        height=50,
        password=True,
        adaptive=True
    )

    barra = ft.Container(
        ft.ResponsiveRow([
            ft.Text(
                'Sistema Integrador de calificaciones de lenguas extranjeras (SICLE)',
                font_family='Open-Sans',
                weight=ft.FontWeight.BOLD,
                size={"xs": 20, "sm": 25, "md": 30, "lg": 35},
                color='white',
                text_align='center'
            )], 
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=1,
            run_spacing={"xs": 5, "sm": 10, "md": 15, "lg": 20}
        ),
        bgcolor='#0D257C',
        padding=10,
        height=60
    )

    def loginDocente(e):
        conexiondb = create_connection(host_name, user_name, user_password, db_name)
        cursor = conexiondb.cursor()

        try:
            # Verificar si el ID del profesor existe
            cursor.execute('''
            SELECT id FROM profesores WHERE id = %s
            ''', (id_docente.value,)) 
            
            user = cursor.fetchone()
            
            if not user:
                print("ID de profesor no existe")
                page.snack_bar = ft.SnackBar(ft.Text("ID de profesor no existe"), open=True)
                page.update()
            else:
                # Si el ID existe, verificar el PIN
                cursor.execute('''
                SELECT * FROM profesores WHERE id = %s AND pin = %s
                ''', (id_docente.value, pin_docente.value))
                
                user = cursor.fetchone()
                
                if user:
                    print("Inicio de sesión exitoso")
                else:
                    print("PIN incorrecto")
                    page.snack_bar = ft.SnackBar(ft.Text("PIN incorrecto"), open=True)
                    page.update()
        except Error as e:
            print(f"El error '{e}' ocurrió")
        finally:
            cursor.close()
            conexiondb.close()

    login_container = ft.Container(
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
                ], alignment=ft.MainAxisAlignment.CENTER),
                bgcolor='white', 
                width=450, 
                height=50, 
                border_radius=60, 
                padding=10
            ),
            ft.Row([
                ft.Image('https://i.postimg.cc/rszvbGS4/4.png', border_radius=100)
            ], alignment=ft.MainAxisAlignment.CENTER, height=100),
            ft.Divider(height=30, color='transparent'),
            ft.Column([
                id_docente, 
                pin_docente
            ]),
            ft.Row([
                ft.FilledButton('Aceptar', on_click=loginDocente, style=ft.ButtonStyle(bgcolor='#3F844B'))
            ], alignment=ft.MainAxisAlignment.CENTER),
        ]),
        padding=20,
        width=page.width*0.9 if page.width < 600 else page.width*0.3,
        height=page.width*0.9 if page.width < 600 else page.width*0.3,
        bgcolor='#0D257C',
        border_radius=40,
        margin=ft.margin.only(top=80, left=page.width*0.05 if page.width < 600 else page.width*0.35)
    )

    return ft.View("/docente", [barra, login_container])
