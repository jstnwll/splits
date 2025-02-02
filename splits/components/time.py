import reflex as rx
from splits import State


def time() -> rx.Component:
    return rx.hstack(
        rx.text(
            "Time: ",
            color_scheme="teal",
        ),
        rx.input(
            placeholder="HH",
            name="time_hours",
            type="text",
            max_length=2,
            width="50px",
            on_change=State.set_time_hours,
            value=State.time_hours,
        ),
        rx.text(":"),
        rx.input(
            placeholder="MM",
            name="time_minutes",
            type="text",
            max_length=2,
            width="50px",
            on_change=State.set_time_minutes,
            value=State.time_minutes,
        ),
        rx.text(":"),
        rx.input(
            placeholder="SS",
            name="time_seconds",
            type="text",
            max_length=2,
            width="50px",
            on_change=State.set_time_seconds,
            value=State.time_seconds,
        ),
    )
