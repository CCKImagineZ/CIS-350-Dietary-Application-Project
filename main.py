import flet as ft
from app import *

def main(page):

    def btn_click(e):
        if not txt_name.value or not txt_cal.value or not txt_date.value:
            txt_name.error_text = "Please enter your Meal Name"
            txt_cal.error_text = "Please enter your meal calorie amount"
            txt_date.error_text = "Please enter the date of your meal"
            page.update()
        else:
            x = Data(txt_name.value,txt_cal.value,txt_meal.value,txt_date.value)
            print(x.get_data())
            page.clean()
            mainpage()

    def buttonclick(e):
        page.clean()
        mealentry = ft.Container(
            width=290,
            height=600,
            bgcolor="black",
            border_radius=35,
            padding=8,
            animate=ft.animation.Animation(1000,"bounceOut"),
        )
        mealentryborder = ft.Container(
            width=290,
            height=580,
            border_radius=30,
            gradient=ft.LinearGradient(
                begin=ft.alignment.top_left,
                end=ft.alignment.bottom_right,
                colors=["#0f766e","#064e3b"],
            )
        )
        mealentryvals = ft.Container(
            width=290,
            height=580,
            visible=True,
            content=ft.Row(
                spacing=10,
                controls=[
                    ft.Column(
                        expand=4,
                        controls=[
                            ft.Container(
                                padding=ft.padding.only(top=145,left=35),
                                expand=True,
                                content=ft.Row(
                                    controls=[
                                        ft.Column(
                                            controls=[
                                                txt_name,
                                                txt_cal,
                                                txt_date,
                                                txt_meal,
                                                ft.ElevatedButton("Submit Meal",bgcolor='black',color='white', on_click=btn_click,width=200),
                                            ]
                                        )
                                    ]
                                )
                            )
                        ]
                    )
                ]
            )
        )
        mealentry_col = ft.Column()
        mealentry.content = mealentry_col
        mealentry_col.controls.append(mealentryborder)
        mealentryborder.content = mealentryvals
        page.add(mealentry)

    def mainpage():
        phonebackground = ft.Container(
            width=290,
            height=600,
            bgcolor="black",
            border_radius=35,
            padding=8,
        )
        welcomemenu = ft.Container(
            width=290,
            height=500,
            border_radius=30,
            gradient=ft.LinearGradient(
                begin=ft.alignment.top_left,
                end=ft.alignment.bottom_right,
                colors=["#0f766e", "#064e3b"],
            )
        )
        textwelcome = ft.Container(
            width=290,
            height=500,
            visible=True,
            content=ft.Row(
                spacing=0,
                controls=[
                    ft.Column(
                        expand=4,
                        controls=[
                            ft.Container(
                                padding=20,
                                expand=True,
                                content=ft.Row(
                                    controls=[
                                        ft.Column(
                                            controls=[
                                                ft.Text(
                                                    "Welcome",
                                                    size=10,
                                                    color="white70",
                                                ),
                                                ft.Text(
                                                    "To our Dietary Application!",
                                                    size=18,
                                                    weight="bold",
                                                    color="white70",
                                                ),
                                                ft.Container(
                                                    padding=ft.padding.only(
                                                        top=10,
                                                    )
                                                ),
                                                ft.Text(
                                                    "Total Calories",
                                                    size=10,
                                                    color="white70",
                                                ),
                                                ft.Text(
                                                    '150 Calories',
                                                    size=22,
                                                    weight="bold",
                                                    color="white70",
                                                ),
                                            ]
                                        )
                                    ]
                                )
                            )
                        ]
                    )
                ]
            )
        )
        buttonmain = ft.Container(
            width=290,
            height=50,
            bgcolor="black",
            margin=0,
            alignment=ft.alignment.center,
            border_radius=10,
            content=ft.Column(
                spacing=20,
                controls=[
                    ft.Container(
                        content=ft.ElevatedButton(
                            "Add Meal",
                            icon_color='blue',
                            icon=ft.icons.FASTFOOD,
                            height=50,
                            width=140,
                            style=ft.ButtonStyle(shape=ft.ContinuousRectangleBorder(radius=30)),
                            on_click=buttonclick,
                        ),
                    ),
                ]
            )
        )
        mainpage_col = ft.Column()
        phonebackground.content = mainpage_col
        mainpage_col.controls.append(welcomemenu)
        welcomemenu.content = textwelcome
        mainpage_col.controls.append(buttonmain)
        buttonmain.alignment = ft.alignment.center
        page.add(phonebackground)

    txt_name = ft.TextField(label="Meal Name",width=200,text_size=20,border_color='white',color='white')
    txt_cal = ft.TextField(label="Calorie Count",width=200)
    txt_meal = ft.Dropdown(label="Type Meal",
                           options=[ft.dropdown.Option("Breakfast"),
                           ft.dropdown.Option("Lunch"),
                           ft.dropdown.Option("Dinner"),],width=200)
    txt_date = ft.TextField(label="Date of Meal",width=200)
    mainpage()

ft.app(target=main)