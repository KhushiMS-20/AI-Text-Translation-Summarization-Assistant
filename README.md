# AI-Text-Translation-Summarization-Assistant
1. Problem Statement
   - Difficulty in translating between multiple languages
   - Time-consuming to summarize lengthy documents
   - Need for an intelligent AI assistant

2. Project Objective
   - Translate text between multiple languages
   - Automatically detect the input language
   - Generate structured summaries
   - Support both typed and voice input
   - Allow users to download the output

3. Technologies Used
   - Python
   - Streamlit
   - Groq API
   - Llama 3.3 70B Versatile Model
   - SpeechRecognition
   - PyAudio
   - VS Code

4. System Architecture
   Show a flow diagram:
   User
   ↓
   Streamlit Frontend
   ↓
   Backend (Python)
   ↓
   Groq API
   ↓
   Llama 3.3 Model
   ↓
   Translation/Summary
   ↓
   Display & Download Result

5. Features
   - Automatic language detection
   - Translation into multiple languages
   - Text summarization
   - Voice recognition
   - Text input
   - Download translation
   - Download summary
   - User-friendly interface

6. Workflow
   Step-by-step process:
   User enters text or speaks
   ↓
   Speech converted to text (if voice input)
   ↓
   AI detects language
   ↓
   Translation or summarization
   ↓
   Output displayed
   ↓
   User downloads the result
