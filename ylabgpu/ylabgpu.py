#!/usr/bin/env python3

import reflex as rx

from ylabgpu.components.cpu_info import cpu_info
from ylabgpu.components.gpu_info import gpu_info
from ylabgpu.components.process_info import process_info
from rxconfig import config


def index() -> rx.Component:
    return rx.container(
        rx.hstack(
            cpu_info(),
            gpu_info(),
            process_info(),
        )
    )


app = rx.App()
app.add_page(index)
