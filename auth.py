import streamlit as st

DEMO_USERNAME = "hr_admin"
DEMO_PASSWORD = "demo123"

def check_login():
    if "logged_in" in st.query_params and st.query_params["logged_in"] == "true":
        return True
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
    return st.session_state.logged_in

def login_page():
    st.set_page_config(page_title="HR Copilot", layout="centered")

    st.markdown("""
    <style>
        * { margin: 0; padding: 0; }
        body {
            background: linear-gradient(135deg, #0f1419 0%, #1a1f2e 100%);
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
        }

        .login-wrapper {
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 20px;
        }

        .login-card {
            width: 100%;
            max-width: 420px;
            background: linear-gradient(135deg, #1a1f2e 0%, #16212b 100%);
            border: 2px solid #2d3748;
            border-radius: 16px;
            padding: 48px 32px;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.5);
        }

        .login-header {
            text-align: center;
            margin-bottom: 40px;
        }

        .login-logo {
            font-size: 56px;
            margin-bottom: 16px;
        }

        .login-title {
            font-size: 28px;
            font-weight: 700;
            background: linear-gradient(90deg, #60a5fa 0%, #818cf8 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 8px;
        }

        .login-subtitle {
            font-size: 14px;
            color: #94a3b8;
        }

        .form-group {
            margin-bottom: 16px;
        }

        .form-label {
            display: block;
            font-size: 13px;
            font-weight: 600;
            color: #cbd5e1;
            margin-bottom: 8px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }

        .credentials-box {
            background: rgba(96, 165, 250, 0.1);
            border: 1px solid #2d3748;
            border-radius: 8px;
            padding: 16px;
            margin-top: 32px;
            font-size: 13px;
            color: #cbd5e1;
        }

        .credentials-box code {
            background: rgba(0, 0, 0, 0.3);
            padding: 2px 6px;
            border-radius: 4px;
            color: #60a5fa;
            font-family: 'Monaco', 'Courier New', monospace;
        }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="login-wrapper">', unsafe_allow_html=True)
    st.markdown("""
    <div class="login-card">
        <div class="login-header">
            <div class="login-logo">🤖</div>
            <div class="login-title">HR Copilot</div>
            <div class="login-subtitle">Intelligent HR Assistant</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.text_input("Username", value=DEMO_USERNAME, key="username", disabled=False)
        st.text_input("Password", value=DEMO_PASSWORD, type="password", key="password", disabled=False)

        if st.button("🚀 Login", use_container_width=True, type="primary"):
            username = st.session_state.username
            password = st.session_state.password

            if username == DEMO_USERNAME and password == DEMO_PASSWORD:
                st.query_params["logged_in"] = "true"
                st.session_state.logged_in = True
                st.success("✓ Welcome back!")
                st.rerun()
            else:
                st.error("❌ Invalid credentials")

        st.markdown("""
        <div class="credentials-box">
            <strong>Demo Account:</strong><br>
            Username: <code>hr_admin</code><br>
            Password: <code>demo123</code>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)
