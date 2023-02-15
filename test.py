import flet as ft


def main(page: ft.Page):

    page.add(
        ft.Text("1"),
        ft.Text("1"),
        ft.Text("1"),
        
        ft.Column([
            ft.Text("2"),
            ft.Text("2"),
            ft.Text("2"),
        ]),

        ft.Row([
            ft.Text("3"),
            ft.Text("3"),
            ft.Text("3"),
        ]),


        ft.Column([
            ft.Row([
                ft.Text("4"),
                ft.Text("4"),
                ft.Text("4"),
            ]),

            ft.Row([
                ft.Text("4"),
                ft.Text("4"),
                ft.Text("4"),
            ]),
        ]),

        ft.Row([
            ft.Column([
                ft.Text("5"),
                ft.Text("5"),
                ft.Text("5"),
            ]),

            ft.Column([
                ft.Text("5"),
                ft.Text("5"),
                ft.Text("5"),
            ]),

        ]),

    )


ft.app(target=main)
