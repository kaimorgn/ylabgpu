#!/usr/bin/env python3

import reflex as rx
from ylabgpu.components.sidebar import sidebar
#from ylabgpu.components.accordion_ghost import accordion_ghost

from rxconfig import config


class State(rx.State):
    """The app state."""


def index() -> rx.Component:
    return rx.container(
        sidebar(),
    )


app = rx.App()
app.add_page(index)
