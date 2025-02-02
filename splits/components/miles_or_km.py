import reflex as rx


def miles_or_km() -> rx.Component:
    return rx.hstack(rx.text("miles"), rx.switch(), rx.text("kilometers"))
