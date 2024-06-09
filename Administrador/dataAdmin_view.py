
import flet as ft

def dataAdmin_view(page: ft.Page, id):

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
            grupos.visible = False
            consultas.visible = True
            liberacion.visible = False
            page.update()

        elif(e.control.selected_index == 1):
            grupos.visible = True
            consultas.visible = False
            liberacion.visible = False
            page.update()

        elif(e.control.selected_index == 2):
            liberacion.visible = True
            consultas.visible = False
            grupos.visible = False
            page.update()
        elif(e.control.selected_index == 3):
            page.go("/")

    navigation_rail = ft.NavigationRail(
        selected_index=0,
        destinations=[
            ft.NavigationDrawerDestination(
                icon_content=ft.Icon(ft.icons.PERSON),
                label="Consultas"
            ),
            ft.NavigationDrawerDestination(
                icon_content=ft.Icon(ft.icons.SCHEDULE),
                label="Grupos"
            ),
            ft.NavigationDrawerDestination(
                icon_content=ft.Icon(ft.icons.FORMAT_LIST_NUMBERED),
                label="Auditorias"
            ),
            ft.NavigationDrawerDestination(
                icon_content=ft.Icon(ft.icons.HIGHLIGHT_OFF),
                label="Salir"
            ),
        ],
        on_change=opciones,
        visible=False
    )

    consultas = ft.Container(
        ft.Row([
            ft.Container(content=ft.Text('Consultas',color='white',text_align='center',size=20),bgcolor='#0D257C',
                         width=250,height=50,alignment=ft.alignment.center,border_radius=30)
        ],alignment=ft.MainAxisAlignment.CENTER),
    )

    grupos = ft.Container(
        ft.Row([
            ft.Container(content=ft.Text('Grupos',color='white',text_align='center',size=20),bgcolor='#0D257C',
                         width=250,height=50,alignment=ft.alignment.center,border_radius=30)
        ],alignment=ft.MainAxisAlignment.CENTER),
    )

    liberacion = ft.Container(
        ft.Row([
            ft.Container(content=ft.Text('Auditoria',color='white',text_align='center',size=20),bgcolor='#0D257C',
                         width=250,height=50,alignment=ft.alignment.center,border_radius=30)
        ],alignment=ft.MainAxisAlignment.CENTER),
    )

    layout = ft.Row(
        [
            navigation_rail,
            ft.VerticalDivider(width=1),
            ft.Container(
                ft.Stack([consultas,grupos,liberacion]),
                expand=True
            )
        ],
        expand=True
    )

    
    navigation_rail.visible = True
    return ft.View("/admin", [barra,layout])