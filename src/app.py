import streamlit as st
import sys
import os
import zipfile
import io
import json
from pathlib import Path
import traceback
import shutil

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from agent.graph import agent
from tools.tools import PROJECT_ROOT, init_project_root

# Page configuration
st.set_page_config(
    page_title="AI Project Generator",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stButton>button {
        width: 100%;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 0.75rem 1.5rem;
        font-size: 1.1rem;
        font-weight: 600;
        border-radius: 10px;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 20px rgba(0,0,0,0.2);
    }
    .success-box {
        padding: 1.5rem;
        border-radius: 10px;
        background: linear-gradient(135deg, #667eea15 0%, #764ba215 100%);
        border-left: 4px solid #667eea;
        margin: 1rem 0;
    }
    .code-file {
        background: #1e1e1e;
        border-radius: 8px;
        padding: 1rem;
        margin: 0.5rem 0;
    }
    .file-header {
        color: #61dafb;
        font-weight: 600;
        margin-bottom: 0.5rem;
        font-family: 'Courier New', monospace;
    }
    h1 {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3rem;
        font-weight: 800;
        margin-bottom: 0.5rem;
    }
    .subtitle {
        color: #666;
        font-size: 1.2rem;
        margin-bottom: 2rem;
    }
    .stTextArea textarea {
        border-radius: 10px;
        border: 2px solid #e0e0e0;
        font-size: 1rem;
    }
    .stTextArea textarea:focus {
        border-color: #667eea;
        box-shadow: 0 0 0 2px rgba(102, 126, 234, 0.1);
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if 'generated_project' not in st.session_state:
    st.session_state.generated_project = None
if 'project_files' not in st.session_state:
    st.session_state.project_files = {}
if 'generation_status' not in st.session_state:
    st.session_state.generation_status = None
if 'plan_info' not in st.session_state:
    st.session_state.plan_info = None

def get_all_files(directory):
    """Recursively get all files in a directory"""
    files = {}
    dir_path = Path(directory)
    if not dir_path.exists():
        return files
    
    for file_path in dir_path.rglob('*'):
        if file_path.is_file():
            relative_path = file_path.relative_to(dir_path)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                files[str(relative_path)] = content
            except Exception as e:
                files[str(relative_path)] = f"Error reading file: {str(e)}"
    return files

def create_zip_download(files_dict):
    """Create a ZIP file from the generated files"""
    zip_buffer = io.BytesIO()
    with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
        for file_path, content in files_dict.items():
            zip_file.writestr(file_path, content)
    zip_buffer.seek(0)
    return zip_buffer

def get_language_from_extension(filename):
    """Get syntax highlighting language from file extension"""
    ext_map = {
        '.py': 'python',
        '.js': 'javascript',
        '.jsx': 'javascript',
        '.ts': 'typescript',
        '.tsx': 'typescript',
        '.html': 'html',
        '.css': 'css',
        '.json': 'json',
        '.md': 'markdown',
        '.yml': 'yaml',
        '.yaml': 'yaml',
        '.sh': 'bash',
        '.txt': 'text',
        '.env': 'bash',
    }
    ext = Path(filename).suffix
    return ext_map.get(ext, 'text')

def generate_project(user_prompt, recursion_limit=100):
    """Generate project using the agent"""
    try:
        # Initialize project root
        init_project_root()
        
        # Clear previous project
        if PROJECT_ROOT.exists():
            for item in PROJECT_ROOT.iterdir():
                if item.is_file():
                    item.unlink()
                elif item.is_dir():
                    shutil.rmtree(item)
        
        # Run the agent
        with st.spinner('🤖 AI is analyzing your request...'):
            result = agent.invoke(
                {"user_prompt": user_prompt},
                {"recursion_limit": recursion_limit}
            )
        
        # Extract plan information
        plan_info = None
        if 'plan' in result:
            plan = result['plan']
            plan_info = {
                'name': getattr(plan, 'name', 'Unknown'),
                'description': getattr(plan, 'description', 'No description'),
                'framework': getattr(plan, 'framework', 'Not specified'),
                'language': getattr(plan, 'language', 'Not specified'),
                'techstack': getattr(plan, 'techstack', 'Not specified'),
                'features': getattr(plan, 'features', [])
            }
        
        # Get all generated files
        files = get_all_files(PROJECT_ROOT)
        
        return {
            'success': True,
            'files': files,
            'plan_info': plan_info,
            'result': result
        }
    except Exception as e:
        return {
            'success': False,
            'error': str(e),
            'traceback': traceback.format_exc()
        }

# Header
st.markdown("<h1>🚀 AI Project Generator</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Transform your ideas into complete projects with AI-powered code generation</p>", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.header("⚙️ Settings")
    recursion_limit = st.slider(
        "Recursion Limit",
        min_value=50,
        max_value=200,
        value=100,
        step=10,
        help="Maximum number of agent iterations"
    )
    
    st.markdown("---")
    st.header("📖 Examples")
    st.markdown("""
    **Try these prompts:**
    
    - *Create a todo app using Next.js and TypeScript*
    - *Build a React dashboard with charts*
    - *Make a Flask API with user authentication*
    - *Create a Vue.js e-commerce site*
    - *Build a colorful portfolio website in HTML, CSS, and JavaScript*
    """)
    
    st.markdown("---")
    st.header("ℹ️ About")
    st.info("""
    This AI-powered tool generates complete project codebases based on your natural language descriptions.
    
    **Features:**
    - Framework-specific generation
    - Complete file structure
    - Ready-to-use code
    - ZIP download
    - Live preview (for web projects)
    """)

# Main content
tab1, tab2, tab3 = st.tabs(["📝 Generate", "📁 Generated Files", "👁️ Preview"])

with tab1:
    st.header("Describe Your Project")
    
    user_prompt = st.text_area(
        "Enter your project description:",
        height=150,
        placeholder="Example: Create a modern todo app using Next.js with TypeScript, featuring add, delete, and mark as complete functionality with a beautiful gradient UI",
        help="Be specific about frameworks, languages, and features you want"
    )
    
    col1, col2, col3 = st.columns([2, 1, 1])
    
    with col1:
        generate_btn = st.button("🎨 Generate Project", type="primary")
    
    if generate_btn:
        if not user_prompt.strip():
            st.error("⚠️ Please enter a project description!")
        else:
            # Generate project
            with st.spinner('🔮 Generating your project... This may take a minute...'):
                result = generate_project(user_prompt, recursion_limit)
            
            if result['success']:
                st.session_state.generated_project = result
                st.session_state.project_files = result['files']
                st.session_state.plan_info = result.get('plan_info')
                st.session_state.generation_status = 'success'
                
                st.success("✅ Project generated successfully!")
                st.balloons()
                
                # Display plan information
                if st.session_state.plan_info:
                    st.markdown("<div class='success-box'>", unsafe_allow_html=True)
                    st.subheader("📋 Project Plan")
                    
                    col1, col2 = st.columns(2)
                    with col1:
                        st.write(f"**Name:** {st.session_state.plan_info['name']}")
                        st.write(f"**Framework:** {st.session_state.plan_info['framework']}")
                        st.write(f"**Language:** {st.session_state.plan_info['language']}")
                    with col2:
                        st.write(f"**Tech Stack:** {st.session_state.plan_info['techstack']}")
                        st.write(f"**Files Generated:** {len(st.session_state.project_files)}")
                    
                    st.write(f"**Description:** {st.session_state.plan_info['description']}")
                    
                    if st.session_state.plan_info['features']:
                        st.write("**Features:**")
                        for feature in st.session_state.plan_info['features']:
                            st.write(f"  • {feature}")
                    
                    st.markdown("</div>", unsafe_allow_html=True)
                
            else:
                st.session_state.generation_status = 'error'
                st.error(f"❌ Error generating project: {result['error']}")
                with st.expander("View Error Details"):
                    st.code(result['traceback'])

with tab2:
    st.header("Generated Files")
    
    if st.session_state.project_files:
        # Download button
        zip_buffer = create_zip_download(st.session_state.project_files)
        st.download_button(
            label="📦 Download Project as ZIP",
            data=zip_buffer,
            file_name=f"{st.session_state.plan_info.get('name', 'project').replace(' ', '_')}.zip" if st.session_state.plan_info else "project.zip",
            mime="application/zip",
            type="primary"
        )
        
        st.markdown("---")
        
        # Display files
        st.subheader(f"📂 Files ({len(st.session_state.project_files)})")
        
        # File tree view
        for file_path in sorted(st.session_state.project_files.keys()):
            with st.expander(f"📄 {file_path}"):
                content = st.session_state.project_files[file_path]
                language = get_language_from_extension(file_path)
                st.code(content, language=language, line_numbers=True)
    else:
        st.info("👈 Generate a project first to see the files here!")

with tab3:
    st.header("Live Preview")
    
    if st.session_state.project_files:
        # Check if it's a web project
        has_html = any(f.endswith('.html') for f in st.session_state.project_files.keys())
        has_index = 'index.html' in st.session_state.project_files
        
        if has_html:
            st.info("🌐 Web project detected!")
            
            if has_index:
                st.markdown("### Preview of index.html")
                
                # Create a simple preview using iframe
                html_content = st.session_state.project_files['index.html']
                
                # Inject CSS if exists
                if 'style.css' in st.session_state.project_files or 'styles.css' in st.session_state.project_files:
                    css_file = 'style.css' if 'style.css' in st.session_state.project_files else 'styles.css'
                    css_content = st.session_state.project_files[css_file]
                    html_content = html_content.replace('</head>', f'<style>{css_content}</style></head>')
                
                # Inject JS if exists
                if 'script.js' in st.session_state.project_files or 'app.js' in st.session_state.project_files:
                    js_file = 'script.js' if 'script.js' in st.session_state.project_files else 'app.js'
                    js_content = st.session_state.project_files[js_file]
                    html_content = html_content.replace('</body>', f'<script>{js_content}</script></body>')
                
                # Display preview
                st.components.v1.html(html_content, height=600, scrolling=True)
                
                st.markdown("---")
                st.caption("💡 Tip: Download the project and open it in your browser for full functionality")
            else:
                st.warning("⚠️ No index.html found. Preview is only available for projects with an index.html file.")
                st.write("**Available HTML files:**")
                for f in st.session_state.project_files.keys():
                    if f.endswith('.html'):
                        st.write(f"  • {f}")
        else:
            st.info("ℹ️ Preview is only available for web projects (HTML/CSS/JS)")
            
            if st.session_state.plan_info:
                framework = st.session_state.plan_info.get('framework', '').lower()
                if any(fw in framework for fw in ['react', 'next', 'vue', 'angular', 'svelte']):
                    st.markdown("""
                    **To run this project:**
                    
                    1. Download the project ZIP
                    2. Extract the files
                    3. Install dependencies: `npm install`
                    4. Run development server: `npm run dev`
                    """)
                elif 'flask' in framework or 'django' in framework or 'fastapi' in framework:
                    st.markdown("""
                    **To run this project:**
                    
                    1. Download the project ZIP
                    2. Extract the files
                    3. Install dependencies: `pip install -r requirements.txt`
                    4. Run the application (check README for specific commands)
                    """)
    else:
        st.info("👈 Generate a project first to see the preview here!")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; padding: 2rem 0;'>
    <p>Built with ❤️ using Streamlit and LangGraph</p>
    <p style='font-size: 0.9rem;'>Powered by AI • Generate any project in seconds</p>
</div>
""", unsafe_allow_html=True)