#!/usr/bin/env python3

import reflex as rx


def cpu_info() -> rx.Component:
    return rx.card(
        rx.heading(
            "CPU Info",
            align="center",
            size="8"
        ),
        rx.divider(
            size="4"
        ),
        rx.vstack(
            rx.text(
                "CPU Vendor: ",
            ),
            rx.text(
                "CPU Model:",
            ),
            rx.text(
                "RAM Vendor: ",
            ),
            rx.text(
                "RAM Model: ",
            ),
            rx.text(
                "HDD Vendor: ",
            ),
            rx.text(
                "HDD Model: ",
            ),
        ),
        rx.divider(
            size="4"
        ),
        rx.vstack(
            rx.text(
                "CPU Core Percent: ",
            ),
            rx.text(
                "RAM Used: ",
            ),
            rx.text(
                "RAM Percent: ",
            ),
            rx.text(
                "HDD Used: ",
            ),
            rx.text(
                "HDD Percent: ",
            ),
        ),
        size="4"
    )
