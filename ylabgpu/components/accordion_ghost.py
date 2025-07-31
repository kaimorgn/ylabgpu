#!/usr/bin/env python3

import reflex as rx
from ylabgpu.components.link_item import link_item


def accordion_ghost(header: str) -> rx.Component:
    '''
    '''
    return rx.accordion.root(
        rx.accordion.item(
            header=header,
            content=rx.vstack(
                link_item(
                    "casa",
                    "/#"
                ),
                link_item(
                    "junin",
                    "/#"
                ),
                link_item(
                    "ohrid",
                    "/#"
                ),
                link_item(
                    "puelo",
                    "/#"
                ),
                justify="start"
            ),
        ),
        type="multiple",
        collapsible=True,
        variant="ghost"
    )

