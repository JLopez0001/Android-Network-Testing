# YouTube Network Condition Testing

This repository contains automated tests to verify the behavior of the YouTube app under various network conditions using Appium and Selenium.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the Tests](#running-the-tests)
- [Project Structure](#project-structure)

## Prerequisites

Before you begin, ensure you have met the following requirements:

- You have installed [Python 3.12.2](https://www.python.org/downloads/release/python-3122/)
- You have installed [Node.js](https://nodejs.org/) and npm
- You have installed [Appium](http://appium.io/) and started the Appium server
- You have a connected Android device or emulator

## Installation

1. **Clone the repository:**

    ```bash
    git clone git@github.com:JLopez0001/Gattaca-Take-Home.git
    cd Gattaca-Take-Home / tests / 
    ```

3. **Install Node.js dependencies:**

    ```bash
    npm install
    ```
Go into your virtual environment ei pipshell env

4. **Install Python dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

5. **Install Appium globally, appium/doctor, and install uiautomator2:**

    ```bash
    npm install -g @appium/doctor        

    appium driver install uiautomator2     
    ```

6. **Install the Appium Python Client:**

    ```bash
    pip install Appium-Python-Client selenium  
    ```

7. **Install Pytest:**  
    ```bash
    pip install pytest
    ```

## Running the Tests

Open terminal and cd into into Gattaca-Take-Home and run the command to run appium server

```bash
cd Gattaca-Take-Home
appium --config appiumrc.json 
```


To run the tests, open another terminal and execute the following command:

```bash
  cd Gattaca-Take-Home/tests 
```
```bash
  python3 test_network_conditions.py
```


# Backend / Frontend Setup
This project features a straightforward frontend and backend setup designed to identify the connected phone.

Future enhancements include:

* Connecting a phone and retrieving the serializer.
* Automating all tests with a single click.
* Incorporating OpenAI for advanced automated testing.
* These improvements aim to streamline the testing process and enhance efficiency.

## Table of Contents

- [Backend](#backend-prerequisites)
    - [Backend Installation](#backend-installation)
    - [Backend Run Server](#backend-running-server)

- [Frontend](#frontend-prerequisites)
    - [Frontend Installation](#frontend-installation)
    - [Frontend Run Server](#frontend-running-server)

## Backend-Prerequisites
Before you begin, ensure you have met the following requirements:

- You have installed [Node.js](https://nodejs.org/) and npm

## Backend-Installation
Open new terminal for backend
1. **CD into Backend Folder:**

    ```bash
    cd Backend
    ```

3. **Initialize node:**

    ```bash
    npm init
    ```


4. **Install dependencies:**

    ```bash
    npm i express usb-detection socket.io url path http 
    ```

## Backend-Running-Server
**Run Server:**
```
 npm i express usb-detection socket.io url path http
```

## Frontend-Prerequisites
- You have installed [Node.js](https://nodejs.org/) and npm

## Frontend-Installation
Open new terminal for Frontend
1. **CD into Frontend Folder and go into AndroidECT:**

```
cd Frontend/AndroidECT
```

2. **Initialized Node**
```
npm i -y
```

## Frontend-Running-Server
```
npm run dev
```


