import flet as ft
from app import *
import sqlite3
dbb = []
dbdaily = [0,0,0,0,0,0,0]
total = 0

def main(page):
    db2 = Database()
    global dbdaily
    dbdaily = db2.get_dailytotals()
    global total
    for n in dbdaily:
        total += n
    def btn_click(e):
        if not txt_name.value or not txt_cal.value or not txt_date.value:
            txt_name.error_text = "Please enter your Meal Name"
            txt_cal.error_text = "Please enter your meal calorie amount"
            txt_date.error_text = "Please enter the date of your meal"
            page.update()
        else:
            db = Database()
            db.insert_table(txt_name.value,txt_cal.value,txt_date.value,txt_meal.value)
            global dbb
            dbb = db.get_table()
            global dbdaily
            dbdaily = db.get_dailytotals()
            global total
            total = 0
            for n in dbdaily:
                total += n
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
            height=525,
            border_radius=30,
            gradient=ft.LinearGradient(
                begin=ft.alignment.top_left,
                end=ft.alignment.bottom_right,
                colors=["#0f766e", "#064e3b"],
            )
        )
        textwelcome = ft.Container(
            width=290,
            height=200,
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
                                                    f"To My Dietary Application!",
                                                    size=18,
                                                    weight="bold",
                                                    color="white70",
                                                ),
                                                ft.Text(
                                                    f"This weeks total calorie count is,",
                                                    size=12,
                                                    weight="bold",
                                                    color="white70",
                                                ),
                                                ft.Text(
                                                    f"{total} Calories",
                                                    size=35,
                                                    weight="bold",
                                                    color="white70",
                                                ),
                                                ft.Container(
                                                    padding=ft.padding.only(
                                                        top=100,
                                                    )
                                                ),
                                            ]
                                        )
                                    ]
                                )
                            ),
                            ft.Container(
                                padding=ft.padding.only(3,0,3,40),
                                content=ft.BarChart(
                                    bar_groups=[
                                        ft.BarChartGroup(
                                            x=0,
                                            bar_rods=[
                                                ft.BarChartRod(
                                                    from_y=0,
                                                    to_y=dbdaily[6],
                                                    width=20,
                                                    color=ft.colors.BLACK,
                                                    tooltip=f"{dbdaily[6]} cal",
                                                    border_radius=0,
                                                ),
                                            ],
                                        ),
                                        ft.BarChartGroup(
                                            x=1,
                                            bar_rods=[
                                                ft.BarChartRod(
                                                    from_y=0,
                                                    to_y=dbdaily[0],
                                                    width=20,
                                                    color=ft.colors.BLACK,
                                                    tooltip=f"{dbdaily[0]} cal",
                                                    border_radius=0,
                                                ),
                                            ],
                                        ),
                                        ft.BarChartGroup(
                                            x=2,
                                            bar_rods=[
                                                ft.BarChartRod(
                                                    from_y=0,
                                                    to_y=dbdaily[1],
                                                    width=20,
                                                    color=ft.colors.BLACK,
                                                    tooltip=f"{dbdaily[1]} cal",
                                                    border_radius=0,
                                                ),
                                            ],
                                        ),
                                        ft.BarChartGroup(
                                            x=3,
                                            bar_rods=[
                                                ft.BarChartRod(
                                                    from_y=0,
                                                    to_y=dbdaily[2],
                                                    width=20,
                                                    color=ft.colors.BLACK,
                                                    tooltip=f"{dbdaily[2]} cal",
                                                    border_radius=0,
                                                ),
                                            ],
                                        ),
                                        ft.BarChartGroup(
                                            x=4,
                                            bar_rods=[
                                                ft.BarChartRod(
                                                    from_y=0,
                                                    to_y=dbdaily[3],
                                                    width=20,
                                                    color=ft.colors.BLACK,
                                                    tooltip=f"{dbdaily[3]} cal",
                                                    border_radius=0,
                                                ),
                                            ],
                                        ),
                                        ft.BarChartGroup(
                                            x=5,
                                            bar_rods=[
                                                ft.BarChartRod(
                                                    from_y=0,
                                                    to_y=dbdaily[4],
                                                    width=20,
                                                    color=ft.colors.BLACK,
                                                    tooltip=f"{dbdaily[4]} cal",
                                                    border_radius=0,
                                                ),
                                            ],
                                        ),
                                        ft.BarChartGroup(
                                            x=6,
                                            bar_rods=[
                                                ft.BarChartRod(
                                                    from_y=0,
                                                    to_y=dbdaily[5],
                                                    width=20,
                                                    color=ft.colors.BLACK,
                                                    tooltip=f"{dbdaily[5]} cal",
                                                    border_radius=0,
                                                ),
                                            ],
                                        ),
                                    ],
                                    border=ft.border.all(8, ft.colors.BLACK87),
                                    left_axis=ft.ChartAxis(
                                        labels_size=0, title=ft.Text("Calories"), title_size=0
                                    ),
                                    bottom_axis=ft.ChartAxis(
                                        labels=[
                                            ft.ChartAxisLabel(
                                                value=0,
                                                label=ft.Container(ft.Text("SUN"), padding=3)
                                            ),
                                            ft.ChartAxisLabel(
                                                value=1,
                                                label=ft.Container(ft.Text("MON"), padding=3)
                                            ),
                                            ft.ChartAxisLabel(
                                                value=2,
                                                label=ft.Container(ft.Text("TUES"), padding=3)
                                            ),
                                            ft.ChartAxisLabel(
                                                value=3,
                                                label=ft.Container(ft.Text("WED"), padding=3)
                                            ),
                                            ft.ChartAxisLabel(
                                                value=4,
                                                label=ft.Container(ft.Text("THUR"), padding=3)
                                            ),
                                            ft.ChartAxisLabel(
                                                value=5,
                                                label=ft.Container(ft.Text("FRI"), padding=3)
                                            ),
                                            ft.ChartAxisLabel(
                                                value=6,
                                                label=ft.Container(ft.Text("SAT"), padding=3)
                                            ),
                                        ],
                                        labels_size=25,
                                    ),
                                    horizontal_grid_lines=ft.ChartGridLines(
                                        color=ft.colors.GREY_300, width=1, dash_pattern=[3, 3]
                                    ),
                                    tooltip_bgcolor=ft.colors.with_opacity(0.5, ft.colors.GREY_300),
                                    max_y=3000,
                                    interactive=True,
                                    expand=True,
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

    txt_name = ft.TextField(label="Meal Name",width=200,text_size=20,color='grey')
    txt_cal = ft.TextField(label="Calorie Count",width=200,color='grey')
    txt_meal = ft.Dropdown(label="Type Meal",
                           options=[ft.dropdown.Option("Breakfast"),
                           ft.dropdown.Option("Lunch"),
                           ft.dropdown.Option("Dinner"),],width=200,color='grey')
    txt_date = ft.Dropdown(label="Day of Meal",color='grey',text_size=15,
                           options=[ft.dropdown.Option("Monday"),
                                    ft.dropdown.Option("Tuesday"),
                                    ft.dropdown.Option("Wednesday"),
                                    ft.dropdown.Option("Thursday"),
                                    ft.dropdown.Option("Friday"),
                                    ft.dropdown.Option("Saturday"),
                                    ft.dropdown.Option("Sunday")], width=200)
    mainpage()

ft.app(target=main)