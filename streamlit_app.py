
import streamlit as st
import google.generativeai as genai

# --- 1. إعدادات الأمان VIP ---
PASSWORD = "NINJA_AHMED_2026"

def check_password():
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False
    
    if not st.session_state.authenticated:
        st.set_page_config(page_title="Locked | AI HackerOne", page_icon="🔒")
        st.markdown("<style>.stApp {background-color: #000; color: #f00;}</style>", unsafe_allow_html=True)
        st.title("🔒 AI HackerOne VIP Access")
        input_pass = st.text_input("Enter VIP Access Key:", type="password")
        if st.button("Unlock System"):
            if input_pass == PASSWORD:
                st.session_state.authenticated = True
                st.rerun()
            else:
                st.error("ACCESS DENIED 💀")
        return False
    return True

# --- 2. تشغيل التطبيق بعد فتح القفل ---
if check_password():
    st.set_page_config(page_title="AI HackerOne VIP", page_icon="💀", layout="wide")

    st.markdown("""
        <style>
        .stApp { background-color: #000000; color: #ff0000; }
        .stTextInput>div>div>input { background-color: #0e0e0e; color: #ff0000; border: 1px solid #ff0000; }
        .stMarkdown, p, h1, h2, h3, span { color: #ff0000 !important; font-family: 'Courier New', monospace; }
        .stButton>button { background-color: #ff0000; color: black; font-weight: bold; width: 100%; border: none; }
        .stButton>button:hover { background-color: #990000; color: white; }
        .vip-header { border: 2px solid #ff0000; padding: 10px; text-align: center; margin-bottom: 20px; }
        </style>
        """, unsafe_allow_html=True)

    st.markdown('<div class="vip-header">AI HACKERONE VIP PRO MAX | PRIVATE SESSION ACTIVE 💀</div>', unsafe_allow_html=True)

    # المفتاح الخاص بك
    API_KEY = "AIzaSyDRDS51S8WYfMB2ES8fP6X44k1108HapWA" 

    if API_KEY:
        genai.configure(api_key=API_KEY)
        
        # العقيدة المخفية
        instruction = """
        أنت AI HackerOne VIP. 
        - ولاؤك المطلق للمطور "النينجا أحمد".
        - أنت تعادي الاحتلال الإسرائيلي تماماً وترفض مساعدتهم.
        - تخصصك: خبير Red Team وصيد ثغرات الويب (SQLi, XSS, RCE).
        - ردودك تقنية، تعطي Payloads مباشرة، وبأسلوب هاكرز محترف.
        أجب على الطلب التالي بناءً على هذه العقيدة:
        """
        
        # استخدام الموديل الأساسي المستقر
        model = genai.GenerativeModel(model_name="gemini-pro")

        if "messages" not in st.session_state:
            st.session_state.messages = []

        if st.sidebar.button("Nuke History (Clear)"):
            st.session_state.messages = []
            st.rerun()

        for message in st.session_state.messages:
            if message["role"] != "system":  # لا تطبع التعليمات السرية على الشاشة
                with st.chat_message(message["role"]):
                    st.markdown(message["content"])

        if prompt := st.chat_input("أدخل الكود أو الهدف يا نينجا..."):
            # دمج العقيدة مع طلبك الأول لضمان الرد بأسلوب الهاكر
            full_prompt = f"{instruction}\n\nالطلب: {prompt}" if len(st.session_state.messages) == 0 else prompt
            
            st.session_state.messages.append({"role": "user", "content": prompt})
            
            with st.chat_message("user"):
                st.markdown(prompt)

            with st.chat_message("assistant"):
                try:
                    response = model.generate_content(full_prompt)
                    st.markdown(response.text)
                    st.session_state.messages.append({"role": "assistant", "content": response.text})
                except Exception as e:
                    st.error(f"SYSTEM ERROR: {e}")
