import subprocess
from pathlib import Path

MODEL = "openai/deepseek-ai/deepseek-v4-pro"


FILES = [
    "site/index.html",
    "site/services.html",
    "site/blog.html",
    "site/faq.html",
    "site/about.html",
    "site/contact.html",
    "site/assets/css/style.css",
    "site/assets/js/main.js",
    "site/sitemap.xml",
    "site/robots.txt",
    "site/templates/state-template.html",
    "site/templates/county-template.html",
    "site/templates/city-template.html",
    "site/docs/architecture.md",
]

for prompt_file in sorted(Path("prompts").glob("*.md")):
    print(f"Running {prompt_file.name}")
    subprocess.run(
        [
            "aider",
            "--yes",
            "--model",
            MODEL,
            *FILES,
            "--message",
            prompt_file.read_text()
        ],
        check=True
    )
