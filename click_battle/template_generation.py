from jinja2.nativetypes import NativeEnvironment
from pathlib import Path

TEMPLATES = Path(__file__).parent.parent / "templates"


def generate_main_page(left, right):
    index = TEMPLATES / "index.html"
    content = index.read_text()
    env = NativeEnvironment()
    t = env.from_string(content)

    return t.render(left_score=left, right_score=right)
