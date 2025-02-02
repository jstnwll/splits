import reflex as rx
from splits import components
from splits import State


def index() -> rx.Component:
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.form.root(
            rx.vstack(
                components.header(),
                components.result(),
                components.calculator_type(),
                # components.miles_or_km(),
                rx.cond(
                    State.view_pace,
                    components.pace(),
                ),
                rx.cond(
                    State.view_time,
                    components.time(),
                ),
                rx.cond(
                    State.view_distance,
                    components.distance(),
                ),
                align="center",
                spacing="5",
                height="80vh",
                justify_content="center",
            ),
        ),
    )


app = rx.App(
    theme=rx.theme(
        has_background=True,
        appearance="inherit",
        accent_color="teal",
        radius="large",
    )
)
app.add_page(index, route="/")
