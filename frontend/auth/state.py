import streamlit as st
from typing import Optional

from patterns.cookie import get_cookie, remove_cookie, set_cookie

def save_auth(access_token: Optional[str], profile: dict) -> None:
    if access_token:
        set_cookie("access_token", access_token)
    st.session_state["profile"] = profile


def clear_auth() -> None:
    remove_cookie("access_token")
    st.session_state.pop("profile", None)


def is_authenticated() -> bool:
    return bool(get_cookie("access_token"))


def current_profile() -> Optional[dict]:
    return st.session_state.get("profile")


def is_admin() -> bool:
    profile = current_profile()
    return bool(profile and profile.get("role") == "admin")


def require_login() -> None:
    if is_authenticated():
        return

    st.warning("Сначала войдите в аккаунт.")
    if st.button("Перейти ко входу", key="require_login_button"):
        st.switch_page("pages/login.py")
    st.stop()


def require_admin() -> None:
    require_login()

    if not is_admin():
        st.error("Эта страница доступна только администратору.")
        st.stop()
