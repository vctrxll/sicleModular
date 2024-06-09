import flet as ft
from estudiante.dataAlumno_view import dataAlumno_view 


def estudiante_view(page: ft.Page):
        id_usuario= ft.TextField(hint_text='Usuario Estudiante', bgcolor='white', border_radius=20)
        pin = ft.TextField(hint_text='Clave de acceso', bgcolor='white', border_radius=20, password = True, can_reveal_password = True)
        barra = ft.Container(ft.ResponsiveRow([
            ft.Text('Sistema Integrador de calificaciones de lenguas extranjeras (SICLE)',
                font_family='Open-Sans',
                weight=ft.FontWeight.BOLD,
                size= 20,# Ajuste responsivo del tamaño del texto
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
                    ], alignment=ft.MainAxisAlignment.CENTER),bgcolor='white', width=page.width *0.4,  height=page.height * 0.05, border_radius=60, padding=page.width *0.002
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
            padding=20,
            width=page.width*0.5 if page.width < 600 else page.width*0.21,
            height=page.width*0.5 if page.width < 600 else page.width*0.21,
            bgcolor='#0D257C',
            border_radius=40,

        )

        login_container= ft.Container(
             content= formulario,
             expand= True,
             alignment=ft.alignment.center
        )

        def loginAlumno(id_alumno, password):
            user = "21350301"
            pin = "4955"
            if user != id_alumno:
                page.snack_bar = ft.SnackBar(ft.Text("ID de alumno no existe"), open=True)
                page.update()
            else:            
                if pin == password:
                    print("Inicio de sesión exitoso")
                    page.views.append(dataAlumno_view(page,id_usuario))
                    page.update()
                else:
                    page.snack_bar = ft.SnackBar(ft.Text("PIN incorrecto"), open=True)
                    page.update()
        return ft.View("/estudiante", [barra, login_container])
    