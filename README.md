# ClassPY 🎓

**ClassPY** is a CLI-based student management system built in Python, designed to reinforce fundamental backend development skills through practical application. The project covers core concepts such as layered architecture, database integration, and service-oriented design.

---

## 📋 Table of Contents

- [ClassPY 🎓](#classpy-)
  - [📋 Table of Contents](#-table-of-contents)
  - [About](#about)
  - [Features](#features)
  - [Tech Stack](#tech-stack)
  - [Project Structure](#project-structure)
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
  - [Usage](#usage)
  - [Contributing](#contributing)
  - [Author](#author)

---

## About

ClassPY was built as a hands-on learning project to consolidate Python knowledge through a real-world-style application. It implements a clean separation of concerns across CLI, service, repository, and database layers — mirroring patterns found in production systems.

---

## Features

- 👤 Student (Aluno) registration and management
- 📝 Grade (Nota) tracking per student
- 🔐 User authentication and login
- 🗂️ Data persistence via SQLite
- 🖥️ Command-line interface for all operations

---

## Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.x |
| Database | SQLite (via `sqlite3`) |
| Interface | CLI (Command Line Interface) |
| Architecture | Repository + Service Pattern |

---

## Project Structure

```
ClassPY/
├── app/
│   ├── cli/                  # CLI entry points and command handlers
│   │   └── main.py
│   ├── database/             # Database connection and setup
│   │   ├── connection.py
│   │   └── setup.py
│   ├── repositories/         # Data access layer (CRUD operations)
│   │   ├── aluno_repository.py
│   │   ├── login_repository.py
│   │   ├── nota_repository.py
│   │   └── users_repository.py
│   ├── services/             # Business logic layer
│   │   ├── aluno_service.py
│   │   ├── login_service.py
│   │   ├── nota_service.py
│   │   └── users_service.py
│   └── __init__.py
├── data/                     # SQLite database file (auto-generated)
├── .gitignore
├── requirements.txt
└── README.md
```

---

## Getting Started

### Prerequisites

- Python 3.8+
- pip

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/PedroMarqus/ClassPY.git
   cd ClassPY
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv .venv

   # Linux / macOS
   source .venv/bin/activate

   # Windows
   .venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```bash
   python app/cli/main.py
   ```

> The SQLite database will be created automatically in the `data/` directory on first run.

---

## Usage

After starting the application, you will be presented with a CLI menu. Available operations include:

- Register and manage students
- Assign and view grades
- Manage users and authentication

---

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

1. Fork the project
2. Create your feature branch: `git checkout -b feature/my-feature`
3. Commit your changes: `git commit -m 'Add my feature'`
4. Push to the branch: `git push origin feature/my-feature`
5. Open a Pull Request

---

## Author

Made with 🐍 by [PedroMarqus](https://github.com/PedroMarqus)