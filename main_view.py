import flet as ft
def main_view(page: ft.Page, goEstu, goDoc,goAdmin):
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

        logo = ft.ResponsiveRow([
        ft.Column([ft.Image('https://i.postimg.cc/PrFD80ML/4.png', width=150, height=150, border_radius=150),
                   ft.Text('Instituto Tecnologico de Tuxtepec', text_align='center'),],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=10,  # Espacio entre elementos en la fila
            run_spacing={"xs": 5, "sm": 10, "md": 15, "lg": 20} )
        
        opciones = ft.Container(
            expand=True,
            content= ft.Column(
                scroll="auto",
                controls=[
                    ft.ResponsiveRow([
                    ft.Container(
                        ft.Column([
                                ft.Image(src="https://i.postimg.cc/x1VBNBmk/1.png", width=120, height=120),
                                ft.TextButton(content=ft.Container(ft.Text(value="Estudiante", weight=ft.FontWeight.W_700, size=20, color="black", text_align='center')),on_click=goEstu),
                                ft.Text('Modulo de Consultas y servicios para los estudiantes', text_align='center', width=150),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                        col={"xs": 12, "sm": 6, "md": 4, "lg": 3}
                    ),
                    ft.Container(
                        ft.Column(
                            [
                                ft.Image(src="https://i.postimg.cc/1XvqBdhj/2.png", width=120, height=120),
                                ft.TextButton(
                                    content=ft.Container(
                                        ft.Text(value="Docente", weight=ft.FontWeight.W_700, size=20, color="black", text_align='center')
                                    ),
                                    on_click=goDoc
                                ),
                                ft.Text('Modulo de Consultas y Actividades', text_align='center', width=150),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER
                        ),
                        col={"xs": 12, "sm": 6, "md": 4, "lg": 3}
                    ),
                    ft.Container(
                        ft.Column(
                            [
                                ft.Image(src="https://i.postimg.cc/HWzXTrc9/3.png", width=120, height=120),
                                ft.TextButton(
                                    content=ft.Container(
                                        ft.Text(value="Administrador", weight=ft.FontWeight.W_700, size=20, color="black", text_align='center')
                                    ),
                                    on_click=goAdmin
                                ),
                                ft.Text('Modulo de Consultas', text_align='center', width=150),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER
                        ),
                        col={"xs": 12, "sm": 6, "md": 4, "lg": 3}
                    )
                        ],
                vertical_alignment=ft.MainAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=30,
                run_spacing={"xs": 20, "sm": 30}
                    )
                ]
            ),padding=20
        )
        return ft.View("/", [barra, logo, opciones])