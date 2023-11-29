import flet as ft
from flet import TextField, Checkbox, Dropdown, ElevatedButton, Text, Row, Column, Container, Stack, View
from flet_core import View
from flet_core.control import Control

theme = ft.Theme(color_scheme_seed='#5a189a')


def clear(e):
    pass


body = Row(
    [

        # Контейнер слева
        ft.Container(

            # Строка с контейнерами
            Column(
                controls=[

                    # Кнопка домой + помощь
                    Container(
                        Row(
                            controls=[

                                # Кнопка домой
                                ElevatedButton(
                                    "Home",
                                    style=ft.ButtonStyle(
                                        shape=ft.RoundedRectangleBorder(radius=5)
                                    ),
                                    scale=2,
                                    on_click=lambda e: e.page.go("/")
                                ),
                                ft.IconButton(icon=ft.icons.QUESTION_MARK,
                                              tooltip='Руководство',
                                              icon_size=50,
                                              style=ft.ButtonStyle(
                                                  shape=ft.CircleBorder()
                                              )
                                              )
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        ),
                        padding=ft.padding.symmetric(horizontal=40)
                    ),

                    IP_input := TextField(
                        label='IP-адрес',
                        hint_text='127.0.0.1',
                        helper_text='Введите IP-адрес',
                        autofocus=True,
                        text_size=26,
                        max_length=15,

                    ),

                    Mask_input := Dropdown(
                        label='Префикс/Маска',
                        hint_text='Выберите префикс/маску',
                        options=[
                            ft.dropdown.Option("0 - 000.000.000.000"),
                            ft.dropdown.Option("1 - 128.000.000.000"),
                            ft.dropdown.Option("2 - 192.000.000.000"),
                            ft.dropdown.Option("3 - 224.000.000.000"),
                            ft.dropdown.Option("4 - 240.000.000.000"),
                            ft.dropdown.Option("5 - 248.000.000.000"),
                            ft.dropdown.Option("6 - 252.000.000.000"),
                            ft.dropdown.Option("7 - 254.000.000.000"),
                            ft.dropdown.Option("8 - 255.000.000.000"),
                            ft.dropdown.Option("9 - 255.128.000.000"),
                            ft.dropdown.Option("10 - 255.192.000.000"),
                            ft.dropdown.Option("11 - 255.224.000.000"),
                            ft.dropdown.Option("12 - 255.240.000.000"),
                            ft.dropdown.Option("13 - 255.248.000.000"),
                            ft.dropdown.Option("14 - 255.252.000.000"),
                            ft.dropdown.Option("15 - 255.254.000.000"),
                            ft.dropdown.Option("16 - 255.255.000.000"),
                            ft.dropdown.Option("17 - 255.255.128.000"),
                            ft.dropdown.Option("18 - 255.255.192.000"),
                            ft.dropdown.Option("19 - 255.255.224.000"),
                            ft.dropdown.Option("20 - 255.255.240.000"),
                            ft.dropdown.Option("21 - 255.255.248.000"),
                            ft.dropdown.Option("22 - 255.255.252.000"),
                            ft.dropdown.Option("23 - 255.255.254.000"),
                            ft.dropdown.Option("24 - 255.255.255.000"),
                            ft.dropdown.Option("25 - 255.255.255.128"),
                            ft.dropdown.Option("26 - 255.255.255.192"),
                            ft.dropdown.Option("27 - 255.255.255.224"),
                            ft.dropdown.Option("28 - 255.255.255.240"),
                            ft.dropdown.Option("29 - 255.255.255.248"),
                            ft.dropdown.Option("30 - 255.255.255.252"),
                            ft.dropdown.Option("31 - 255.255.255.254"),
                            ft.dropdown.Option("32 - 255.255.255.255")

                        ],
                        text_size=26,
                    ),

                    # Кнопка очистить + подсчитать
                    Container(
                        Row(
                            controls=[
                                ElevatedButton(
                                    "Очистить",
                                    style=ft.ButtonStyle(
                                        shape=ft.RoundedRectangleBorder(radius=5)
                                    ),
                                    scale=1.5,
                                    icon=ft.icons.DELETE,
                                    on_click=clear
                                ),

                                ft.OutlinedButton(
                                    "Подсчитать",
                                    style=ft.ButtonStyle(
                                        shape=ft.RoundedRectangleBorder(radius=5)
                                    ),
                                    scale=1.5,
                                    icon=ft.icons.CHECK
                                )
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                        ),
                        padding=ft.padding.symmetric(horizontal=40)
                    )
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            width=700,
            bgcolor=ft.colors.BLACK45,
            border_radius=10,
            padding=60
        ),

        # Контейнер справа
        Container(
            Column(

            ),
            expand=True,
            bgcolor=ft.colors.BLACK45,
            border_radius=10,
            padding=60
        )

    ],
    expand=True,
    spacing=30
)


def _view_() -> View:
    return View(
        "/ipcalc",
        controls=[
            body
        ],
        padding=30
    )
