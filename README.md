# VedaVerseHackathon

## Project Learniverse

Welcome to **Learniverse**, an innovative web platform integrating two prime XR technologies: Augmented Reality (AR) and Virtual Reality (VR). Our platform aims to revolutionize education by providing immersive and interactive learning experiences targeted at school children from kindergarten to class 10th.

## Documentation
[Documentation](insert-link-here)

## Problem Statement
Traditional education methods often fail to fully engage students and cater to diverse learning styles. This project aims to overcome these limitations by using AR and VR to provide immersive learning experiences.

## Solution Overview
Learniverse offers school students a hands-on approach to learning with AR-based interactive 3D models, VR simulations for exploring complex topics, and gamified quizzes to enhance engagement and retention.

## Target Audience & Impact
This project is designed for school students of all levels. By integrating immersive technologies, it transforms learning into an interactive, fun experience, especially beneficial for visual and kinesthetic learners, and supports inclusive learning for students with special needs.


### Key Features:

1. **Landing Page with User Login and Email Notification System**:
   - Intro to our site, Secure user authentication, and email-based notifications.


2. **Learning Section**:
   - **AR Learning**: Interactive 3D models (10+ models developed using JavaScript, React, and Three.js). Enter the input as text or speech, e.g. Earth. This will give the 3D Model of that particular text where children can interact with it, listen to it, and explore more. The 3D model is developed using Three.js hence making learning fun for children.
   - **VR Learning**: Explorable human body systems, namely the Skeletal, Muscular, and Circulatory systems developed using Unity and open-source models. Wear the VR headset and dive into the world of human anatomy to explore the various organs and their functionality. Information is provided in text as well as speech format. The organs can be grabbed, rotated, moved, and isolated to explore more. It also includes the assembly and reassembly of the various systems included.
   - **Assessment**: Engaging educational quizzes that make learning fun. It incorporates the questions related to the information provided in the hands-on AR and VR experiences to solidify the knowledge gained by children.

## Technologies Used

- **Frontend**: HTML, CSS, JavaScript, React
- **Backend**: Django
- **VR Development**: Unity 3D Engine, Unity XR Interaction Toolkit, SketchFab for assets
- **AR Development**: Three.js, React

## Project Setup

Follow these steps to set up the project locally:

1. **Clone the Repository**:
   
   ```bash
   git clone https://github.com/SanaSultana1234/VedaVerseHackathon.git
   cd VedaVerseHackathon
2. **Create a Virtual Environment**:

    ```bash
    python -m venv venv

3. **Create a Virtual Environment**:
  For Windows:

    ```bash
    venv\Scripts\activate
  For macOS/Linux:
  
    ```bash
    source venv/bin/activate
 4. **Install Dependencies**:

    ```bash
    pip install -r requirements.txt
Running the Project
5. **Make Migrations**:

    ```bash
    python manage.py makemigrations
6. **Apply Migrations**:

     ```bash
    python manage.py migrate
7. **Run the Development Server**:
   
      ```bash
      python manage.py runserver


### Running the AR Project

In the project directory, you can run the following commands:

1. **Install Dependencies**:
   ```bash
   npm install
2.  **Run the App in Development Mode**:

    ```bash
    npm start
This will start the app in development mode. You can open http://localhost:3000 to view it in your browser.


### Running the VR Project

1. **Open the VR Project in Unity**:

Open Unity Hub, click on Add, and select the directory where the VR project is located within the repository.
Resolve Any Dependencies:

Unity will automatically resolve dependencies on project startup. Ensure all required packages (e.g., XR Interaction Toolkit, TextMesh Pro) are installed.
Run the Scene:

Open the MainVR scene and click Play in the Unity Editor to test the VR environment.

2 **Build and Deploy**:

To build the project for VR headsets, go to File > Build Settings, select the target platform as Oculus, and click Build and Run.

Developers
Developer 1: [Sana Sultana](https://www.linkedin.com/in/sanasultana004/)
Developer 2: [G. Pravalika](https://www.linkedin.com/in/pravalika-g/)
Developer 3: [D. Varsha](https://www.linkedin.com/in/varsha-dumpala-a83652251/)
Developer 4: [T. Sreeja](https://www.linkedin.com/in/sreeja-t-283620229/)



Future Development:
Implementing additional AR and VR models.
Optimizing the platform for better performance.
Expanding gamification features to increase engagement.
Enhancing overall user experience and accessibility.

