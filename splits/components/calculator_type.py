import reflex as rx
from splits import State


def calculator_type() -> rx.Component:
    return rx.select(
        [
            "Pace",
            "Time",
            "Distance",
        ],
        name="calculator_type",
        value=State.calculator_type,
        on_change=State.set_calculator_type,
        width="130px",
    )
