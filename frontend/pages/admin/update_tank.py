import requests
import streamlit as st

from patterns.header import header
from api.client import get_error_message, update_tank

header()
tank_id = st.session_state.get('selected_tank_id')
st.title('Добавление танка')

with st.form("create_tank_form"):
    title = st.text_input("Название танка", key="title")
    photo_path = st.text_input("Фото танка", key="photo_path", value='-')
    health = st.text_input("Здоровье танка", key="health", value='-')
    damage = st.text_input("Урон танка", key="damage", value='-')
    armor = st.text_input("Бронирование танка", key="armor", value='-')
    history = st.text_input("Историческая справка о танке", key="history", value='Историческая справка о данном танке отсутствует')
    recommendation = st.text_input("Рекомендация по игре на танке", key="recommendation", value='Рекомендации по игре на данном танке отсутстуют')
    category = st.text_input("Тип танка", key="category")
    nation = st.text_input("Нация танка", key="nation")
    level = st.text_input("Уровень танка", key="level")

    submitted = st.form_submit_button("Изменить танк")

if submitted:
    if not title.strip() or not category.strip() or not nation.strip() or not level.strip():
        st.error("Заполните обязательно поля: Название танка, Тип танка, Нация танка, Уровень танка.")
        st.stop()

    try:
        response = update_tank(
            tank_id = tank_id,
            title = title.strip(),
            photo_path = photo_path.strip(),
            health = health.strip(),
            damage = damage.strip(),
            armor = armor.strip(),
            history = history.strip(),
            recommendation = recommendation.strip(),
            category = category.strip(),
            nation = nation.strip(),
            level = level.strip(),
        )
    except requests.RequestException:
        st.error("Backend недоступен. Проверьте, запущен ли FastAPI.")
        st.stop()

    if response.status_code in (200, 201):
        st.success("Танк успешно добавлен")
        st.switch_page("pages/tanks.py")
    else:
        st.error(get_error_message(response))


