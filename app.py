"""A small Drafter counter for Final Project Practice."""

from dataclasses import dataclass

from drafter import (
    Button, Header, Page, assert_has, assert_state, hide_debug_information,
    route, set_site_information, set_website_framed, set_website_title, start_server,
)


set_website_title("Kamal's Counter")
set_site_information(
    author="Kamal Mandava",
    description="A counter with increment, decrement, and reset buttons.",
    sources="Adapted from Drafter's Build your first app tutorial.",
    planning="Store an integer in state and use three routes to increment, decrement, and reset it.",
    links=["https://drafter-edu.github.io/drafter/start/first-app/"],
)
hide_debug_information()
set_website_framed(False)


@dataclass
class State:
    count: int


@route
def index(state: State) -> Page:
    """Show the current count and the three counter controls."""
    return Page(state, [
        Header("Counter"),
        "Current count: " + str(state.count) + "\n",
        Button("+1", "increment"),
        Button("-1", "decrement"),
        Button("Reset", "reset_count"),
    ])


@route
def increment(state: State) -> Page:
    """Increase the count by one and show the updated counter."""
    state.count = state.count + 1
    return index(state)


@route
def decrement(state: State) -> Page:
    """Decrease the count by one and show the updated counter."""
    state.count = state.count - 1
    return index(state)


@route
def reset_count(state: State) -> Page:
    """Reset the count to zero and show the updated counter."""
    state.count = 0
    return index(state)


assert_state(increment(State(0)), State(1))
assert_state(decrement(State(0)), State(-1))
assert_state(reset_count(State(7)), State(0))
assert_has(index(State(3)), "Current count: 3")

start_server(State(0))
