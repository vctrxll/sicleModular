import flet as ft
from Administrador.dataAdmin_view import dataAdmin_view


def admin_view(page: ft.Page):
        id_admin= ft.TextField(hint_text='Usuario administrador', bgcolor='white', border_radius=10, adaptive=True)
        pin_admin = ft.TextField(hint_text='Clave de acceso', bgcolor='white', border_radius=10,password = True, adaptive=True, can_reveal_password = True)
        barra = ft.Container(ft.ResponsiveRow([
            ft.Text('Sistema Integrador de calificaciones de lenguas extranjeras (SICLE)',
                font_family='Open-Sans',
                weight=ft.FontWeight.BOLD,
                size={"xs": 20, "sm": 25, "md": 30, "lg": 35},  # Ajuste responsivo del tamaño del texto
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
                    id_admin, 
                    pin_admin
,
                ]),
                ft.Row([
                    ft.FilledButton('Aceptar',on_click = lambda e: loginAdmin(id_admin.value, pin_admin.value), style=ft.ButtonStyle(bgcolor='#3F844B'))
                ], alignment=ft.MainAxisAlignment.CENTER),
            ]),
            padding=20,
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


        def loginAdmin(id_admin,password):
            user = "12"
            pin = "12"
            if user != id_admin:
                page.snack_bar = ft.SnackBar(ft.Text("ID no existe"), open=True)
                page.update()
            else:            
                if pin == password:
                    print("Inicio de sesión exitoso")
                    page.views.append(dataAdmin_view(page,id_admin))
                    page.update()
                else:
                    page.snack_bar = ft.SnackBar(ft.Text("PIN incorrecto"), open=True)
                    page.update()
    
        return ft.View("/admin", [barra, login_container])