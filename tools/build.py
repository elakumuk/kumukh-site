"""Builds index.html from src.html, inlining the wordmark (CSS masks need same-origin images)."""
import base64, os
here = os.path.join(os.path.dirname(__file__), "..")
b = base64.b64encode(open(os.path.join(here, "assets/wordmark.png"), "rb").read()).decode()
s = open(os.path.join(here, "src.html")).read().replace("__WM__", "data:image/png;base64," + b)
open(os.path.join(here, "index.html"), "w").write(s); print("built index.html")
