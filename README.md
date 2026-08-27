# YouTube to Blog Converter

## Overview
The YouTube to Blog Converter is a Streamlit-based application designed to transform YouTube videos into well-structured technical blog posts. The project leverages advanced AI/ML models from Groq to extract key technical concepts from YouTube content and automatically craft engaging and informative blog posts.

## Features
- **YouTube Video Analysis:** Extract technical concepts and insights from YouTube channel videos.
- **AI-Powered Blog Generation:** Use advanced Groq models to generate comprehensive technical blog posts.
- **Customizable Settings:** Configure API keys, YouTube channels, blog topics, and LLM models.
- **Download Blog Post:** Export the generated blog in Markdown format.

## Requirements
- Python 3.8 or higher
- Streamlit
- crewai
- crewai_tools
- langchain_groq

## Installation
1. Clone this repository:
    ```bash
    git clone <repository-url>
    cd <project-directory>
    ```

2. Install required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the Streamlit app:
    ```bash
    streamlit run blog.py
    ```

## How to Use
1. Open the app in your browser (default: http://localhost:8501).
2. Enter the required inputs in the sidebar:
    - **Groq API Key:** Obtain your API key from [Groq](https://console.groq.com/keys).
    - **YouTube Channel Handle:** Enter the channel handle (e.g., `@channel_handle`).
    - **Blog Topic:** Provide the topic for the blog post.
    - **LLM Model:** Select one of the available Groq models.
    - **Process Detail Level:** Adjust verbosity for process execution.

3. Click on the **Generate Blog Post** button.
4. View and download the generated blog post in Markdown format.

## Application Flow
1. **YouTube Content Analysis:**
   - The `YoutubeChannelSearchTool` searches and extracts information from videos of the provided channel.

2. **Groq LLM Integration:**
   - Customizable Groq LLM models are used to analyze content and generate a comprehensive blog.

3. **Task Execution:**
   - Research and writing tasks are executed using Crew agents.

4. **Blog Generation:**
   - The final content is displayed in Markdown format and can be downloaded.

## Example Usage
1. Enter `@channel_handle` as the YouTube channel handle.
2. Set the topic as "AI vs ML vs DL vs Data Science."
3. Choose `llama3-70b-8192` as the LLM model.
4. Generate the blog and download it.

## Troubleshooting
### Error: "Please enter your Groq API key!"
- Ensure that a valid Groq API key is provided.

### Error: "Please fill in both topic and channel handle!"
- Make sure the YouTube channel handle and blog topic are not empty.

### Error: "🚨 Error generating blog: ..."
- Check internet connectivity and API configuration.
- Verify that the provided YouTube channel handle is correct.

## Contributing
Contributions are welcome! Please submit a pull request for any improvements or suggestions.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contact
For any issues or questions, please contact the project maintainer.

