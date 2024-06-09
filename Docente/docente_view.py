import flet as ft
import requests
from Docente.dataDocente_view import dataDocente_view

def docente_view(page: ft.Page):
    id_docente = ft.TextField(
        hint_text='Usuario Docente',
        bgcolor='white',
        border_radius=10,
        adaptive=True
    )
    pin_docente = ft.TextField(
        hint_text='Clave de acceso',
        bgcolor='white',
        border_radius=10,
        password=True,
        can_reveal_password = True,
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

    def loginDocente(id_profesor, password):
        url = f"https://dbsicle1.viictor-axel11.workers.dev/loginProfesor?id_profesor={id_profesor}&pin={password}"
        response = requests.get(url)
        result = response.json()
        
        if not result['success']:
            page.snack_bar = ft.SnackBar(ft.Text(result['message']), open=True)
            page.update()
        else:
            print("Inicio de sesión exitoso")
            page.views.append(dataDocente_view(page, id_profesor))
            page.update()



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
                    id_docente, 
                    pin_docente
,
                ]),
                ft.Row([
                    ft.FilledButton('Aceptar',on_click = lambda e: loginDocente(id_docente.value, pin_docente.value), style=ft.ButtonStyle(bgcolor='#3F844B'))
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


    return ft.View("/docente", [barra, login_container])
