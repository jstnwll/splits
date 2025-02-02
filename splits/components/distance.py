import reflex as rx
from splits import State


def distance() -> rx.Component:
    return rx.hstack(
        rx.text(
            "Distance: ",
            color_scheme="teal",
        ),
        rx.select(
            [
                "5k",
                "10k",
                "Half Marathon",
                "Marathon",
                "50k",
                "50 miler",
                "100k",
                "100 miler",
            ],
            name="distance",
            label="Select Event",
            placeholder="Select Event",
            on_change=State.set_distance,
            value=State.distance_value,
            width="160px",
        ),
        rx.input(
            name="custom_distance",
            type="text",
            placeholder="or Enter Distance (mi)",
            min="0",
            on_change=State.set_custom_distance,
            value=State.distance,
            width="160px",
        ),
    )
