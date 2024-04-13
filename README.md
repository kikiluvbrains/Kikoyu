# Kikoyu Image File Reviewer Application

The Kikoyu application is designed for processing image segmentation data from machine learning models. It offers a user-friendly interface for reviewing and validating image data, enhancing the accuracy and efficiency of machine learning workflows. This README provides detailed instructions on how to set up and build the application.

## Prerequisites

Before you start the setup process, ensure you meet the following requirements:

- Operating System: You are using a Unix/Linux/macOS or Windows operating system.
- Git: You have Git installed on your machine for cloning the repository.
- Python and pip: You have Python and pip installed, as the application and its dependencies are Python-based.

## Setup Instructions

To set up the Kikoyu application on your system, follow these steps:

1. **Clone the Git Repository**

   Begin by cloning the Kikoyu repository to your local machine. Open a terminal or command prompt and execute the following command:
   
   ```bash
   git clone git@github.com:kikiluvbrains/Kikoyu.git

2. **Navigate to the Project Directory**
   ```
   cd Kikoyu
   ```
4. **Install Dependencies**
   ```
   bash pip install -r requirements.txt
   ```

5. **Build the Application with PyInstaller**
   ```
   py -m PyInstaller --onedir Kikoyu_application.py```
   ```
## License

MIT License. Free to use.
