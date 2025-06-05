# agile-sustainability

## Overview
This repository contains an interactive quiz application designed to help companies determine the best integration form for embedding sustainability into their Scaled Agile Framework (SAFe). The quiz is part of an article discussing the "Twin Transition"—the simultaneous transformation towards greater sustainability and digitalization.

## Installation
This project uses `uv` as the package manager and `venv` for virtual environment management. Follow the steps below to set up the project:

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd agile-sustainability
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. Install dependencies using `uv`:
   ```bash
   uv install
   ```

## Running the Application
To start the quiz application, run the following command:
```bash
streamlit run app.py
```

This will launch the application in your default web browser.

## License
This project is licensed under the terms of the MIT license. See the `LICENSE` file for details.