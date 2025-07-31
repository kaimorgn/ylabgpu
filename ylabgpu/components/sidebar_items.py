#!/usr/bin/env python3

import reflex as rx
from ylabgpu.components.link_item import link_item
from ylabgpu.components.accordion_ghost import accordion_ghost


def sidebar_items() -> rx.Component:
    '''
    '''
    return rx.vstack(
        link_item(
            "Home",
            "/#"
        ),
        accordion_ghost(
                "Machine Monitor"
        ),
        align="center",
        spacing="1",
        width="100%",
    )

