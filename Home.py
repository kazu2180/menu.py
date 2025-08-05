import streamlit as st
import datetime

st.set_page_config(page_title="献立カレンダー", layout="wide")

# ページ選択
page = st.sidebar.radio("ページを選択", ["📅 カレンダー", "📜 履歴", "⭐ お気に入り"])

# セッションステート初期化
if "meal_data" not in st.session_state:
    st.session_state.meal_data = {}
if "favorites" not in st.session_state:
    st.session_state.favorites = []

# 📅 カレンダーページ
if page == "📅 カレンダー":
    st.title("🍱 今週の献立（平日のみ）")
    st.markdown("""
    <div style="background-color:#f0f8ff; padding:10px; border-radius:10px">
    <h4>🔗 おすすめレシピサイト</h4>
    <ul>
        <li><a href="https://cookpad.com/jp/search/%E3%81%8A%E5%BC%81%E5%BD%93" target="_blank">クックパッド 🍚</a></li>
        <li><a href="https://www.ebarafoods.com/recipe/cla_menu/35/" target="_blank">エバラ食品 🍳</a></li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

    today = datetime.date.today()
    weekday_dates = []
    delta = datetime.timedelta(days=1)
    current = today

    # 平日5日分取得
    while len(weekday_dates) < 5:
        if current.weekday() < 5:
            weekday_dates.append(current)
        current += delta

    for date in weekday_dates:
        key = str(date)
        st.markdown(f"### 📅 {date.strftime('%Y-%m-%d (%a)')}")
        with st.container():
            col1, col2 = st.columns([1, 1])
            with col1:
                main_dish = st.text_input("🥘 主菜", value=st.session_state.meal_data.get(key, {}).get("main", ""), key=f"main_{key}")
            with col2:
                side_dish = st.text_input("🥗 副菜", value=st.session_state.meal_data.get(key, {}).get("side", ""), key=f"side_{key}")
            notes = st.text_area("📝 備考", value=st.session_state.meal_data.get(key, {}).get("notes", ""), key=f"notes_{key}")

            # 保存
            st.session_state.meal_data[key] = {
                "main": main_dish,
                "side": side_dish,
                "notes": notes
            }

            # お気に入り追加
            if main_dish and st.button(f"⭐ 主菜をお気に入りに追加 ({date})", key=f"fav_main_{key}"):
                if main_dish not in st.session_state.favorites:
                    st.session_state.favorites.append(main_dish)
                    st.success(f"{main_dish} をお気に入りに追加しました！")

# 📜 履歴ページ
elif page == "📜 履歴":
    st.title("📜 献立履歴")
    if st.session_state.meal_data:
        for date, data in sorted(st.session_state.meal_data.items()):
            st.markdown(f"#### 📅 {date}")
            st.write(f"🥘 主菜: {data.get('main', '')}")
            st.write(f"🥗 副菜: {data.get('side', '')}")
            st.write(f"📝 備考: {data.get('notes', '')}")
            st.markdown("---")
    else:
        st.info("まだ献立が登録されていません。")

# ⭐ お気に入りページ
elif page == "⭐ お気に入り":
    st.title("⭐ お気に入りメニュー")
    if st.session_state.favorites:
        for i, meal in enumerate(st.session_state.favorites):
            st.write(f"{i+1}. {meal}")
    else:
        st.info("お気に入りメニューはまだありません。")

    # 削除機能
    remove_meal = st.selectbox("❌ 削除するメニューを選択", [""] + st.session_state.favorites)
    if remove_meal and st.button("削除"):
        st.session_state.favorites.remove(remove_meal)
        st.success(f"{remove_meal} をお気に入りから削除しました！")