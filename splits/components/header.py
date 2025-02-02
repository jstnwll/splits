import reflex as rx


def header() -> rx.Component:
    return rx.box(
        rx.heading("s p l i t s", as_="h1", size="9", color_scheme="teal"),
        rx.text(
            "running calculator",
            as_="p",
            size="6",
            color_scheme="teal",
        ),
        text_align="center",
    )
