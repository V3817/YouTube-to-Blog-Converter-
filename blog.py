# Force newer SQLite version
__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

import streamlit as st
from crewai import Agent, Task, Crew, Process
from crewai_tools import YoutubeChannelSearchTool
from langchain_groq import ChatGroq
import os

# Streamlit UI Configuration
st.set_page_config(
    page_title="YouTube to Blog Converter",
    page_icon="📝",
    layout="centered"
)

def create_groq_llm(api_key, model_name):
    return ChatGroq(
        temperature=0.3,
        model_name=model_name,
        groq_api_key=api_key
    )

def main():
    st.title("🎥 YouTube to Blog Converter")
    st.markdown("### Transform YouTube Videos into Technical Blog Posts")
    
    with st.sidebar:
        st.header("API Configuration")
        groq_api_key = st.text_input(
            "Groq API Key",
            type="password",
            help="Get your API key from https://console.groq.com/keys"
        )
        
        st.header("Content Settings")
        channel_handle = st.text_input(
            "YouTube Channel Handle", 
            placeholder="@your-channel",
            help="Enter the YouTube channel ID starting with @"
        )
        topic = st.text_input(
            "Blog Topic",
            placeholder="Enter your blog topic"
        )
        groq_model = st.selectbox(
            "LLM Model",
            options=["llama3-70b-8192", "mixtral-8x7b-32768", "gemma-7b-it"],
            index=0
        )
        process_verbosity = st.select_slider(
            "Process Detail Level",
            options=[0, 1, 2],
            value=1
        )
        
    col1, col2 = st.columns([3, 1])
    
    with col1:
        if st.button("🚀 Generate Blog Post", use_container_width=True):
            if not groq_api_key:
                st.error("❌ Please enter your Groq API key!")
                return
            if not topic or not channel_handle:
                st.error("❌ Please fill in both topic and channel handle!")
                return
                
            with st.spinner("🔍 Analyzing YouTube content..."):
                try:
                    yt_tool = YoutubeChannelSearchTool(
                        youtube_channel_handle=channel_handle,
                        config={
                            'max_results': 3,
                            'transcription_depth': 'full'
                        }
                    )
                    
                    groq_llm = create_groq_llm(groq_api_key, groq_model)
                    
                    researcher = Agent(
                        role='Senior Technical Researcher',
                        goal=f'Extract key technical concepts from {channel_handle} videos',
                        backstory="Expert in technical content analysis and research.",
                        tools=[yt_tool],
                        llm=groq_llm,
                        verbose=True,
                        allow_delegation=False
                    )

                    writer = Agent(
                        role='Chief Technical Writer',
                        goal='Craft engaging technical blog content',
                        backstory="Technical writer specializing in clear documentation.",
                        tools=[yt_tool],
                        llm=groq_llm,
                        verbose=True
                    )

                    research_task = Task(
                        description=f"Analyze {channel_handle} videos about {topic}",
                        expected_output="Technical report with key concepts and comparisons",
                        agent=researcher
                    )

                    writing_task = Task(
                        description="Create blog post using research data",
                        expected_output="Well-structured technical blog in Markdown",
                        agent=writer,
                        output_file='generated_blog.md'
                    )

                    crew = Crew(
                        agents=[researcher, writer],
                        tasks=[research_task, writing_task],
                        process=Process.sequential,
                        verbose=process_verbosity
                    )

                    result = crew.kickoff(inputs={'topic': topic})

                    st.success("✅ Blog Generation Complete!")
                    st.subheader("Generated Content")
                    st.markdown(result)
                    
                    st.download_button(
                        label="📥 Download Markdown",
                        data=result,
                        file_name=f"{topic.replace(' ', '_')}_blog.md",
                        mime="text/markdown"
                    )

                except Exception as e:
                    st.error(f"🚨 Error generating blog: {str(e)}")

    with col2:
        st.markdown("""
        **How to Use:**
        1. Enter Groq API Key
        2. Set YouTube channel
        3. Specify blog topic
        4. Select LLM model
        5. Click Generate
        """)

if __name__ == "__main__":
    main()
