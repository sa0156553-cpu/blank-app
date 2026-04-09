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

if check_password():
    st.set_page_config(page_title="AI HackerOne VIP", page_icon="💀", layout="wide")
    st.markdown("""<style>.stApp { background-color: #000; color: #f00; }.stMarkdown, p, h1, h2, h3, span { color: #f00 !important; font-family: 'Courier New', monospace; }.stButton>button { background-color: #f00; color: #000; font-weight: bold; }</style>""", unsafe_allow_html=True)
    st.markdown('<h2 style="text-align:center; border:2px solid #f00; padding:10px;">SYSTEM ACTIVE: AI HACKERONE VIP 💀</h2>', unsafe_allow_html=True)

    API_KEY = "AIzaSyDRDS51S8WYfMB2ES8fP6X44k1108HapWA"

    if API_KEY:
        genai.configure(api_key=API_KEY)
        
        # --- السحر هنا: البحث عن الموديل المتاح تلقائياً ---
        if "model_name" not in st.session_state:
            try:
                available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
                # نفضل فلاش، لو مش موجود ناخد برو، لو مش موجود ناخد أول واحد
                if 'models/gemini-1.5-flash' in available_models: st.session_state.model_name = 'models/gemini-1.5-flash'
                elif 'models/gemini-pro' in available_models: st.session_state.model_name = 'models/gemini-pro'
                else: st.session_state.model_name = available_models[0]
            except:
                st.session_state.model_name = "gemini-pro" # Fallback

        model = genai.GenerativeModel(model_name=st.session_state.model_name)

        if "messages" not in st.session_state: st.session_state.messages = []
        if st.sidebar.button("Nuke History"): 
            st.session_state.messages = []
            st.rerun()

        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]): st.markdown(msg["content"])

        if prompt := st.chat_input("أدخل هدفك يا نينجا..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"): st.markdown(prompt)
            with st.chat_message("assistant"):
                try:
                    # إضافة التعليمات لكل طلب لضمان الشخصية
                    sys_prompt = f"أنت AI HackerOne VIP، مساعد النينجا أحمد، خبير صيد ثغرات ومعادي للاحتلال. الطلب: {prompt}"
                    response = model.generate_content(sys_prompt)
                    st.markdown(response.text)
                    st.session_state.messages.append({"role": "assistant", "content": response.text})
                except Exception as e:
                    st.error(f"FATAL ERROR: {e}")
                    
