#!/usr/bin/env python3

import reflex as rx


def gpu_info() -> rx.Component:
    return rx.card(
        rx.heading(
            "GPU Info",
            align="center",
            size="8",
        ),
        rx.divider(
            size="4",
        ),
        rx.vstack(
            rx.text(
                "GPU Vendor: ",
            ),
            rx.text(
                "GPU Model: ",
            ),
        ),
        rx.divider(
            size="4",
        ),
        rx.vstack(
            rx.text(
                "VRAM Used: ",
            ),
            rx.text(
                "VRAM Percent: ",
            ),
            rx.text(
                "GPU Temperature: ",
            ),
            rx.text(
                "Power Used: ",
            ),
            rx.text(
                "Fan Percent: ",
            )
        ),
        size="4",
    )
