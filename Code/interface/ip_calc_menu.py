import flet as ft
from flet import (TextField, Dropdown, ElevatedButton, Text, Row, Column, Container, Stack, View, TextButton, DataCell,
                  DataTable, DataRow, DataColumn)
from flet_core import View, ControlEvent
import sys

sys.path.append('../')
# noinspection PyUnresolvedReferences
from modules.ip_calculator_module import IP_Calculator

theme = ft.Theme(color_scheme_seed='#5a189a',
                 color_scheme=ft.ColorScheme(
                     background='#0f0f0f',
                     primary_container='#272727'

                 ))


def validate(e: ControlEvent) -> None:
    if all([IP_input.value, Mask_input.value]):
        calc_button.disabled = False
    else:
        calc_button.disabled = True
    calc_button.update()


def clear(e):
    IP_cell.text = ""
    IP_cell_bin.text = ""
    Prefix_cell.text = ""
    Prefix_cell_bin.text = ""
    Netmask_cell.text = ""
    Netmask_cell_bin.text = ""
    Wildcard_cell.text = ""
    Wildcard_cell_bin.text = ""
    Network_cell.text = ""
    Network_cell_bin.text = ""
    Broadcast_cell.text = ""
    Broadcast_cell_bin.text = ""
    Hostmin_cell.text = ""
    Hostmin_cell_bin.text = ""
    Hostmax_cell.text = ""
    Hostmax_cell_bin.text = ""
    Hosts_cell.text = ""
    Hosts_cell_bin.text = ""
    out_table.update()

    IP_input.value = ""
    IP_input.error_text = ""
    IP_input.update()

    Mask_input.value = ""
    Mask_input.update()

    IP_input.focus()
    calc_button.disabled = True
    calc_button.update()


def calculate(e):
    try:
        out = IP_Calculator(IP_input.value, int(Mask_input.value)).main()
        print('\n\n', '-'*55, sep='')
        [print(*x, sep=' | ', end='\n') for x in out]
        print('-'*55, end='\n\n')
        IP_cell.text = out[0][0]
        IP_cell_bin.text = out[0][1]
        Prefix_cell.text = out[1][0]
        Prefix_cell_bin.text = out[1][1]
        Netmask_cell.text = out[2][0]
        Netmask_cell_bin.text = out[2][1]
        Wildcard_cell.text = out[3][0]
        Wildcard_cell_bin.text = out[3][1]
        Network_cell.text = out[4][0]
        Network_cell_bin.text = out[4][1]
        Broadcast_cell.text = out[5][0]
        Broadcast_cell_bin.text = out[5][1]
        Hostmin_cell.text = out[6][0]
        Hostmin_cell_bin.text = out[6][1]
        Hostmax_cell.text = out[7][0]
        Hostmax_cell_bin.text = out[7][1]
        Hosts_cell.text = out[8][0]
        Hosts_cell_bin.text = out[8][1]

        out_table.update()

    except ValueError as e:
        print(e)
        IP_input.error_text = e
        IP_input.update()
    else:
        IP_input.error_text = ""
        IP_input.update()


def error_clear(e: ControlEvent) -> None:
    if IP_input.error_text:
        if IP_input.value != error_ip:
            IP_input.error_text = ""
            IP_input.update()


def copy_to_clipboard(p: ft.Page, out):
    p.set_clipboard(out)
    p.update()


def copy_cell_value(e: ControlEvent) -> None:
    if len(str(e.control.text)) > 0:
        copy_to_clipboard(e.page, str(e.control.text))
        print(f"COPIED: {e.control.text}")
    else:
        print("EMPTY")


def text_button_style(theme: ft.Page.theme_mode, mode: int) -> dict[str, any]:
    if mode == 1:
        return {
            "style": ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(),
                color="#e9b8ff",
            ),
            "on_click": copy_cell_value,
        }
    elif mode == 2:
        return {
            "style": ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(),
                color="#ceffb8",
            ),
            "on_click": copy_cell_value
        }


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
                        label='Введите IP-адрес',
                        hint_text='127.0.0.1',
                        autofocus=True,
                        text_size=26,
                        max_length=15,
                        input_filter=ft.InputFilter(
                            allow=True,
                            regex_string=r"^[0-9\.]*$",
                            replacement_string='',
                        ),
                        border_color=ft.colors.WHITE54,
                        focused_border_color='#dbb8ff',
                        on_change=validate
                    ),

                    Mask_input := Dropdown(
                        label='Префикс/Маска',
                        hint_text='Выберите префикс/маску',
                        options=[
                            ft.dropdown.Option(0, "0 - 000.000.000.000"),
                            ft.dropdown.Option(1, "1 - 128.000.000.000"),
                            ft.dropdown.Option(2, "2 - 192.000.000.000"),
                            ft.dropdown.Option(3, "3 - 224.000.000.000"),
                            ft.dropdown.Option(4, "4 - 240.000.000.000"),
                            ft.dropdown.Option(5, "5 - 248.000.000.000"),
                            ft.dropdown.Option(6, "6 - 252.000.000.000"),
                            ft.dropdown.Option(7, "7 - 254.000.000.000"),
                            ft.dropdown.Option(8, "8 - 255.000.000.000"),
                            ft.dropdown.Option(9, "9 - 255.128.000.000"),
                            ft.dropdown.Option(10, "10 - 255.192.000.000"),
                            ft.dropdown.Option(11, "11 - 255.224.000.000"),
                            ft.dropdown.Option(12, "12 - 255.240.000.000"),
                            ft.dropdown.Option(13, "13 - 255.248.000.000"),
                            ft.dropdown.Option(14, "14 - 255.252.000.000"),
                            ft.dropdown.Option(15, "15 - 255.254.000.000"),
                            ft.dropdown.Option(16, "16 - 255.255.000.000"),
                            ft.dropdown.Option(17, "17 - 255.255.128.000"),
                            ft.dropdown.Option(18, "18 - 255.255.192.000"),
                            ft.dropdown.Option(19, "19 - 255.255.224.000"),
                            ft.dropdown.Option(20, "20 - 255.255.240.000"),
                            ft.dropdown.Option(21, "21 - 255.255.248.000"),
                            ft.dropdown.Option(22, "22 - 255.255.252.000"),
                            ft.dropdown.Option(23, "23 - 255.255.254.000"),
                            ft.dropdown.Option(24, "24 - 255.255.255.000"),
                            ft.dropdown.Option(25, "25 - 255.255.255.128"),
                            ft.dropdown.Option(26, "26 - 255.255.255.192"),
                            ft.dropdown.Option(27, "27 - 255.255.255.224"),
                            ft.dropdown.Option(28, "28 - 255.255.255.240"),
                            ft.dropdown.Option(29, "29 - 255.255.255.248"),
                            ft.dropdown.Option(30, "30 - 255.255.255.252"),
                            ft.dropdown.Option(31, "31 - 255.255.255.254"),
                            ft.dropdown.Option(32, "32 - 255.255.255.255")

                        ],
                        text_size=22,
                        border_color=ft.colors.WHITE54,
                        focused_border_color='#dbb8ff',
                        on_change=validate
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

                                calc_button := ft.OutlinedButton(
                                    "Подсчитать",
                                    style=ft.ButtonStyle(
                                        shape=ft.RoundedRectangleBorder(radius=5)
                                    ),
                                    scale=1.5,
                                    icon=ft.icons.CHECK,
                                    on_click=calculate,
                                    disabled=True
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
                controls=[
                    out_table := DataTable(
                        columns=[
                            DataColumn(Text(
                                "Параметр",
                                weight=ft.FontWeight.BOLD
                            )),
                            DataColumn(Text(
                                "Десятичное значение",
                                weight=ft.FontWeight.BOLD
                            )),
                            DataColumn(Text(
                                "Двоичное значение",
                                weight=ft.FontWeight.BOLD
                            )),
                        ],
                        rows=[
                            DataRow(
                                cells=[
                                    DataCell(Text("IP-адрес")),
                                    DataCell(IP_cell := TextButton(
                                        "",
                                        **text_button_style(theme, 1),

                                    ),),
                                    DataCell(IP_cell_bin := TextButton(
                                        "",
                                        **text_button_style(theme, 2)
                                    )),
                                ],
                            ),
                            DataRow(
                                cells=[
                                    DataCell(Text("Префикс")),
                                    DataCell(Prefix_cell := TextButton(
                                        "",
                                        **text_button_style(theme, 1)
                                    )),
                                    DataCell(Prefix_cell_bin := TextButton(
                                        "",
                                        **text_button_style(theme, 2)
                                    )),
                                ],
                            ),
                            DataRow(
                                cells=[
                                    DataCell(Text("Маска")),
                                    DataCell(Netmask_cell := TextButton(
                                        "",
                                        **text_button_style(theme, 1)
                                    )),
                                    DataCell(Netmask_cell_bin := TextButton(
                                        "",
                                        **text_button_style(theme, 2)
                                    )),
                                ],
                            ),
                            DataRow(
                                cells=[
                                    DataCell(Text("Обратная маска")),
                                    DataCell(Wildcard_cell := TextButton(
                                        "",
                                        **text_button_style(theme, 1)
                                    )),
                                    DataCell(Wildcard_cell_bin := TextButton(
                                        "",
                                        **text_button_style(theme, 2)
                                    )),
                                ],
                            ),
                            DataRow(
                                cells=[
                                    DataCell(Text("Номер сети")),
                                    DataCell(Network_cell := TextButton(
                                        "",
                                        **text_button_style(theme, 1)
                                    )),
                                    DataCell(Network_cell_bin := TextButton(
                                        "",
                                        **text_button_style(theme, 2)
                                    )),
                                ],
                            ),
                            DataRow(
                                cells=[
                                    DataCell(Text("Широковещательный IP-адрес")),
                                    DataCell(Broadcast_cell := TextButton(
                                        "",
                                        **text_button_style(theme, 1)
                                    )),
                                    DataCell(Broadcast_cell_bin := TextButton(
                                        "",
                                        **text_button_style(theme, 2)
                                    )),
                                ],
                            ),
                            DataRow(
                                cells=[
                                    DataCell(Text("IP-адрес первого хоста")),
                                    DataCell(Hostmin_cell := TextButton(
                                        "",
                                        **text_button_style(theme, 1)
                                    )),
                                    DataCell(Hostmin_cell_bin := TextButton(
                                        "",
                                        **text_button_style(theme, 2)
                                    )),
                                ],
                            ),
                            DataRow(
                                cells=[
                                    DataCell(Text("IP-адрес последнего хоста")),
                                    DataCell(Hostmax_cell := TextButton(
                                        "",
                                        **text_button_style(theme, 1)
                                    )),
                                    DataCell(Hostmax_cell_bin := TextButton(
                                        "",
                                        **text_button_style(theme, 2)
                                    )),
                                ],
                            ),
                            DataRow(
                                cells=[
                                    DataCell(Text("Количество хостов")),
                                    DataCell(Hosts_cell := TextButton(
                                        "",
                                        **text_button_style(theme, 1)
                                    )),
                                    DataCell(Hosts_cell_bin := TextButton(
                                        "",
                                        **text_button_style(theme, 2)
                                    )),
                                ],
                            ),
                        ],
                        border=ft.border.all(
                            width=3,
                            color=ft.colors.WHITE54
                        ),
                        border_radius=5,
                        vertical_lines=ft.border.BorderSide(2, ft.colors.WHITE54),
                        horizontal_lines=ft.border.BorderSide(2, ft.colors.WHITE54),
                        scale=1.3
                    ),

                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.CENTER
            ),
            expand=True,
            bgcolor=ft.colors.BLACK45,
            border_radius=10,
            padding=60,
            alignment=ft.alignment.center
        )

    ],
    expand=True,
    spacing=30,

)


def _view_() -> View:
    return View(
        "/ipcalc",
        controls=[
            body
        ],
        padding=30,
        # bgcolor=ft.colors.BLACK45
    )
