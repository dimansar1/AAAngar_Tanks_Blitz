from streamlit_cookies_controller import CookieController
from typing import Optional

controller = CookieController()


def get_cookie(name: str) -> Optional[str]:
    try:
        return controller.get(name)
    except TypeError:
        return None


def set_cookie(name: str, value: str) -> None:
    controller.set(name, value)


def remove_cookie(name: str) -> None:
    try:
        controller.remove(name)
    except TypeError:
        pass
