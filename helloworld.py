#!/usr/bin/env python3

import os
import flet as ft

def main(page: ft.Page) -> None:

    def button_clicked(e) -> None:
        page.window_destroy()

    page.title = os.path.basename(__file__)
    page.window_width = 300
    page.window_height = 150
    page.window_center()
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    text = ft.Text('hello, world')
    button = ft.ElevatedButton('OK', on_click=button_clicked)
    page.add(text, button)

    page.window_visible = True
    page.update()

ft.app(target=main, view=ft.FLET_APP_HIDDEN)
# ft.app(target=main, view=ft.WEB_BROWSER)
