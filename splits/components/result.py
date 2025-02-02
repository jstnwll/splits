import reflex as rx
from splits import State


def result() -> rx.Component:
    return rx.vstack(
        rx.card(
            rx.center(
                rx.heading(
                    State.result,
                    align="center",
                    size="9",
                ),
            ),
            size="3",
        ),
    )
