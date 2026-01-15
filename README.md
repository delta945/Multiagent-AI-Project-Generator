# 🚀 AI Project Generator

An intelligent AI-powered project generator that creates complete, production-ready codebases from natural language descriptions. Built with LangGraph and Streamlit, this tool transforms your ideas into functional applications in seconds.

![Project Generator Demo](/images/demo1.png)

## ✨ Features

- **Framework-Specific Generation**: Specify frameworks like Next.js, React, Vue.js, Flask, Django, and more
- **Language Support**: Works with JavaScript, TypeScript, Python, and other languages
- **Complete Project Structure**: Generates all necessary files with proper organization
- **Beautiful Web Interface**: Modern Streamlit UI for easy interaction
- **Live Preview**: Preview web projects directly in the browser
- **ZIP Download**: Download your generated project as a ZIP file
- **Intelligent Planning**: AI analyzes your requirements and creates a structured plan

## 🎬 Demo

### 1. Enter Your Project Description
Simply describe what you want to build in natural language:

![Entering project prompt](/images/demo1.png)

### 2. View Generated Project Structure
The AI creates a complete file structure with all necessary components:

![Generated files overview](/images/demo2.png)

### 3. Inspect the Generated Code
Every file contains complete, functional, well-structured code:

![Code preview](/images/demo3.png)

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/delta945/Multiagent-AI-Project-Generator.git
   cd agent_developer
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   
   Create a `.env` file in the root directory:
   ```bash
   GROQ_API_KEY=your_groq_api_key_here
   ```

## 🚀 Usage

### Using the Streamlit Web Interface (Recommended)

1. **Start the Streamlit app**
   ```bash
   streamlit run app.py
   ```

2. **Open your browser** to `http://localhost:8501`

3. **Enter your project description**
   
   Be specific about what you want:
   - Mention the framework (Next.js, React, Flask, etc.)
   - Specify the language (TypeScript, Python, JavaScript)
   - Describe the features you need
   - Include styling preferences (Tailwind, Material-UI, etc.)

4. **Generate and download** your project!

The system will:
- Analyze your requirements
- Create a detailed project plan
- Generate all necessary files
- Provide a downloadable ZIP archive

### Using the Command Line Interface

```bash
python src/main.py
```

Then enter your project prompt when asked.

## 📖 How It Works

The AI Project Generator uses a sophisticated multi-agent architecture powered by LangGraph:

### 1. **Planner Agent** 
Analyzes your natural language prompt and creates a structured project plan:
- Detects specified frameworks and languages
- Identifies required features and functionality
- Plans optimal file structure and organization
- Determines dependencies and integrations

### 2. **Architect Agent**
Breaks down the plan into actionable implementation tasks:
- Creates detailed task descriptions for each component
- Manages dependencies between files
- Ensures proper integration patterns
- Defines interfaces and data flow

### 3. **Coder Agent**
Implements each task with production-quality code:
- Writes complete, functional code for every file
- Maintains consistency across the entire codebase
- Follows framework-specific best practices
- Includes proper error handling and edge cases

## 🎯 Example Prompts

### Web Applications
```
"Create a modern todo app using Next.js with TypeScript, featuring add, delete, 
and mark as complete functionality with a clean UI"
```

```
"Build a React portfolio website with smooth animations, dark mode, 
and a working contact form"
```

```
"Make a Vue.js e-commerce product listing page with filters, search, 
and shopping cart functionality"
```

### Backend APIs
```
"Create a Flask REST API with user authentication, JWT tokens, 
and CRUD operations for a blog platform"
```

```
"Build a FastAPI service with PostgreSQL integration, user management, 
and async endpoints"
```

```
"Make a Django blog API with posts, comments, categories, and user profiles"
```

### Static Websites
```
"Create a beautiful landing page with HTML, CSS, and JavaScript featuring 
parallax scrolling and smooth animations"
```

```
"Build a responsive portfolio website with dark mode toggle, smooth scroll 
navigation, and a project showcase grid"
```

```
"Make a colorful gradient-based pricing page with comparison tables 
and animated feature cards"
```

## 📁 Project Structure

```
agent_developer/
├── app.py                 # Streamlit web interface
├── src/
│   ├── main.py           # CLI entry point
│   ├── agent/
│   │   ├── graph.py      # LangGraph agent definition
│   │   └── states.py     # State models
│   ├── prompts/
│   │   └── prompt.py     # Agent prompts and templates
│   └── tools/
│       └── tools.py      # File operations tools
├── generated_project/     # Output directory for generated projects
├── images/               # Demo screenshots
│   ├── demo1.png        # Project prompt interface
│   ├── demo2.png        # Generated files view
│   └── demo3.png        # Code preview
└── requirements.txt      # Python dependencies
```

## 🎨 Features of the Streamlit Interface

### 📝 Generate Tab
- **Input Area**: Enter your project description with full detail
- **Recursion Control**: Adjust complexity limit for larger projects
- **Plan Visualization**: View the generated project plan with:
  - Detected framework and programming language
  - Complete feature list
  - File count and structure overview
  - Implementation strategy

### 📁 Generated Files Tab
- **File Browser**: Navigate through the complete project structure
- **Syntax Highlighting**: View code with beautiful syntax coloring
- **One-Click Download**: Get entire project as a ZIP file
- **Organized Tree View**: See file hierarchy at a glance

### 👁️ Preview Tab
- **Live Preview**: Instant rendering for HTML/CSS/JS projects
- **Automatic Asset Injection**: CSS and JS automatically integrated
- **Framework Instructions**: Step-by-step guide for running React, Next.js, and other framework projects locally

## ⚙️ Configuration

### Recursion Limit
Fine-tune the generation depth in the sidebar (50-200) based on your project's complexity:

- **50-75**: Simple projects
  - Single page applications
  - Basic static websites
  - Few components (3-5 files)

- **100** (Default): Standard projects
  - Multi-page applications
  - Moderate feature sets
  - 5-15 files

- **150-200**: Complex projects
  - Full-stack applications
  - Many features and integrations
  - 15+ files with intricate dependencies

### Framework Detection
The system intelligently detects frameworks mentioned in your prompt:

- **Frontend**: Next.js, React, Vue.js, Angular, Svelte
- **Backend**: Flask, Django, FastAPI, Express, NestJS
- **Full-Stack**: MERN, MEAN, Django + React
- **Static**: HTML/CSS/JS, Jekyll, Hugo
- **Mobile**: React Native, Flutter (basic structure)

## 🔧 Troubleshooting

### "Error generating project"
- ✅ Verify your `GROQ_API_KEY` is set correctly in `.env`
- ✅ Ensure you have a stable internet connection
- ✅ Try increasing the recursion limit for complex projects
- ✅ Check the console for specific error messages

### "No files generated" or incomplete output
- ✅ Make your prompt more specific and detailed
- ✅ Explicitly mention framework and programming language
- ✅ Add concrete details about desired features
- ✅ Increase recursion limit if the project is complex

### Preview not working
- ✅ Preview only works for standalone HTML/CSS/JS projects
- ✅ For React/Next.js/Vue, download ZIP and run locally with npm/yarn
- ✅ Check browser console (F12) for JavaScript errors
- ✅ Ensure pop-ups are allowed if preview opens in new window

### Generated code has errors
- ✅ Provide more context in your prompt about desired behavior
- ✅ Specify versions if you need specific framework versions
- ✅ Download and test locally - some features may require dependencies
- ✅ Review the generated package.json for required installations

## 💡 Tips for Best Results

1. **Be Specific**: Instead of "make a website", try "create a React portfolio website with dark mode, smooth scrolling, and a contact form using Tailwind CSS"

2. **Mention Frameworks**: Always specify your preferred framework and language

3. **List Features**: Explicitly list the features you want (authentication, database, API, etc.)

4. **Styling Preferences**: Mention if you want Tailwind, Bootstrap, Material-UI, or custom CSS

5. **Start Simple**: Test with simpler projects first to understand the system's capabilities

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

Please ensure your code follows the existing style and includes appropriate documentation.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- **LangGraph**: Powering the multi-agent orchestration ([LangGraph](https://github.com/langchain-ai/langgraph))
- **Streamlit**: Providing the beautiful web interface ([Streamlit](https://streamlit.io/))
- **Groq**: Lightning-fast LLM inference ([Groq](https://groq.com/))

## 🔮 Future Enhancements

- [ ] Support for more frameworks (Astro, Remix, SolidJS)
- [ ] Database schema generation
- [ ] API documentation generation
- [ ] Test file generation
- [ ] Docker containerization
- [ ] CI/CD pipeline templates
- [ ] Real-time collaboration features

---

**Transform your ideas into code instantly! 🎉**

Have questions or suggestions? Open an issue or reach out to the community!