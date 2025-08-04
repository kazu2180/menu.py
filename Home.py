import streamlit as st
import datetime

st.set_page_config(page_title="献立管理", layout="wide")

# サイドバーでページ選択
page = st.sidebar.radio("ページを選択", ["📅 カレンダー", "📜 履歴", "⭐ お気に入り"])

# セッションステート初期化
if "meal_data" not in st.session_state:
    st.session_state.meal_data = {}
if "favorites" not in st.session_state:
    st.session_state.favorites = []

# 📅 カレンダーページ
if page == "📅 カレンダー":
    st.title("今週の献立を登録")
    today = datetime.date.today()
    for i in range(7):
        date = today + datetime.timedelta(days=i)
        key = str(date)
        meal = st.text_input(f"{date.strftime('%Y-%m-%d')} の献立", value=st.session_state.meal_data.get(key, ""), key=key)
        st.session_state.meal_data[key] = meal

        # お気に入りに追加ボタン
        if meal and st.button(f"⭐ お気に入りに追加 ({date})", key=f"fav_{key}"):
            if meal not in st.session_state.favorites:
                st.session_state.favorites.append(meal)
                st.success(f"{meal} をお気に入りに追加しました！")

# 📜 履歴ページ
elif page == "📜 履歴":
    st.title("献立履歴")
    if st.session_state.meal_data:
        for date, meal in sorted(st.session_state.meal_data.items()):
            st.write(f"📅 {date}: 🍽️ {meal}")
    else:
        st.info("まだ献立が登録されていません。")

# ⭐ お気に入りページ
elif page == "⭐ お気に入り":
    st.title("お気に入りメニュー一覧")
    if st.session_state.favorites:
        for i, meal in enumerate(st.session_state.favorites):
            st.write(f"{i+1}. {meal}")
    else:
        st.info("お気に入りメニューはまだありません。")

    # お気に入りの削除
    remove_meal = st.selectbox("削除するメニューを選択", [""] + st.session_state.favorites)
    if remove_meal and st.button("❌ 削除"):
        st.session_state.favorites.remove(remove_meal)
        st.success(f"{remove_meal} をお気に入りから削除しました！")