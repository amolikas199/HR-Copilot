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
            background: #f9fafb;
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        }

        .login-wrapper {
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 20px;
        }

        .login-container {
            display: grid;
            grid-template-columns: 1fr 1fr;
            max-width: 900px;
            width: 100%;
            box-shadow: 0 10px 40px rgba(0, 0, 0, 0.08);
            border-radius: 12px;
            overflow: hidden;
            background: white;
        }

        .login-left {
            background: linear-gradient(135deg, #10b981 0%, #059669 100%);
            padding: 60px 40px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            color: white;
        }

        .login-logo {
            font-size: 48px;
            margin-bottom: 24px;
        }

        .login-title {
            font-size: 32px;
            font-weight: 700;
            margin-bottom: 12px;
            line-height: 1.2;
        }

        .login-subtitle {
            font-size: 15px;
            opacity: 0.9;
            line-height: 1.6;
        }

        .login-right {
            padding: 60px 40px;
            display: flex;
            flex-direction: column;
            justify-content: center;
        }

        .login-right h2 {
            font-size: 24px;
            margin-bottom: 32px;
            color: #111827;
        }

        .form-group {
            margin-bottom: 20px;
        }

        .form-label {
            display: block;
            font-size: 13px;
            font-weight: 600;
            color: #374151;
            margin-bottom: 8px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }

        .login-btn {
            background: #10b981;
            color: white;
            padding: 12px 16px;
            border-radius: 6px;
            border: none;
            font-weight: 600;
            cursor: pointer;
            font-size: 15px;
            margin-top: 24px;
            transition: all 0.3s ease;
        }

        .login-btn:hover {
            background: #059669;
        }

        .demo-note {
            font-size: 13px;
            color: #6b7280;
            margin-top: 20px;
            padding-top: 20px;
            border-top: 1px solid #e5e7eb;
        }

        .demo-note code {
            background: #f3f4f6;
            padding: 2px 6px;
            border-radius: 4px;
            color: #10b981;
            font-weight: 600;
        }

        @media (max-width: 768px) {
            .login-container {
                grid-template-columns: 1fr;
            }
            .login-left {
                padding: 40px 30px;
            }
        }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="login-wrapper">', unsafe_allow_html=True)
    st.markdown("""
    <div class="login-container">
        <div class="login-left">
            <div class="login-logo">🤖</div>
            <div class="login-title">HR Copilot</div>
            <div class="login-subtitle">Intelligent HR Assistant powered by AI. Get instant answers from your company's HR documents.</div>
        </div>
        <div class="login-right">
            <h2>Welcome back.</h2>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1])
    with col1:
        st.text_input("EMAIL", value=DEMO_USERNAME, key="username", label_visibility="collapsed")
    with col2:
        st.text_input("PASSWORD", value=DEMO_PASSWORD, type="password", key="password", label_visibility="collapsed")

    if st.button("Sign in", use_container_width=True, type="primary"):
        username = st.session_state.username
        password = st.session_state.password

        if username == DEMO_USERNAME and password == DEMO_PASSWORD:
            st.query_params["logged_in"] = "true"
            st.session_state.logged_in = True
            st.success("✓ Logged in!")
            st.rerun()
        else:
            st.error("❌ Invalid credentials")

    st.markdown("""
            <div class="demo-note">
                <strong>Demo:</strong> <code>hr_admin</code> / <code>demo123</code>
            </div>
        </div>
    </div>
    </div>
    """, unsafe_allow_html=True)
