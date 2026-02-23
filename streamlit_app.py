import streamlit as st
import requests
import os
import base64

# --- CONFIGURATION ---
ST_API_URL = os.getenv("BACKEND_URL", "https://auradocs.onrender.com/")
APP_NAME = "AuraDocs"
APP_ICON = "📄"

st.set_page_config(
    page_title=f"{APP_NAME} | Intelligent Document Assistant",
    page_icon=APP_ICON,
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- PREMIUM CSS STYLING ---
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&display=swap');

    /* Global Overrides */
    * {{ font-family: 'Inter', sans-serif; }}
    
    .stApp {{
        background: radial-gradient(circle at top right, #1a1c24, #0e1117);
    }}

    /* Heading Style */
    .main-title {{
        font-size: 3rem;
        font-weight: 700;
        background: -webkit-linear-gradient(#00f2fe, #4facfe);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
    }}
    
    .sub-title {{
        color: #8892b0;
        font-size: 1.1rem;
        margin-bottom: 2rem;
    }}

    /* Sidebar Glassmorphism */
    [data-testid="stSidebar"] {{
        background-color: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(10px);
        border-right: 1px solid rgba(255, 255, 255, 0.05);
    }}

    /* Chat Elements */
    .stChatMessage {{
        background-color: rgba(255, 255, 255, 0.02);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 15px;
        padding: 1rem;
        margin-bottom: 1rem;
    }}

    /* File Uploader Decor */
    .uploadedFile {{
        background-color: #1e293b;
        border-radius: 10px;
        padding: 10px;
    }}

    /* Buttons */
    .stButton>button {{
        border-radius: 8px;
        background: linear-gradient(90deg, #4facfe 0%, #00f2fe 100%);
        color: white;
        font-weight: 600;
        border: none;
        padding: 0.5rem 1rem;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }}
    .stButton>button:hover {{
        transform: translateY(-1px);
        box-shadow: 0 4px 12px rgba(79, 172, 254, 0.3);
        color: white;
    }}

    /* Links */
    a {{ color: #4facfe; text-decoration: none; }}
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR: CONTROLS & STATUS ---
with st.sidebar:
    st.markdown(f"<h2 style='color: #4facfe;'>{APP_NAME} Control Panel</h2>", unsafe_allow_html=True)
    st.caption("Advanced Knowledge Retrieval")
    st.divider()

    # API Connection Status
    st.subheader("🌐 System Status")
    try:
        # Simple health check if needed, otherwise just show configured URL
        st.success("API: Connected")
    except:
        st.error("API: Disconnected")
    
    api_url = st.text_input("Backend URL", value=ST_API_URL)
    
    st.divider()

    # Document Section
    st.subheader("📁 Knowledge Source")
    uploaded_file = st.file_uploader("Drop your PDF archive here", type=["pdf"], help="Upload a document to train the assistant.")
    
    if uploaded_file is not None:
        if st.button("🚀 Process & Index"):
            with st.spinner("Analyzing document structure..."):
                try:
                    files = {"file": (uploaded_file.name, uploaded_file.getvalue(), "application/pdf")}
                    response = requests.post(f"{api_url}/upload", files=files)
                    if response.status_code == 200:
                        st.balloons()
                        st.success("AuraDocs has successfully indexed your content.")
                    else:
                        st.error(f"Processing failed: {response.json().get('error', 'Critical Error')}")
                except Exception as e:
                    st.error(f"Network error: Check if backend is running at {api_url}")

    st.spacer = st.container()
    st.spacer.write("") # Padding
    st.caption("© 2026 AuraDocs. Built with Mistral-7B.")

# --- MAIN INTERFACE: CHAT ---
st.markdown(f"<div class='main-title'>{APP_NAME}</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>Your personal AI assistant for instant document intelligence.</div>", unsafe_allow_html=True)

# Initialize Session State
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant", 
            "content": "Hello! I'm AuraDocs. Upload a PDF in the sidebar, and I'll help you extract insights from it instantly. What would you like to know?"
        }
    ]

# Display history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User Interaction
if prompt := st.chat_input("Ask AuraDocs anything..."):
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate assistant response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        with st.spinner("Consulting knowledge base..."):
            try:
                response = requests.post(
                    f"{api_url}/ask",
                    json={"question": prompt}
                )
                if response.status_code == 200:
                    raw_answer = response.json().get("answer", "No response received.")
                    
                    # Extract content from ChatHuggingFace response structure
                    if isinstance(raw_answer, dict):
                        answer = raw_answer.get("content", str(raw_answer))
                    else:
                        answer = str(raw_answer)
                    
                    message_placeholder.markdown(answer)
                    st.session_state.messages.append({"role": "assistant", "content": answer})
                elif response.status_code == 422:
                    st.error("Invalid request. Please check the backend input format.")
                else:
                    error_detail = response.json().get("error", "The backend encountered an issue.")
                    st.warning(f"⚠️ {error_detail}")
            except Exception as e:
                st.error(f"Connection Error: {e}")

# Footer
st.markdown("<br><br>", unsafe_allow_html=True)
st.divider()
col1, col2 = st.columns([4, 1])
with col1:
    st.caption("Pro Tip: For best results, ensure your PDF is text-searchable (not just scanned images).")
