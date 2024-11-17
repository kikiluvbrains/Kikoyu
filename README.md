# Kikoyu Image File Reviewer
The Kikoyu application is designed for processing image segmentation data from machine learning models. It offers a user-friendly interface for reviewing and validating image data, enhancing the accuracy and efficiency of machine learning workflows. This README provides detailed instructions on how to set up and build the application.

![Screenshot from 2024-11-17 02-47-43](https://github.com/user-attachments/assets/05aa7426-8654-4056-a4a7-e935442a9975)
![Screenshot from 2024-11-17 02-46-22](https://github.com/user-attachments/assets/7dd41268-859b-4ac6-aeb1-a6c1d5231bdd)
![Screenshot from 2024-11-17 02-46-34](https://github.com/user-attachments/assets/ec085f61-4c87-4bb8-9755-b3b1406b45e1)

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
   py -m PyInstaller --onedir Kikoyu_application.py
   ```

6. **Navigate to location of application**
   ``` Open "Kikoyu_application" by double-clicking on it```
   
   ![image](https://github.com/kikiluvbrains/Kikoyu/assets/121206270/9abae367-1ec3-4272-8c15-65b81f401e94)

## License

MIT License. Free to use.
