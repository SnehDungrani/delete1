# System Test Copilot

## Overview
This repository contains an ANTLR4 grammar project for defining the language for the "Aktion" column of the test catalog "Lenkradheizung". It is intended for use with IntelliJ IDEA's ANTLR plugin to preview and test the language grammar without any parser implementation.
This repository contains as well the data for the test catalogs and the project presentations.  
<ins>**Unauthorized publication, distribution or online use of any data of this repository without the explicit consent of (Volkswagen AG) is strictly prohibited!!!**</ins>

## Prerequisites
Ensure you have the following installed:
- [IntelliJ IDEA](https://www.jetbrains.com/idea/)
- [ANTLR4 Plugin for IntelliJ](https://plugins.jetbrains.com/plugin/7358-antlr-v4)

## Project Structure
```
project-root/
│── Data
│   ├── BASELINE_CODEBEAMER_LRH_V02.xls          # "Lenkradheizung" test catalog
│── Diagrams                                     # System diagrams and architecture
│── Presentations                                # Project related presentations
│── VW_Grammar_LRH                               # ANTLR4 project root
│   ├── .idea
│   ├── src
│   ├── .gitignore
│   ├── grammar_lrh.g4          # ANTLR4 grammar definition
│── lora                                         # LoRA model checkpoints and scripts
│   ├── lora_model_3b/
│   │   └── checkpoint-*/         # Model checkpoints (3b)
│   ├── lora_model_8b/
│   │   └── checkpoint-*/         # Model checkpoints (8b)
│   ├── final.lark                # Grammar file
│   ├── lora_finetune.ipynb       # LoRA fine-tuning notebook
│   ├── syncode_evaluation.ipynb  # Evaluation notebook
│   ├── train.csv/.xlsx           # Training data
│   └── validation.xlsx           # Validation data
│── README.md          # Project documentation
```

## Lora Folder

The `lora` directory contains resources for LoRA (Low-Rank Adaptation) model training and evaluation. It includes:
- Model checkpoint folders for different model sizes (3b, 8b)
- Training and validation datasets (CSV/XLSX)
- Jupyter notebooks for fine-tuning and evaluation
- Grammar and configuration files for LoRA experiments

Use these resources to train, fine-tune, and evaluate LoRA models for test automation or grammar-based tasks.

## Setup and Configuration
### 1. Install ANTLR4 Plugin in IntelliJ
- Go to `File` → `Settings` → `Plugins`
- Search for `ANTLR v4` and install it
- Restart IntelliJ IDEA

### 2. Open the Project File
- Start Intellij IDEA
- Open the file `VW_Grammar_LRH` with Intellij IDEA

### 3. Use the ANTLR Preview Feature to Test the Grammar
- Open `grammar_lrh.g4`
- Click on `ANTLR Preview` (found in the left panel or via `View` → `Tool Windows` → `ANTLR Preview`)
- Enter a sample input in the **Input** section
- Observe the **Parse Tree** visualization to verify the grammar behavior

## Modifying the Grammar
- Modify the `grammar_lrh.g4` file as needed, then save your changes to be able to test the new modifications.
- Use the ANTLR preview feature to test different language inputs
- Adjust rules to correctly parse the intended language structure

## Author
This project has been developed by Bassel Rafie from the Institute for Software and Systems Engineerung of TU Clausthal.

## License
**Unauthorized publication, distribution or online use of any data of this repository without the explicit consent of (Volkswagen AG) is strictly prohibited.**

---

# System Test Copilot UI

A Flask-based web application that provides an interactive interface for generating test automation steps. The application supports multiple AI models and maintains conversation history for different users.

## 🚀 Features

- Interactive web interface for test automation generation
- Support for multiple AI models (Llama, Gemma, DeepSeek, etc.)
- User management system with MongoDB integration
- Conversation history management
- Export functionality for chat logs and results
- Responsive design for desktop and mobile
- Real-time token counting and response metrics
- Multi-user support with separate chat histories
- AI service integration for model management and inference

## 📁 Project Structure

```
System_Test_Copilot_Ui/
├── ai_services.py        # AI model service and inference
├── mongo_crud.py         # MongoDB operations
├── token_counter.py      # Token counting utilities
├── syncode.py            # Test automation generation
├── final.lark            # Grammar file for parsing
├── requirements.txt      # Python dependencies
├── examples.xlsx         # Example test cases
│
├── static/               # Front-end assets
│   ├── css/
│   │   └── style.css     # Main stylesheet
│   ├── js/
│   │   ├── botResponse.js
│   │   ├── chat.js
│   │   ├── chatHistory.js
│   │   ├── userManagement.js
│   │   ├── userPrompt.js
│   │   ├── utility.js
│   │   └── modules/
│   │       └── chat/     # Chat-related modules
│   └── favicon.ico       # Website favicon
│
└── templates/
    └── index.html        # Main application template
```

## 🧑‍💻 Development Environment Setup

### 1. ✅ Prerequisites

- Python 3.13+
- [uv](https://docs.astral.sh/uv/) - Fast Python package manager
- MongoDB
- Modern web browser

### 2. 🔧 Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd system-test-copilot
```

2. Install uv (if not already installed):
```bash
# On macOS and Linux
curl -Ls https://astral.sh/uv/install.sh | bash

# On Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

3. Add uv to your PATH (if not already added):
```bash
# On macOS and Linux
setenv PATH "$HOME/.local/bin:$PATH"

# On Windows (add to system PATH or use in PowerShell)
$env:PATH += ";$env:USERPROFILE\.local\bin"
```

4. Install dependencies using uv:
```bash
uv sync
```

4. Set up environment variables in `.env`:
```env
MONGODB_URI=your_mongodb_connection_string
SAIA_API_KEY=your_api_key
SAIA_API_ENDPOINT=your_api_endpoint
HUGGING_FACE_HUB_TOKEN=your_hf_token
HF_CACHE=your_hf_cache_directory
SYNCODE_CACHE=your_syncode_cache_directory
```

### 3. 🚀 Running the Application

```bash
uv run python main.py
```

Access the application at:
```
http://localhost:5000
```

## 🛠️ Technologies Used

### Backend
- **Flask** - Web framework
- **PyMongo** - MongoDB driver
- **python-dotenv** - Environment management
- **requests** - HTTP client
- **tiktoken** - Token counting
- **huggingface-hub** - ML model integration
- **syncode** - AI model for test automation
- **transformers** - Hugging Face transformers
- **pandas** - Data processing
- **openpyxl** - Excel file handling
- **pydantic** - Data validation

### Frontend
- **HTML5/CSS3** - Structure and styling
- **JavaScript (ES6+)** - Client-side functionality
- **Bootstrap 5** - UI components
- **Font Awesome** - Icons

### Database
- **MongoDB** - NoSQL database

### Package Management
- **uv** - Fast Python package manager

## 📝 Usage

1. **User Management**
   - Click the "+" button to create a new user
   - Enter username when prompted
   - Select user from dropdown to switch accounts

2. **Chat Interface**
   - Select AI model from dropdown
   - Type your test requirement in the input box
   - Press Enter or click send button
   - View generated test automation steps

3. **History Management**
   - View past conversations in left sidebar
   - Click conversation to load
   - Use rename/delete buttons for management

4. **Export Options**
   - Export full chat history
   - Export last result only

5. **AI Model Management**
   - Configure model parameters in ai_services.py
   - Manage model loading and inference
   - Handle model responses and error cases

## 🔒 Security Notes

- Never commit `.env` file with sensitive credentials
- Keep API keys and tokens secure
- Use environment variables for sensitive data
- Secure MongoDB connection string
- Protect AI model access credentials

## 🐛 Troubleshooting

- Check MongoDB connection if conversations aren't saving
- Verify API keys in `.env` if models aren't responding
- Clear browser cache if UI isn't updating properly
- Check AI service logs for model inference issues
- Verify model configuration in ai_services.py
- Ensure uv is properly installed and in PATH
- Check Python version compatibility (requires 3.13+)

## 📦 Package Management

This project uses [uv](https://docs.astral.sh/uv/) for fast Python package management:

- **Install dependencies**: `uv sync`
- **Add new dependency**: `uv add package-name`
- **Run scripts**: `uv run python script.py`
- **Activate environment**: `uv shell`
- **Update dependencies**: `uv sync --upgrade`
