'''
In this section, we are creating a To-Do App.
'''

# importing the library
import flet as ft


# defining the main function
def main(page: ft.Page):
    page.title = "Flet To-Do App"

    # input text field
    input_text_field = ft.TextField(hint_text="Add Tasks", width=250)

    # defining add button function
    def button_add_task(e):
        page.add(ft.Checkbox(label=input_text_field.value))

    # page layout
    page.add(
        ft.Row(
            [
                input_text_field,
                ft.IconButton(ft.icons.ADD, on_click=button_add_task)
            ]
        )
    )


# calling the app
ft.app(target=main)
