"""
AI Text Translation & Summarization Assistant - Web UI
Run with: streamlit run app.py

Requirements:
    pip install streamlit groq
"""

import streamlit as st
from groq import Groq

# --------------------------------------------------
# Page Config
# --------------------------------------------------

st.set_page_config(
    page_title="AI Translation & Summarization Assistant",
    page_icon="🌐",
    layout="centered",
)

st.title("🌐 AI Text Translation & Summarization Assistant")
st.caption("Powered by Groq · Llama 3.1")

# --------------------------------------------------
# Sidebar - API Key
# --------------------------------------------------

with st.sidebar:
    st.header("⚙️ Settings")

    api_key = st.text_input(
        "Groq API Key",
        type="password",
        placeholder="gsk_...",
        help="Get a free key at console.groq.com",
    )

    st.divider()

    model = st.selectbox(
        "Model",
        options=[
            "openai/gpt-oss-20b",
            "openai/gpt-oss-120b",
            "meta-llama/llama-4-scout-17b-16e-instruct",
            "meta-llama/llama-4-maverick-17b-128e-instruct",
            "qwen/qwen3-32b",
            "groq/compound",
        ],
        index=0,
        help="llama-3.1-8b-instant and llama-3.3-70b-versatile are now "
        "enterprise-only/deprecated on Groq. These are the current public models.",
    )

    temperature = st.slider("Temperature", 0.0, 1.0, 0.3, 0.1)

    st.divider()
    st.markdown(
        "**Note:** Your API key is only used for this session and is "
        "never stored or sent anywhere except Groq's API."
    )

# --------------------------------------------------
# Main - Operation Choice
# --------------------------------------------------

operation = st.radio(
    "Choose Operation",
    options=["Translate", "Summarize"],
    horizontal=True,
)

target_language = None
if operation == "Translate":
    target_language = st.text_input("Target Language", placeholder="e.g. French, Spanish, Japanese")

text = st.text_area(
    "Enter / Paste your text",
    height=280,
    placeholder="Paste the text you want to translate or summarize here...",
)

run_button = st.button("🚀 Run", type="primary", use_container_width=True)

# --------------------------------------------------
# Prompt Builders
# --------------------------------------------------

def build_translation_prompt(language: str, text: str) -> str:
    return f"""You are a professional translator.

Translate the following text into {language}.

Requirements:

- Preserve formatting.
- Preserve names.
- Preserve technical terms where appropriate.
- Return only the translated text.

Text:

{text}
"""


def build_summary_prompt(text: str) -> str:
    return f"""You are an expert editor.

Summarize the following text.

Provide:

1. Summary
2. Five Key Points
3. Important Keywords
4. Target Audience
5. One-Sentence Summary

Write in simple English.

Text:

{text}
"""

# --------------------------------------------------
# Run Logic
# --------------------------------------------------

if run_button:
    if not api_key:
        st.error("Please enter your Groq API key in the sidebar.")
    elif operation == "Translate" and not target_language:
        st.error("Please enter a target language.")
    elif not text.strip():
        st.error("Please enter some text.")
    else:
        try:
            client = Groq(api_key=api_key)

            if operation == "Translate":
                prompt = build_translation_prompt(target_language, text)
                heading = f"🌍 Translation ({target_language})"
            else:
                prompt = build_summary_prompt(text)
                heading = "📝 Summary"

            with st.spinner("Calling Groq API..."):
                response = client.chat.completions.create(
                    model=model,
                    messages=[{"role": "user", "content": prompt}],
                    temperature=temperature,
                )

            result = response.choices[0].message.content

            st.divider()
            st.subheader(heading)
            st.markdown(result)

            st.download_button(
                "⬇️ Download Result",
                data=result,
                file_name="result.txt",
                mime="text/plain",
                use_container_width=True,
            )

        except Exception as e:
            if "model_not_found" in str(e) or "does not exist" in str(e):
                st.error(
                    f"The model `{model}` isn't available on your Groq account. "
                    "Try a different model from the sidebar, or check "
                    "console.groq.com/docs/models for the current list."
                )
            else:
                st.error(f"Something went wrong: {e}")

# --------------------------------------------------
# Footer
# --------------------------------------------------

st.divider()
st.caption("Built with Streamlit + Groq")