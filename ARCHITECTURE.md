# Agent Flow Architecture

## 🔄 Complete Flow Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                         USER INPUT                               │
│  "Create a todo app using Next.js with TypeScript"              │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│                    PLANNER AGENT                                 │
│  • Analyzes user prompt                                          │
│  • Detects framework (Next.js)                                   │
│  • Detects language (TypeScript)                                 │
│  • Identifies features                                           │
│  • Creates file structure plan                                   │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ▼
                    ┌────────┐
                    │  PLAN  │
                    │  State │
                    └────┬───┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│                   ARCHITECT AGENT                                │
│  • Breaks plan into implementation tasks                         │
│  • Orders tasks by dependencies                                  │
│  • Creates detailed task descriptions                            │
│  • Specifies functions, classes, variables                       │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ▼
                   ┌──────────┐
                   │ TASK PLAN│
                   │  State   │
                   └────┬─────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────────────┐
│                     CODER AGENT                                  │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │  For each task in task_plan:                              │  │
│  │    1. Read existing file (if any)                         │  │
│  │    2. Generate complete code                              │  │
│  │    3. Write file to disk                                  │  │
│  │    4. Move to next task                                   │  │
│  └───────────────────────────────────────────────────────────┘  │
│                                                                  │
│  Tools Available:                                                │
│  • write_file(path, content)                                     │
│  • read_file(path)                                               │
│  • list_files(directory)                                         │
│  • get_current_directory()                                       │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ▼
                  ┌──────────────┐
                  │ All tasks    │
                  │ completed?   │
                  └──┬────────┬──┘
                     │        │
                  NO │        │ YES
                     │        │
                     ▼        ▼
              ┌──────────┐  ┌────────────────┐
              │ Continue │  │  FINAL STATE   │
              │ to next  │  │  Project Done! │
              │   task   │  └────────────────┘
              └──────────┘
```

## 📊 State Flow

```
Initial State:
{
  "user_prompt": "Create a todo app using Next.js with TypeScript"
}
         ↓
After Planner:
{
  "user_prompt": "...",
  "plan": {
    "name": "Next.js Todo App",
    "description": "A modern todo application",
    "framework": "Next.js",
    "language": "TypeScript",
    "techstack": "Next.js, TypeScript, React",
    "features": ["Add todos", "Delete todos", "Mark complete"],
    "files": [
      {"path": "package.json", "purpose": "Project dependencies"},
      {"path": "app/page.tsx", "purpose": "Main page component"},
      {"path": "components/TodoList.tsx", "purpose": "Todo list component"},
      ...
    ]
  }
}
         ↓
After Architect:
{
  "user_prompt": "...",
  "plan": {...},
  "task_plan": {
    "implementation_steps": [
      {
        "filepath": "package.json",
        "task_description": "Create package.json with Next.js 14, TypeScript, and React dependencies..."
      },
      {
        "filepath": "app/page.tsx",
        "task_description": "Create main page component that imports TodoList and renders it..."
      },
      ...
    ]
  }
}
         ↓
After Coder (iterative):
{
  "user_prompt": "...",
  "plan": {...},
  "task_plan": {...},
  "coder_state": {
    "current_step_idx": 5,  // Completed 5 tasks
    "task_plan": {...}
  },
  "status": "DONE"
}
```

## 🎯 Key Improvements

### 1. Framework Detection
The planner now explicitly looks for framework mentions:
- Next.js, React, Vue.js, Angular, Svelte
- Flask, Django, FastAPI, Express
- And more!

### 2. Language Detection
Detects programming language preferences:
- JavaScript vs TypeScript
- Python versions
- Other languages

### 3. Structured Output
The Plan model now includes:
```python
class Plan(BaseModel):
    name: str
    description: str
    framework: Optional[str]  # NEW!
    language: Optional[str]   # NEW!
    techstack: str
    features: list[str]
    files: list[File]
```

## 🖥️ Streamlit Interface Flow

```
User Opens App
      ↓
┌─────────────────┐
│  Generate Tab   │
│  • Input prompt │
│  • Settings     │
└────────┬────────┘
         │ Click Generate
         ▼
┌─────────────────┐
│  Agent Process  │
│  (Background)   │
└────────┬────────┘
         │
         ▼
┌─────────────────────────────────┐
│  Display Results                │
│  • Project plan                 │
│  • Framework & language         │
│  • Features list                │
└─────────────────────────────────┘
         │
         ├─────────────────┬─────────────────┐
         ▼                 ▼                 ▼
┌─────────────────┐ ┌──────────────┐ ┌──────────────┐
│ Generated Files │ │   Preview    │ │  Download    │
│  • File tree    │ │  • HTML view │ │  • ZIP file  │
│  • Code viewer  │ │  • Run guide │ │              │
└─────────────────┘ └──────────────┘ └──────────────┘
```

## 🔧 Tools Integration

```
Coder Agent
     │
     ├─→ write_file(path, content)
     │   └─→ Writes to: generated_project/{path}
     │
     ├─→ read_file(path)
     │   └─→ Reads from: generated_project/{path}
     │
     ├─→ list_files(directory)
     │   └─→ Lists: generated_project/{directory}/*
     │
     └─→ get_current_directory()
         └─→ Returns: generated_project/
```

## 📦 Output Structure

```
generated_project/
├── package.json          (if Next.js/React/Vue)
├── tsconfig.json         (if TypeScript)
├── next.config.js        (if Next.js)
├── app/
│   ├── page.tsx
│   └── layout.tsx
├── components/
│   ├── TodoList.tsx
│   └── TodoItem.tsx
├── styles/
│   └── globals.css
└── public/
    └── ...
```

Or for HTML/CSS/JS:
```
generated_project/
├── index.html
├── style.css
├── script.js
└── README.md
```

## 🎨 Streamlit Features

1. **Syntax Highlighting**: Automatic language detection
2. **Live Preview**: For HTML/CSS/JS projects
3. **ZIP Download**: One-click project download
4. **File Browser**: Tree view of all files
5. **Plan Display**: Shows detected framework/language
6. **Error Handling**: Clear error messages

---

This architecture ensures that user-specified frameworks and languages are respected throughout the entire generation process!
