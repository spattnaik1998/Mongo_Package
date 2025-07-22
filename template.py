import os
from pathlib import Path
import logging

package_name = "mongodb_connect"

list_of_files = [
    ".github/workflows/ci.yml",
    "src/__init__.py",
    f"src/{package_name}/__init__.py",
    f"src/{package_name}/mongo_crud.py",
    "tests/__init__.py",
    "tests/unit/__init__.py",
    "tests/unit/unit.py",
    "tests/integration/__init__.py",
    "tests/integration/int.py"
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",
    "experiments/experiments.ipynb"
]

for filepath in list_of_files:
    # Create directories if they do not exist
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Created directory: {filedir} for file {filename}") 
    
    # Create the file if it does not exist
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass  # Just create an empty file