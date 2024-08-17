import flet as ft
def main(page:ft.Page):
    page.title="contador"
    page.vertical_alignment=ft.MainAxisAlignment.CENTER
    text_number=ft.TextField(value="0",text_align=ft.TextAlign.CENTER,width=80,disabled=True)
    
    def menos(e):
        text_number.value=str(int(text_number.value)-1)
        text_number.update()
    def mais(e):
        text_number.value=str(int(text_number.value)+1)
        text_number.update()
    page.add(
        ft.Row(
            controls=[
                ft.IconButton(icon=ft.icons.REMOVE,on_click=menos),
                text_number,
                ft.IconButton(icon=ft.icons.ADD,on_click=mais),
                
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )
    page.update()

if __name__=="__main__":
    ft.app(target=main)