import reflex as rx
from typing import Dict, List

from rxconfig import config


class State(rx.State):
    """The app state."""

    cols: Dict[str, List[str]] = {
        "To-Do": ["Card 1", "Card 2"],
        "In Progress": ["Card 1", "Card 2"],
        "Done": ["Card 1", "Card 2"],
    }

    @staticmethod
    def render_cols(col_name: str) -> rx.Component:
        return rx.vstack(
            rx.card(
                rx.heading(col_name, align="center"),
                width="300px",
            ),
            rx.card(
                rx.foreach(State.cols[col_name], State.render_cards),
                size="4",
                width="300px",
                height="500px"
            )
        )

    @staticmethod
    def render_cards(card_name: str) -> rx.Component:
        return rx.card(
            rx.heading(card_name, align="center", justify="center"),
            size="3",
            height="100px"
        )


def index() -> rx.Component:
    return rx.container(
       rx.vstack(
        rx.heading("Kanban Board"),
        rx.flex(
            rx.scroll_area(
                rx.hstack(
                    rx.foreach(State.cols.keys(), State.render_cols),
                    scrollbars="horizontal",
                    justify="center",
                    align="center"
                )
            ),
            rx.button(
                rx.heading("+"),
                width="60px",
                height="60px",
                background_color="GREEN",
                align="bottom_left"
            )
        )
       )
    )


app = rx.App()
app.add_page(index)
