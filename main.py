import flet as ft

from main_view import main_view
from estudiante.estudiante_view import estudiante_view
from Administrador.admin_view import admin_view
from Docente.docente_view import docente_view

def main(page: ft.Page):
    page.title = "SICLE - Sistema Integrador de Calificaciones"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.favicon = "/assets/logo.ico"

    def goEstu(e):
        page.go('/estudiante')
    
    def goDoc(e):
        page.go('/docente')
    
    def goAdmin(e):
        page.go('/admin')

    def route_change(route):
        page.views.clear()
        if page.route == "/":
            page.views.append(main_view(page, goEstu, goDoc, goAdmin))  # Llama a main_view y pasa las funciones de navegación
        elif page.route == "/estudiante":
            page.views.append(estudiante_view(page))
        elif page.route == "/docente":
            page.views.append(docente_view(page))
        elif page.route == "/admin":
            page.views.append(admin_view(page))
        page.update()

    page.on_route_change = route_change
    page.go(page.route)

ft.app(target=main, view=ft.AppView.WEB_BROWSER, assets_dir="assets")