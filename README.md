# Learniverse

## Table of Contents
- [Project Overview](#project-overview)
- [Problem Statement](#problem-statement)
- [Solution Overview](#solution-overview)
- [Target Audience & Impact](#target-audience--impact)
- [Key Features](#key-features)
- [Technologies Used](#technologies-used)
- [Project Setup](#project-setup)
  - [Running the AR Project](#running-the-ar-project)
  - [Running the VR Project](#running-the-vr-project)
- [Developers](#developers)
- [Future Development](#future-development)

## Project Overview

Welcome to **Learniverse**, an innovative web platform integrating Augmented Reality (AR) and Virtual Reality (VR) technologies. Our platform aims to revolutionize education by providing immersive and interactive learning experiences targeted at school children from kindergarten to 10th grade.

## Problem Statement

Traditional education methods often fail to fully engage students and cater to diverse learning styles. This project aims to overcome these limitations by using AR and VR to provide immersive learning experiences.

## Solution Overview

Learniverse offers school students a hands-on approach to learning with AR-based interactive 3D models, VR simulations for exploring complex topics, and gamified quizzes to enhance engagement and retention.

## Target Audience & Impact

This project is designed for school students of all levels. By integrating immersive technologies, it transforms learning into an interactive, fun experience, especially beneficial for visual and kinesthetic learners, and supports inclusive learning for students with special needs.

## Key Features

1. **Landing Page with User Login and Email Notification System**
   - Introduction to our site
   - Secure user authentication
   - Email-based notifications

2. **Learning Section**
   - **AR Learning**: Interactive 3D models (10+ models developed using JavaScript, React, and Three.js)
   - **VR Learning**: Explorable human body systems (Skeletal, Muscular, and Circulatory) developed using Unity and open-source models
   - **Assessment**: Engaging educational quizzes

## Technologies Used

- **Frontend**: HTML, CSS, JavaScript, React
- **Backend**: Django
- **VR Development**: Unity 3D Engine, Unity XR Interaction Toolkit, SketchFab for assets
- **AR Development**: Three.js, React

## Documentation

For detailed information about the project, please refer to our comprehensive documentation:

[Learniverse Documentation](https://drive.google.com/file/d/1Nvdd4nTZDWvN9cqkKEKy6nejGLZfFh7I/view)

## Demo Video

Watch our demo video to see Learniverse in action and understand how it can revolutionize the learning experience:

[Learniverse Demo Video](https://www.youtube.com/watch?v=Lg-R_b08B84)


## Project Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/SanaSultana1234/VedaVerseHackathon.git
   cd VedaVerseHackathon
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Make and apply migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Run the development server:
   ```bash
   python manage.py runserver
   ```

### Running the AR Project

1. Install dependencies:
   ```bash
   npm install
   ```

2. Start the development server:
   ```bash
   npm start
   ```
   Open http://localhost:3000 in your browser.

### Running the VR Project

1. Open the VR project in Unity:
   - Use Unity Hub to add the project directory
   - Ensure all required packages are installed

2. Run the scene:
   - Open the MainVR scene and click Play in the Unity Editor

3. Build and deploy:
   - Go to File > Build Settings
   - Select Oculus as the target platform
   - Click Build and Run

## Developers

- [Sana Sultana](https://www.linkedin.com/in/sanasultana004/)
- [G. Pravalika](https://www.linkedin.com/in/pravalika-g/)
- [D. Varsha](https://www.linkedin.com/in/varsha-dumpala-a83652251/)
- [T. Sreeja](https://www.linkedin.com/in/sreeja-t-283620229/)

## Future Development

- Implement additional AR and VR models
- Optimize the platform for better performance
- Expand gamification features to increase engagement
- Enhance overall user experience and accessibility

