import os

# Define the structure
structure = {
    "ddo-core": ["__init__.py", "agent.py", "domain.py", "tool.py", "README.md"],
    "ddo-runtime": [
        "__init__.py", "runtime.py", "README.md",
        ("memory", ["__init__.py", "vectorstore.py", "redis.py", "filecache.py"])
    ],
    "ddo-gov": ["__init__.py", "telemetry.py", "audit.py", "policy.py", "README.md"],
    "ddo-plugins": ["__init__.py", "openai_plugin.py", "watsonx_plugin.py", "search_plugin.py", "README.md"],
    "examples": [("finance_demo", []), ("healthcare_demo", []), "README.md"],
    "tests": ["test_core.py", "test_runtime.py", "test_plugins.py", "README.md"],
}

# Top-level files
root_files = [
    ".gitignore",
    "LICENSE",
    "README.md",
    "framework.md",
    "requirements.txt",
    "setup.py"
]

# Create directories and files
def create_structure():
    for folder, contents in structure.items():
        os.makedirs(folder, exist_ok=True)
        for item in contents:
            if isinstance(item, tuple):
                subfolder, subfiles = item
                subfolder_path = os.path.join(folder, subfolder)
                os.makedirs(subfolder_path, exist_ok=True)
                for f in subfiles:
                    open(os.path.join(subfolder_path, f), "a").close()
            else:
                open(os.path.join(folder, item), "a").close()

    for file in root_files:
        open(file, "a").close()

    print("✅ DDO project structure created successfully.")

if __name__ == "__main__":
    create_structure()

