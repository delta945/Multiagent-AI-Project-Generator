# Quick Start Guide

## 🚀 Get Started in 3 Steps

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Set Up Environment
Create a `.env` file with your API key:
```
GROQ_API_KEY=your_api_key_here
```

### Step 3: Run the App
```bash
streamlit run app.py
```

Or simply double-click `run_app.bat` on Windows!

## 💡 Example Usage

1. Open the app in your browser (http://localhost:8501)
2. Enter a prompt like:
   - "Create a todo app using Next.js and TypeScript"
   - "Build a Flask API with authentication"
   - "Make a colorful portfolio in HTML, CSS, JS"
3. Click "Generate Project"
4. Download your project as ZIP!

## 🎯 Key Features

### Framework Detection
The AI automatically detects and uses your specified framework:
- ✅ Next.js
- ✅ React
- ✅ Vue.js
- ✅ Angular
- ✅ Flask
- ✅ Django
- ✅ FastAPI
- ✅ And more!

### Language Support
Specify your preferred language:
- ✅ JavaScript
- ✅ TypeScript
- ✅ Python
- ✅ Go
- ✅ And more!

## 📱 Interface Overview

### Generate Tab
- Input your project description
- Adjust settings
- View project plan after generation

### Generated Files Tab
- Browse all files with syntax highlighting
- Download as ZIP
- Copy code snippets

### Preview Tab
- Live preview for HTML/CSS/JS projects
- Instructions for running framework projects

## 🔧 Tips

1. **Be Specific**: Mention framework and language explicitly
   - Good: "Create a todo app using Next.js with TypeScript"
   - Better: "Create a modern todo app using Next.js 14 with TypeScript, featuring add, delete, mark complete, with a gradient purple UI"

2. **Adjust Recursion Limit**: For complex projects, increase to 150-200

3. **Check the Plan**: Review the generated plan to ensure it matches your requirements

## ❓ Troubleshooting

**App won't start?**
- Make sure Streamlit is installed: `pip install streamlit`
- Check Python version (3.8+ required)

**No files generated?**
- Verify your GROQ_API_KEY in `.env`
- Make your prompt more detailed
- Increase recursion limit

**Preview not working?**
- Preview only works for HTML/CSS/JS
- For React/Next.js, download and run locally

## 🎉 You're Ready!

Start generating amazing projects with AI!
