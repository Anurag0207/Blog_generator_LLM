import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_community.llms import CTransformers
import os

os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"

def generate_blog(input_text, word_count, audience_type):
    model_path = 'TheBloke/Llama-2-7B-Chat-GGML'
    model_file = 'llama-2-7b-chat.ggmlv3.q8_0.bin'

    llm = CTransformers(
        model=model_path,
        model_type='llama',
        model_file=model_file,
        config={'max_new_tokens': 256, 'temperature': 0.01}
    )
    
    prompt_template = """
    Write a blog post about {input_text} tailored for {audience_type}. Make sure the content, language, and depth of information are suitable for {audience_type}. Limit the blog to around {word_count} words.
    """
    
    prompt = PromptTemplate(input_variables=["audience_type", "input_text", "word_count"], template=prompt_template)
    
    response = llm(prompt.format(audience_type=audience_type, input_text=input_text, word_count=word_count))
    return response

st.set_page_config(page_title="Blog Generator", page_icon='✍️', layout='centered', initial_sidebar_state='collapsed')
st.header("Blog Generator ✍️")

blog_topic = st.text_input("Enter the Blog Topic")

col1, col2 = st.columns([5, 5])

with col1:
    word_count = st.text_input('Number of Words')
with col2:
    audience_type = st.selectbox('Target Audience', ('Researchers', 'Critics', 'Amateurs'), index=0)

if st.button("Generate"):
    blog_response = generate_blog(blog_topic, word_count, audience_type)
    st.write(blog_response)
