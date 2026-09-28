# 🚀 VisionDesk AI

## AI-Powered Visual Data Analytics & Business Intelligence Platform

VisionDesk AI is an AI-powered Visual Data Analytics and Business Intelligence platform that combines **Computer Vision, Document Intelligence, Retrieval-Augmented Generation (RAG), AI Agents, Data Analytics, and Automated Reporting** into a single application.

The project was developed as part of the **Infosys Springboard Internship** and progressed through four milestones, starting from visual object detection and PPE detection and evolving into a complete AI-powered analytics platform.

---

# 📌 Table of Contents

- [Project Overview](#-project-overview)
- [Problem Statement](#-problem-statement)
- [Solution](#-solution)
- [Objectives](#-objectives)
- [Key Features](#-key-features)
- [Project Milestones](#-project-milestones)
- [System Architecture](#-system-architecture)
- [Application Workflow](#-application-workflow)
- [PPE Detection Workflow](#-ppe-detection-workflow)
- [Document Intelligence Workflow](#-document-intelligence-workflow)
- [RAG Workflow](#-rag-workflow)
- [AI Agent Workflow](#-ai-agent-workflow)
- [Dashboard Workflow](#-dashboard-workflow)
- [Reporting Workflow](#-reporting-workflow)
- [Technologies Used](#-technologies-used)
- [Project Structure](#-project-structure)
- [Module Description](#-module-description)
- [Installation](#-installation)
- [API Configuration](#-api-configuration)
- [Running the Application](#-running-the-application)
- [Application Pages](#-application-pages)
- [How to Use](#-how-to-use)
- [Example Use Case](#-example-use-case)
- [Input and Output](#-input-and-output)
- [AI Components](#-ai-components)
- [Security](#-security)
- [Testing](#-testing)
- [Limitations](#-limitations)
- [Future Enhancements](#-future-enhancements)
- [Learning Outcomes](#-learning-outcomes)
- [Internship Information](#-internship-information)
- [Team Members](#-team-members)
- [Acknowledgements](#-acknowledgements)
- [Disclaimer](#-disclaimer)
- [License](#-license)

---

# 📖 Project Overview

Modern organizations work with different forms of data such as images, videos, documents, and analytical records.

Analyzing all these sources separately can be time-consuming and inefficient.

**VisionDesk AI** provides a unified platform that brings multiple AI capabilities together.

The platform allows users to:

- Analyze images and videos.
- Detect PPE and safety violations.
- Process PDF, TXT, and DOCX documents.
- Create a searchable knowledge base.
- Retrieve information from documents.
- Ask questions using an AI assistant.
- Use Retrieval-Augmented Generation.
- Combine visual and document-based information.
- View analytics through dashboards.
- Track scan history.
- Generate PDF and CSV reports.

---

# ❗ Problem Statement

Organizations often use different tools for:

- Computer vision
- Document processing
- Information retrieval
- Data analytics
- Reporting

This creates a fragmented workflow.

For example, a safety team may need one application for PPE detection, another tool for reading safety manuals, another system for analytics, and another tool for reporting.

VisionDesk AI aims to combine these capabilities into one platform.

---

# 💡 Proposed Solution

VisionDesk AI integrates:

```text
Computer Vision
       +
Document Intelligence
       +
Knowledge Base
       +
Vector Search
       +
RAG
       +
AI Agent
       +
Data Analytics
       +
Automated Reporting

into a single Streamlit-based application.

🎯 Objectives

The main objectives of VisionDesk AI are:

Develop an AI-powered visual analysis system.
Detect PPE using YOLO.
Identify potential safety violations.
Process documents automatically.
Extract useful information from documents.
Create a searchable knowledge base.
Implement Retrieval-Augmented Generation.
Develop an AI-powered question-answering system.
Combine visual and textual information.
Provide an analytics dashboard.
Maintain historical scan records.
Generate automated PDF and CSV reports.
Provide a modern and user-friendly interface.
✨ Key Features
👷 PPE Detection

VisionDesk AI uses a trained YOLO model for visual detection.

Features include:

Image upload
Video upload
Object detection
PPE detection
Confidence scores
Compliance checking
Violation identification
Annotated detection results
Scan history
📄 Document Intelligence

The application supports:

PDF
TXT
DOCX

Uploaded documents are processed and divided into smaller chunks for retrieval.

Processing Pipeline
Document Upload
      ↓
Text Extraction
      ↓
Text Processing
      ↓
Text Chunking
      ↓
Knowledge Base
🤖 Ask AI

The Ask AI module allows users to ask questions in natural language.

Example:

What PPE is required in construction areas?

The system retrieves relevant information from the knowledge base and uses an LLM to generate an answer.

🔎 Knowledge Base

The knowledge base stores processed document information.

It allows the system to:

Store document chunks
Search relevant information
Retrieve context
Support AI question answering
🧠 Retrieval-Augmented Generation

RAG allows the AI system to retrieve relevant information before generating an answer.

This helps the LLM answer questions using information from the uploaded project documents.

🔗 AI Agent

The AI agent can combine information from:

Uploaded documents
Knowledge base
PPE detection results
Visual analysis

This enables more contextual AI responses.

📊 Analytics Dashboard

The dashboard provides:

Total scans
Compliant scans
Non-compliant scans
Violation statistics
Historical records
Detection trends
Data tables
KPI cards
📋 Automated Reporting

The reporting module generates:

Summary reports
PPE statistics
Scan history
PDF reports
CSV exports
🏗️ Project Milestones
🟦 Milestone 1 — AI Visual Analytics

The first milestone focused on implementing the basic computer vision pipeline.

Implemented
Image upload
YOLO object detection
Object identification
Confidence scores
Detection visualization
Streamlit interface
Workflow
Image
  ↓
Upload
  ↓
YOLO Model
  ↓
Object Detection
  ↓
Confidence Score
  ↓
Detection Result
🟩 Milestone 2 — PPE Detection

The second milestone extended the computer vision system for workplace safety monitoring.

Implemented
PPE detection
Construction-site image analysis
Safety violation detection
Compliance checking
Confidence scores
Image processing
Video processing
Workflow
Construction Image / Video
            ↓
        YOLO Model
            ↓
      Object Detection
            ↓
       PPE Detection
            ↓
    Compliance Analysis
            ↓
   Violation Identification
            ↓
       Final Result
🟨 Milestone 3 — Document Intelligence & RAG

The third milestone introduced document processing and AI-powered retrieval.

Implemented
PDF processing
TXT processing
DOCX processing
Text extraction
Text chunking
Embeddings
Vector search
Knowledge base
RAG-based question answering
Workflow
Document
   ↓
Text Extraction
   ↓
Text Chunking
   ↓
Embeddings
   ↓
Vector Database
   ↓
User Query
   ↓
Similarity Search
   ↓
Relevant Context
   ↓
LLM
   ↓
AI Answer
🟥 Milestone 4 — Complete VisionDesk AI Platform

The final milestone integrates all previous components into one platform.

PPE Detection
      +
Document Intelligence
      +
Knowledge Base
      +
RAG
      +
AI Agent
      +
Analytics
      +
Reporting

The final system provides a unified AI-powered dashboard through Streamlit.

🏛️ System Architecture
                         ┌──────────────────────┐
                         │     VisionDesk AI     │
                         │    Streamlit App      │
                         └───────────┬──────────┘
                                     │
             ┌───────────────────────┼───────────────────────┐
             │                       │                       │
             ▼                       ▼                       ▼
      ┌─────────────┐        ┌──────────────┐        ┌─────────────┐
      │ PPE Detection│        │  Documents   │        │   Ask AI    │
      └──────┬──────┘        └──────┬───────┘        └──────┬──────┘
             │                      │                       │
             ▼                      ▼                       ▼
        YOLO Model            Text Extraction            AI Agent
             │                      │                       │
             ▼                      ▼                       ▼
      Detection Results       Text Chunks              RAG Search
             │                      │                       │
             │                      ▼                       ▼
             │               Knowledge Base                LLM
             │                      │                       │
             └──────────────┬───────┴───────────────────────┘
                            │
                            ▼
                   ┌──────────────────┐
                   │ Analytics Engine │
                   └────────┬─────────┘
                            │
                  ┌─────────┴─────────┐
                  ▼                   ▼
             Dashboard             Reports
                                    │
                            ┌───────┴───────┐
                            ▼               ▼
                           PDF             CSV
🔄 Application Workflow
                    START
                      │
                      ▼
              Open VisionDesk AI
                      │
                      ▼
              Select Application Page
                      │
       ┌──────────────┼───────────────┐
       │              │               │
       ▼              ▼               ▼
   PPE Detection   Documents       Ask AI
       │              │               │
       ▼              ▼               ▼
   YOLO Model     Processing       RAG / Agent
       │              │               │
       └──────────────┼───────────────┘
                      │
                      ▼
                 Data Storage
                      │
                      ▼
                  Dashboard
                      │
                      ▼
                   Report
                      │
                      ▼
                    END
👷 PPE Detection Workflow
Upload Image / Video
        ↓
Save Temporary File
        ↓
Load YOLO Model
        ↓
Run Detection
        ↓
Identify Objects
        ↓
Calculate Confidence
        ↓
Check PPE Compliance
        ↓
Identify Violations
        ↓
Display Annotated Result
        ↓
Store Scan Information
📄 Document Intelligence Workflow
User Uploads Document
        ↓
Check File Type
        ↓
PDF / TXT / DOCX
        ↓
Extract Text
        ↓
Split Text Into Chunks
        ↓
Generate Embeddings
        ↓
Store in Knowledge Base
        ↓
Ready for Search
🧠 RAG Workflow

RAG stands for Retrieval-Augmented Generation.

The RAG pipeline used by the project follows this general flow:

                User Question
                      │
                      ▼
                Query Processing
                      │
                      ▼
              Query Embedding
                      │
                      ▼
              Similarity Search
                      │
                      ▼
             Relevant Text Chunks
                      │
                      ▼
             Context Construction
                      │
                      ▼
                    LLM
                      │
                      ▼
                Final Answer
Example

User asks:

What PPE is required in construction areas?

The system:

Processes the question.
Searches the knowledge base.
Finds relevant document chunks.
Retrieves the relevant context.
Sends the context to the LLM.
Generates the final answer.
🤖 AI Agent Workflow
                   User Question
                         │
                         ▼
                     AI Agent
                         │
              ┌──────────┴──────────┐
              │                     │
              ▼                     ▼
       Knowledge Base        Visual Analysis
              │                     │
              ▼                     ▼
      Relevant Documents       PPE Results
              │                     │
              └──────────┬──────────┘
                         ▼
                  Combined Context
                         │
                         ▼
                        LLM
                         │
                         ▼
                    AI Response
📊 Dashboard Workflow
PPE Scan
   ↓
Detection Result
   ↓
Storage
   ↓
Historical Records
   ↓
Data Processing
   ↓
KPIs + Charts
   ↓
Dashboard
📋 Reporting Workflow
Scan History
      ↓
Data Processing
      ↓
Statistics
      ↓
Summary Generation
      ↓
┌─────┴─────┐
▼           ▼
PDF         CSV
Report      Export
🛠️ Technologies Used
Technology	Purpose
Python	Core programming language
Streamlit	Web application framework
YOLOv8	Object detection
Ultralytics	YOLO implementation
OpenCV	Image and video processing
Pillow	Image handling
LangChain	LLM and RAG integration
LangGraph	AI agent workflow
FAISS	Vector similarity search
Gemini / LLM	AI-powered responses
PyMuPDF	PDF processing
python-docx	DOCX processing
Pandas	Data processing
FPDF / fpdf2	PDF report generation
CSV	Data export
Git	Version control
GitHub	Repository management
📂 Project Structure
AI-VisionDesk/
│
├── app.py
│
├── agent.py
├── documents.py
├── knowledge_base.py
├── llm.py
├── report.py
├── storage.py
├── vision.py
│
├── best.pt
│
├── data/
│   └── safety_manual.pdf
│
├── screenshots/
│   ├── home.png
│   ├── ppe-detection.png
│   ├── documents.png
│   ├── ask-ai.png
│   ├── dashboard.png
│   └── report.png
│
├── requirements.txt
├── .gitignore
└── README.md
📁 Module Description
app.py

Main Streamlit application.

Responsible for:

User interface
Navigation
File uploads
PPE detection interface
Document interface
Ask AI interface
Dashboard
Reports
vision.py

Handles computer vision functionality.

Responsible for:

YOLO model loading
Image detection
Video detection
Bounding boxes
PPE analysis
Compliance evaluation
documents.py

Handles document processing.

Responsible for:

PDF processing
TXT processing
DOCX processing
Text extraction
Text chunking
knowledge_base.py

Manages the document knowledge base.

Responsible for:

Storing chunks
Embeddings
Vector search
Relevant document retrieval
agent.py

Handles the AI agent workflow.

Responsible for:

User questions
Context retrieval
Combining information
AI response generation
llm.py

Handles LLM configuration.

Responsible for:

Model configuration
API key handling
LLM initialization
Model availability
storage.py

Handles application data.

Responsible for:

Scan history
Detection records
Historical data
KPI information
report.py

Handles automated reporting.

Responsible for:

Report summaries
PDF generation
CSV export
Report formatting
⚙️ Installation
1. Clone the Repository
git clone https://github.com/Lav9236/AI-VisionDesk.git

Move into the project folder:

cd AI-VisionDesk
2. Create a Virtual Environment
python -m venv .venv
3. Activate the Virtual Environment
Windows
.venv\Scripts\activate

After activation:

(.venv)

should appear in the terminal.

4. Install Dependencies
python -m pip install -r requirements.txt

If required for PDF generation:

python -m pip install fpdf2
🔑 API Configuration

VisionDesk AI requires an LLM API key for AI-powered functionality.

The API key should never be committed to GitHub.

Windows CMD
set GEMINI_API_KEY=YOUR_API_KEY
Windows PowerShell
$env:GEMINI_API_KEY="YOUR_API_KEY"
🔐 Streamlit Secrets

Alternatively, create:

.streamlit/
└── secrets.toml

Add:

GEMINI_API_KEY = "YOUR_API_KEY"

Make sure the file is included in .gitignore.

▶️ Running the Application

Activate the virtual environment and run:

python -m streamlit run app.py

The application will open in your browser.

🖥️ Application Pages

VisionDesk AI contains six major sections:

🏠 Home
👷 PPE Detection
📄 Documents
🤖 Ask AI
📊 Dashboard
📋 Report
🏠 Home

The Home page provides an overview of VisionDesk AI.

It includes:

Platform introduction
System status
AI capabilities
Feature overview
Recent activity
👷 PPE Detection

Users can upload an image or video.

The YOLO model analyzes the input and displays:

Detected objects
PPE information
Confidence scores
Compliance status
Violations
Annotated results
📄 Documents

Users can upload:

PDF
TXT
DOCX

The application extracts the text and adds the processed information to the knowledge base.

Users can then search the uploaded information.

🤖 Ask AI

Users can ask questions about the available knowledge.

Example:

What safety precautions are mentioned in the manual?

The system retrieves relevant information and generates an AI response.

📊 Dashboard

The dashboard provides:

Total scans
Compliance statistics
Violation statistics
Historical records
Detection trends
Analytical charts
📋 Report

The Report page allows users to generate:

PDF reports
CSV files
Scan summaries
Detection statistics
🚀 How to Use
Step 1

Run the application:

python -m streamlit run app.py
Step 2

Open the Home page.

Step 3

Navigate to PPE Detection.

Step 4

Upload a construction-site image or video.

Step 5

Review the detection results.

Step 6

Open Documents.

Step 7

Upload a safety manual.

Step 8

Open Ask AI.

Step 9

Ask a question related to the uploaded document.

Step 10

Open Dashboard to view analytics.

Step 11

Open Report to generate PDF or CSV output.

📌 Example Use Case
Construction Safety Monitoring

A construction organization can use VisionDesk AI to assist with workplace safety monitoring.

Workflow
Construction Image
       ↓
PPE Detection
       ↓
Worker / PPE Identification
       ↓
Compliance Analysis
       ↓
Violation Detection
       ↓
Store Result
       ↓
Dashboard
       ↓
Generate Report

The organization can also upload its safety manual and use Ask AI to retrieve safety-related information.

📥 Input
Visual Input

Supported image/video formats depend on the configured application and libraries.

Examples:

JPG
JPEG
PNG
MP4
Document Input
PDF
TXT
DOCX
📤 Output

The system can produce:

Detection results
Annotated images
Video detection results
PPE compliance status
Violation information
AI-generated answers
Dashboard analytics
PDF reports
CSV exports
🧠 AI Components
YOLO

YOLO is used for object detection.

The project uses a trained model:

best.pt

The model is used for PPE-related detection.

Computer Vision

OpenCV and Pillow are used for:

Image processing
Video processing
Image loading
Visualization
Detection result handling
Embeddings

Document text can be represented as vectors called embeddings.

These representations allow semantic similarity comparison between:

User Query
     ↕
Document Chunks
FAISS

FAISS is used for vector similarity search.

It helps retrieve document chunks that are semantically related to the user's query.

Large Language Model

The LLM generates natural-language answers using the retrieved context and available information.

💾 Data Storage

VisionDesk AI maintains information related to processed scans.

Depending on the application configuration, stored information can include:

File name
Scan type
Detection information
Compliance status
Violations
Timestamp
Historical scan information

This data is used for:

Dashboard analytics
Scan history
Report generation
📊 Analytics

The application converts scan information into useful metrics.

Example:

                 Total Scans
                      │
             ┌────────┴────────┐
             ▼                 ▼
         Compliant        Non-Compliant
                                │
                    ┌───────────┼───────────┐
                    ▼           ▼           ▼
                 Helmet       Vest       Other
                Violation   Violation   Violations
🔐 Security

The project follows basic security practices:

API keys should be stored securely.
Secrets should never be committed to GitHub.
.venv should not be uploaded.
Private documents should not be uploaded publicly.
Sensitive information should be removed before publishing the repository.
🚫 Recommended .gitignore
# Virtual Environment
.venv/
venv/

# Python
__pycache__/
*.pyc
*.pyo

# Environment Variables
.env

# Streamlit Secrets
.streamlit/secrets.toml

# Databases
*.db
*.sqlite
*.sqlite3

# Generated Files
*.csv
*.log

# Temporary Files
temp/
tmp/

# IDE
.vscode/
.idea/

# Operating System
.DS_Store
Thumbs.db
🧪 Testing

The project can be tested module by module.

Vision Testing

Test:

YOLO model loading
Image upload
Object detection
Confidence scores
Compliance calculation
Document Testing

Test:

PDF processing
TXT processing
DOCX processing
Text extraction
Chunk generation
RAG Testing

Test:

Knowledge-base creation
Document retrieval
Similarity search
AI response generation
Dashboard Testing

Test:

Scan history
KPI calculations
Charts
Data tables
Reporting Testing

Test:

PDF generation
CSV generation
Summary creation
⚠️ Limitations
1. Model Dependency

Detection performance depends on the quality and training of the YOLO model.

2. Image Quality

Poor-quality images can affect detection performance.

3. Dataset Dependency

The model is limited to the classes it was trained to recognize.

4. LLM/API Dependency

AI-powered features may require an active API connection.

5. Local Deployment

The current project is primarily designed for local Streamlit execution.

6. Real-Time Monitoring

The current implementation is not a complete real-time industrial CCTV monitoring system.

🔮 Future Enhancements

Potential future improvements include:

👁️ Real-Time Monitoring
Live CCTV integration
Real-time PPE detection
Instant safety alerts
🤖 Advanced AI
Multi-agent architecture
Better contextual reasoning
Voice-based AI assistant
Multimodal AI
📊 Advanced Analytics
Predictive analytics
Risk prediction
Safety trend analysis
Advanced BI dashboards
☁️ Cloud Deployment
Cloud hosting
Scalable inference
Cloud database
Containerized deployment
👥 User Management
User authentication
Admin dashboard
Role-based access
Organization accounts
📧 Notifications
Email alerts
Automated safety notifications
Scheduled reports
Violation alerts
🌐 Multi-Language Support

Support for multiple Indian and international languages.

📚 Learning Outcomes

Through this project, the team gained practical experience in:

Programming
Python
Modular programming
File handling
Exception handling
Virtual environments
Computer Vision
Object detection
YOLO
Image processing
Video processing
Confidence scores
Generative AI
LLMs
Prompt engineering
RAG
Embeddings
Vector databases
AI Agents
Agent workflows
Context retrieval
LangGraph
AI-assisted decision workflows
Data Science
Pandas
Data processing
Analytics
Visualization
KPI generation
Software Development
Streamlit
Git
GitHub
Project architecture
Dependency management
Documentation

Project: AI-Powered Visual Data Analytics & Business Intelligence Platform

Project Name: VisionDesk AI

Domain:

Artificial Intelligence
Data Science
Computer Vision
Generative AI
Business Intelligence

Programming Language: Python

Framework: Streamlit

👥 Team Members

This project was developed collaboratively by:

#	Team Member
1	Pratishtha
2	Rithikashri
3	Nandini
4	Omair
5	Lavakush
6	Ritish

🏆 Project Highlights
✓ AI-Powered Platform
✓ Computer Vision
✓ YOLO-Based PPE Detection
✓ Image & Video Analysis
✓ Document Intelligence
✓ PDF/TXT/DOCX Processing
✓ Knowledge Base
✓ Vector Search
✓ Retrieval-Augmented Generation
✓ AI Agent
✓ LLM Integration
✓ Data Analytics
✓ Interactive Dashboard
✓ Scan History
✓ Automated Reports
✓ PDF Export
✓ CSV Export
✓ Streamlit Web Application
🔗 Repository

🙏 Acknowledgements

We would like to acknowledge the platforms, frameworks, and technologies used during the development of this project:

Infosys Springboard
Python
Streamlit
Ultralytics YOLO
OpenCV
Pillow
LangChain
LangGraph
FAISS
Google Gemini / LLM services
PyMuPDF
Pandas
FPDF
Git
GitHub

📜 Disclaimer

VisionDesk AI was developed for educational and internship purposes as part of the Infosys Springboard Internship.

The PPE detection results depend on factors such as:

Training data
Model performance
Image quality
Lighting conditions
Camera angle
Detection classes

Therefore, the system should not be considered a replacement for professional workplace safety inspections, certified safety equipment checks, or official safety procedures.

📄 License

This project was developed for educational and internship purposes.

If the repository is distributed as an open-source project, an appropriate license should be added based on the team's requirements and the licenses of the third-party libraries, datasets, and models used.

⭐ Conclusion

VisionDesk AI demonstrates how multiple Artificial Intelligence technologies can be integrated into one practical application.

The platform combines:

Computer Vision
       +
Document Intelligence
       +
Vector Search
       +
RAG
       +
AI Agents
       +
Data Analytics
       +
Business Intelligence
       +
Automated Reporting

into a unified platform.

The project demonstrates the complete journey from visual data analysis and PPE detection to intelligent information retrieval, AI-assisted analysis, dashboards, and automated reporting.

🚀 VisionDesk AI
Transforming Visual & Document Data into Intelligent Insights.

Built with Python • Streamlit • YOLO • RAG • AI Agents • Data Analytics
