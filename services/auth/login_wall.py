import streamlit as st

def render_login_wall():
    if st.session_state.get("user_id") is not None:
        return True
    st.title("🏋🏻AI-REALTIME-GYM-COACH")
    st.markdown("### Welcome...PLease enter the username to login.")

    with st.form("login form",clear_on_submit=False):
        username = st.text_input("Name(unique)",placeholder="eg : arslan2005")
        submit_button = st.form_submit_button("start session",width="stretch")

    if submit_button:
        if not username:
            st.error("fill user name!")
            return False
        st.session_state["username"] = username
        st.session_state["user_id"] = "1"

        st.rerun()

    return False
