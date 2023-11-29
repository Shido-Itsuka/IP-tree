import flet as ft
from flet import TextField, Checkbox, ElevatedButton, Text, Row, Column, Container, Stack, View
from flet_core import View
from flet_core.control import Control


def _view_() -> View:
    return View(
        "/iptree",
        controls=[
            ft.ElevatedButton("Go Home", on_click=lambda e: e.page.go("/"))
        ]
    )
