#!/usr/bin/env python3

import reflex as rx


def link_item(text:str, href: str) -> rx.Component:
    '''
    [概要]
    
    Args:
        text: 
        href:

    Rerurn:
        
    '''
    return rx.link(
        rx.hstack(
            rx.text(
                text,
                size="4",
            ),
            width="100%",
            padding_x="0.5rem",
            padding_y="0.75rem",
            align="center",
            style={
                "_hover": {
                    "bg": rx.color(
                        "accent",
                        4
                    ),
                    "color": rx.color(
                        "accent",
                        11
                    ),
                },
                "border-radius": "0.5em",
            },
        ),
        href=href,
        underline="none",
        weight="medium",
        width="100%",
    )
