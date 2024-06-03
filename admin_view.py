import flet as ft
def admin_view(page: ft.Page):
        barra = ft.Container(ft.ResponsiveRow([
            ft.Text(
                'Sistema Integrador de calificaciones de lenguas extranjeras (SICLE)',
                font_family='Open-Sans',
                weight=ft.FontWeight.BOLD,
                size={"xs": 20, "sm": 25, "md": 30, "lg": 35},  # Ajuste responsivo del tamaño del texto
                color='white',
                text_align='center'
            )], 
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=1,  # Espacio entre elementos en la fila
        run_spacing={"xs": 5, "sm": 10, "md": 15, "lg": 20} ),
                bgcolor='#0D257C',
                padding=10,
                height=60,)


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
                    ft.TextField(hint_text='Usuario Administrador', bgcolor='white', border_radius=10, width=380, height=50),
                    ft.TextField(hint_text='Clave de acceso', bgcolor='white', border_radius=10, width=380, height=50, password = True, adaptive=True),
                ]),
                ft.Row([
                    ft.FilledButton('Aceptar', style=ft.ButtonStyle(bgcolor='#3F844B'))
                ], alignment=ft.MainAxisAlignment.CENTER),
            ]),
            padding=20,
            width=page.width*0.9 if page.width < 600 else page.width*0.3,
            height=page.width*0.9 if page.width < 600 else page.width*0.3,
            bgcolor='#0D257C',
            border_radius=40,
            margin=ft.margin.only(top=80, left=page.width*0.05 if page.width < 600 else page.width*0.35)
        )

        return ft.View("/admin", [barra, container])