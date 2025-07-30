#!/usr/bin/env python3

import reflex as rx


def process_info() -> rx.Component:
    return rx.card(
        rx.heading(
            "Process Info",
            align="center",
            size="8",
        ),
        rx.divider(
            size="4",
        ),
    )
