# PyQt6 Example Project

This is a simple PyQt6 example project that creates a GUI with buttons to interact with. The project uses Python's `virtualenv` to manage dependencies and is set up with a `requirements.txt` file.

## Prerequisites

Ensure that you have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

## Setup Instructions

1. **Clone the repository**

   - With SSH:
     ```bash
     git clone git@github.com:8408323/python-qt-test.git
     ```

   - With HTTPS:
     ```bash
     git clone https://github.com/8408323/python-qt-test.git
     ```

2. **Create and activate a virtual environment:**

   - On **Windows**:
     ```bash
     python -m venv .venv
     .venv\Scripts\activate
     ```

   - On **macOS/Linux**:
     ```bash
     python -m venv .venv
     source .venv/bin/activate
     ```

3. **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the PyQt6 application:**
    ```bash
    python main.py
    ```

    This will launch a GUI with buttons to interact with.

## Files in the Project

```
/python-qt-test
    ├── main.py            # Entry point of the application
    ├── view.py            # View (MainView) definition
    ├── presenter.py       # Presenter (MainPresenter) definition
    ├── model.py           # Model (DataModel) definition
    ├── README.md          # This setup guide.
    ├── requirements.txt   # Lists the required Python dependencies (PyQt6).
```

## Deactivating the Virtual Environment

After you're done, you can deactivate the virtual environment by running:
```bash
deactivate
