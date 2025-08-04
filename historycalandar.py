import streamlit as st
import pandas as pd
from utils import init_session_state

init_session_state()
st.title("📜 献立履歴 & カレンダー")

# 月選択
months = sorted(set(pd.to_datetime(st.session_state["menu_history"]["日付"]).dt.strftime("%Y-%m")))
selected_month = st.selectbox("表示する月を選択", months)

# フィルター表示
filtered = st.session_state["menu_history"][
    pd.to_datetime(st.session_state["menu_history"]["日付"]).dt.strftime("%Y-%m") == selected_month
]

st.write(f"📆 {selected_month} の献立")
st.dataframe(filtered, use_container_width=True)