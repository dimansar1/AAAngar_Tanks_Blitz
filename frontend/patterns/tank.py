import requests
import streamlit as st

def render_tank_card(tank: dict) -> None:
    tank_id = tank["id"]

    with st.container(border=True):
        if tank.get("photo_path") != '-':
            st.image(tank["photo_path"], use_container_width=True)
        else:
            st.info("Изображение не добавлено")

        st.subheader(tank["title"])

        if st.button("Подробнее", key=f"card_details_{tank_id}"):
            st.session_state["selected_tank_id"] = tank
            st.switch_page("pages/tank.py")
            