import reflex as rx
from splits import State


def pace() -> rx.Component:
    return rx.hstack(
        rx.text(
            "Pace: ",
            color_scheme="teal",
        ),
        rx.input(
            placeholder="HH",
            name="pace_hour",
            type="text",
            max_length=2,
            width="50px",
            on_change=State.set_pace_hours,
            value=State.pace_hours,
        ),
        rx.text(":"),
        rx.input(
            placeholder="MM",
            name="pace_minutes",
            type="text",
            max_length=2,
            width="50px",
            on_change=State.set_pace_minutes,
            value=State.pace_minutes,
        ),
        rx.text(":"),
        rx.input(
            placeholder="SS",
            name="pace_seconds",
            type="text",
            max_length=2,
            width="50px",
            on_change=State.set_pace_seconds,
            value=State.pace_seconds,
        ),
        text_align="center",
    )
