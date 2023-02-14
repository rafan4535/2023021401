'''
In this section, we are creating a To-Do App.
'''

# importing the library
import flet as ft


# defining the main function
def main(page: ft.Page):
    page.title = "Flet Counter App"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER

    txt = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)

    # Defining Minus Function
    def minus(e):
        txt.value = str(int(txt.value) - 1)
        page.update()

    def plus(e):
        txt.value = str(int(txt.value) + 1)
        page.update()

    page.add(
        ft.Column(
            [
                ft.Text(value="Flet Counter App"),
                
                ft.Row(
                    [
                        ft.IconButton(ft.icons.REMOVE, on_click=minus),
                        txt,
                        ft.IconButton(ft.icons.ADD, on_click=plus),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )


ft.app(target=main)
