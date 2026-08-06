import streamlit as st

DEMO_USERNAME = "hr_admin"
DEMO_PASSWORD = "demo123"

def check_login():
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
    return st.session_state.logged_in

def login_page():
    st.set_page_config(page_title="HR Copilot", layout="centered")

    st.markdown("""
    <style>
        body { background: #0f1419; }
        .login-container {
            max-width: 400px;
            margin: 80px auto;
            padding: 40px;
            background: linear-gradient(135deg, #1a1f2e 0%, #16212b 100%);
            border-radius: 12px;
            border: 1px solid #2d3748;
        }
        .login-title {
            text-align: center;
            color: #60a5fa;
            font-size: 32px;
            margin-bottom: 10px;
            font-weight: bold;
        }
        .login-subtitle {
            text-align: center;
            color: #94a3b8;
            margin-bottom: 30px;
            font-size: 14px;
        }
    </style>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown('<div class="login-title">🤖 HR Copilot</div>', unsafe_allow_html=True)
        st.markdown('<div class="login-subtitle">Intelligent HR Assistant</div>', unsafe_allow_html=True)

        st.divider()

        username = st.text_input("Username", placeholder=DEMO_USERNAME)
        password = st.text_input("Password", type="password", placeholder="••••••")

        if st.button("Login", use_container_width=True):
            if username == DEMO_USERNAME and password == DEMO_PASSWORD:
                st.session_state.logged_in = True
                st.success("✓ Logged in successfully!")
                st.rerun()
            else:
                st.error("❌ Invalid credentials. Try: hr_admin / demo123")

        st.markdown("""
        ---
        **Demo Credentials:**
        Username: `hr_admin`
        Password: `demo123`
        """)
