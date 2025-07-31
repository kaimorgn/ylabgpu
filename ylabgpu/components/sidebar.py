#!/usr/bin/env python3

import reflex as rx
from ylabgpu.components.sidebar_items import sidebar_items


def sidebar() -> rx.Component:
    '''
    '''
    return rx.box(
        rx.desktop_only(
            rx.vstack(
                rx.hstack(
                    rx.heading(
                        "Ylab App",
                        size="7",
                        weight="bold",
                    ),
                    rx.color_mode.button(
                        position="right"
                    ),
                    align="center",
                    justify="start",
                    padding_x="0.5rem",
                    width="100%",
                ),
                sidebar_items(),
                spacing="5",
                position="fixed",
                left="0px",
                top="0px",
                z_index="5",
                padding_x="0",
                padding_y="1.5em",
                bg=rx.color(
                    "accent",
                    3
                ),
                align="start",
                height="100vh",
                width="11em",
            ),
        ),
        rx.mobile_and_tablet(
            rx.drawer.root(
                rx.drawer.trigger(
                    rx.icon(
                        "align-justify",
                        size=30
                    )
                ),
                rx.drawer.overlay(
                    z_index="5"
                ),
                rx.drawer.portal(
                    rx.drawer.content(
                        rx.vstack(
                            rx.box(
                                rx.drawer.close(
                                    rx.icon(
                                        "x",
                                        size=30
                                    ),
                                    width="100%",
                                ),
                                sidebar_items(),
                                spacing="5",
                                width="100%",
                            ),
                            top="auto",
                            right="auto",
                            height="100%",
                            width="20em",
                            padding="1.5em",
                            bg=rx.color(
                                "accent",
                                2
                            ),
                        ),
                        width="100%",
                    ),
                    direction="left",
                ),
                padding="1em",
            ),
        )
    )

