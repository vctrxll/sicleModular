import flet as ft
from estudiante.dataAlumno_view import dataAlumno_view 

numeros_control_nip = [
    {'numero_control': "21350301", 'nip': "4955"},
    {'numero_control': "21350265", 'nip': "1909"},
    {'numero_control': "21350281", 'nip': "1718"},
    {'numero_control': "21350499", 'nip': "0302"},
    {'numero_control': "21350273", 'nip': "1212"}
]


def estudiante_view(page: ft.Page):
        id_usuario= ft.TextField(hint_text='Usuario Estudiante', bgcolor='white', border_radius=20)
        pin = ft.TextField(hint_text='Clave de acceso', bgcolor='white', border_radius=20, password = True, can_reveal_password = True)

        barra = ft.Container(ft.ResponsiveRow([
            ft.Text('Sistema Integrador de calificaciones de lenguas extranjeras (SICLE)',
                font_family='Open-Sans',
                weight=ft.FontWeight.BOLD,
                size= 16,# Ajuste responsivo del tamaño del texto
                color='white', text_align='center'
            )], alignment=ft.MainAxisAlignment.CENTER, spacing=1,  # Espacio entre elementos en la fila
        run_spacing={"xs": 5, "sm": 10, "md": 15, "lg": 20} ), bgcolor='#0D257C', padding=10, height=60,)
        
        formulario = ft.Container(
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
                    ], alignment=ft.MainAxisAlignment.CENTER),alignment=ft.alignment.center,bgcolor='white', width=page.width *0.4,  height=page.height * 0.05, border_radius=60, padding=page.width *0.002
                ),
                ft.Row([
                    ft.Image('https://i.postimg.cc/rszvbGS4/4.png', border_radius=100, height = page.height *0.12)
                ], alignment=ft.MainAxisAlignment.CENTER),
                ft.Divider(height=page.height *0.002, color='transparent'),
                ft.Column([
                    id_usuario, 
                    pin,
                ]),
                ft.Row([
                    ft.FilledButton('Aceptar',on_click = lambda e: loginAlumno(id_usuario.value, pin.value), style=ft.ButtonStyle(bgcolor='#3F844B'))
                ], alignment=ft.MainAxisAlignment.CENTER),
            ]),
            padding=page.width * 0.02,
            bgcolor='#0D257C',
            border_radius=40,
        )

        login_container = ft.ResponsiveRow(
        [
            ft.Container(
                content=formulario,
                col={"xs": 10, "sm": 8, "md": 3.5, "lg": 3.5},  # Ajusta según tus necesidades
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER,  # Centrado vertical y horizontal
    )

        def loginAlumno(id_alumno, password):
            usuario = next((u for u in numeros_control_nip if u['numero_control'] == id_alumno), None)
            if usuario:
                if usuario['nip'] == password:
                    print("Inicio de sesión exitoso para el alumno")
                    page.views.append(dataAlumno_view(page, id_alumno))
                    page.update()
                else:
                    page.snack_bar = ft.SnackBar(ft.Text("PIN incorrecto"), open=True)
                    page.update()
            else:
                    page.snack_bar = ft.SnackBar(ft.Text("ID no existe"), open=True)
                    page.update()

        return ft.View("/estudiante", [barra, login_container])

    
    