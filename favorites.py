import streamlit as st
import pandas as pd
from utils import init_session_state

init_session_state()
st.title("🌟 お気に入り献立")

# 表示
st.subheader("登録済みのお気に入り")
st.dataframe(st.session_state["favorites"], use_container_width=True)

# 追加フォーム
st.subheader("🍽️ 新しいお気に入りを追加")
with st.form("add_favorite"):
    main = st.text_input("主菜")
    side = st.text_input("副菜")
    rice = st.text_input("ご飯もの")
    memo = st.text_input("メモ")
    submitted = st.form_submit_button("追加する")
    if submitted:
        new_row = pd.DataFrame([{
            "主菜": main, "副菜": side, "ご飯もの": rice, "メモ": memo
        }])
        st.session_state["favorites"] = pd.concat(
            [st.session_state["favorites"], new_row], ignore_index=True
        )
        st.success("お気に入りに追加しました！")