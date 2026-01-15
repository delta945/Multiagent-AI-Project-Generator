from typing import Optional, List
from pydantic import BaseModel, Field, ConfigDict


class File(BaseModel):
    """Represents a file to be created in the project"""
    path: str = Field(description="The path to the file to be created or modified")
    purpose: str = Field(description="The purpose of the file, e.g. 'main application logic', 'data processing module', etc.")
    

class Plan(BaseModel):
    """Complete project plan with all necessary information"""
    name: str = Field(description="The name of app to be built")
    description: str = Field(description="A one-line description of the app to be built, e.g. 'A web application for managing personal finances'")
    framework: Optional[str] = Field(None, description="The primary framework to be used, e.g. 'Next.js', 'React', 'Vue.js', 'Flask', 'Django', etc. Extract from user prompt if specified. If not specified, use None for simple HTML/CSS/JS projects.")
    language: Optional[str] = Field(None, description="The primary programming language, e.g. 'JavaScript', 'TypeScript', 'Python', 'Go', etc. Extract from user prompt if specified.")
    techstack: str = Field(description="The tech stack to be used for the app, e.g. 'HTML, CSS, JavaScript', 'React, TypeScript, Tailwind CSS', 'Flask, Python, SQLite', etc.")
    features: List[str] = Field(description="A list of features that the app should have, e.g. ['user authentication', 'data visualization', 'CRUD operations']")
    files: List[File] = Field(description="A list of files to be created, each with a 'path' and 'purpose'")


class ImplementationTask(BaseModel):
    """A single implementation task for a file"""
    filepath: str = Field(description="The path to the file to be modified or created")
    task_description: str = Field(description="A detailed description of the task to be performed on the file, e.g. 'Create the main HTML structure with header, main content area, and footer', 'Implement user authentication logic with login and signup functions', etc.")


class TaskPlan(BaseModel):
    """Complete task plan with all implementation steps"""
    implementation_steps: List[ImplementationTask] = Field(description="A list of steps to be taken to implement the project, ordered by dependency")
    model_config = ConfigDict(extra="allow")
    

class CoderState(BaseModel):
    """State management for the coder agent"""
    task_plan: TaskPlan = Field(description="The plan for the task to be implemented")
    current_step_idx: int = Field(0, description="The index of the current step in the implementation steps")
    current_file_content: Optional[str] = Field(None, description="The content of the file currently being edited or created")