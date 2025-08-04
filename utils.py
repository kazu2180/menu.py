import pandas as pd
from datetime import datetime, timedelta

def init_session_state():
    if "weekly_menu" not in st.session_state:
        monday = datetime.today() - timedelta(days=datetime.today().weekday())
        dates = [(monday + timedelta(days=i)).strftime("%Y-%m-%d") for i in range(5)]
        st.session_state["weekly_menu"] = pd.DataFrame({
            "日付": dates,
            "主菜": [""] * 5,
            "副菜": [""] * 5,
            "ご飯もの": [""] * 5,
            "メモ": [""] * 5
        })

    if "menu_history" not in st.session_state:
        st.session_state["menu_history"] = pd.DataFrame(columns=["日付", "主菜", "副菜", "ご飯もの", "メモ"])

    if "favorites" not in st.session_state:
        st.session_state["favorites"] = pd.DataFrame(columns=["主菜", "副菜", "ご飯もの", "メモ"])