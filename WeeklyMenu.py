import streamlit as st
import pandas as pd
from utils import init_session_state

init_session_state()
st.title("📅 今週の献立")

edited_menu = st.data_editor(st.session_state["weekly_menu"], num_rows="dynamic")

if st.button("✅ 履歴に追加する"):
    st.session_state["weekly_menu"] = edited_menu
    st.session_state["menu_history"] = pd.concat(
        [st.session_state["menu_history"], edited_menu],
        ignore_index=True
    )
    st.success("履歴に追加しました！")