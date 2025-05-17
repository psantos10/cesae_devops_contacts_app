# 📇 CESAE DevOps Contacts App

**Aplicação Demo de Suporte ao Curso DevOps - CESAE**

This repository hosts a demo application developed as part of the CESAE DevOps course. It serves as a practical example to illustrate DevOps principles, including containerization, CI/CD pipelines, and deployment strategies.

---

## 🚀 Project Overview

The CESAE DevOps Contacts App is a simple web application that allows users to manage a list of contacts. It is built using Python and Flask, with a focus on demonstrating DevOps practices such as:

- **Containerization**: Utilizing Docker for consistent development and deployment environments.
- **Continuous Integration/Continuous Deployment (CI/CD)**: Implementing automated testing and deployment pipelines.
- **Infrastructure as Code (IaC)**: Managing infrastructure through code for reproducibility and scalability.

---

## 🧰 Technologies Used

- **Python 3.x**: Core programming language.
- **Flask**: Lightweight web framework for Python.
- **Docker**: Containerization platform to package the application.
- **HTML/CSS**: Front-end structure and styling.
- **Git**: Version control system.
- **GitHub Actions**: CI/CD pipeline automation.

---

## 📁 Project Structure

```
cesae_devops_contacts_app/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── Dockerfile             # Docker image configuration
├── .dockerignore          # Files to exclude from Docker build
├── .gitignore             # Files to exclude from Git
├── templates/             # HTML templates
│   └── index.html         # Main page template
├── static/                # Static files (CSS, JS, images)
│   └── style.css          # Stylesheet
└── README.md              # Project documentation
```

---

## 🛠️ Installation and Setup

### Prerequisites

- Python 3.x installed on your machine.
- Docker installed and running.
- Git installed for version control.

### Clone the Repository

```bash
git clone https://github.com/brunocastromusic/cesae_devops_contacts_app.git
cd cesae_devops_contacts_app
```

### Running the Application Locally

#### Using Python

1. Create a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:

   ```bash
   python app.py
   ```

4. Access the application at `http://localhost:5000`.

#### Using Docker

1. Build the Docker image:

   ```bash
   docker build -t cesae_contacts_app .
   ```

2. Run the Docker container:

   ```bash
   docker run -d -p 5000:5000 cesae_contacts_app
   ```

3. Access the application at `http://localhost:5000`.

---

## ⚙️ CI/CD Pipeline

The project integrates GitHub Actions for automating the CI/CD pipeline. The workflow includes:

- **Linting**: Ensuring code quality and style consistency.
- **Testing**: Running unit tests to validate functionality.
- **Building Docker Image**: Creating a Docker image for the application.
- **Deployment**: Deploying the application to a staging or production environment.

*Note: The `.github/workflows/` directory contains the workflow configuration files.*

---

## 🧪 Testing

To run tests (if implemented), execute:

```bash
pytest
```

*Ensure that `pytest` is included in your `requirements.txt` and that test files are properly configured.*

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch:

   ```bash
   git checkout -b feature/your-feature-name
   ```

3. Make your changes and commit them:

   ```bash
   git commit -m "Add your message here"
   ```

4. Push to your forked repository:

   ```bash
   git push origin feature/your-feature-name
   ```

5. Open a pull request detailing your changes.

---

## 📬 Contact

For questions or suggestions, please contact [Bruno Castro](https://github.com/brunocastromusic).

---

## 📚 Acknowledgments

This project is a fork of [psantos10/cesae_devops_contacts_app](https://github.com/psantos10/cesae_devops_contacts_app). Special thanks to the original author for the foundational work.
