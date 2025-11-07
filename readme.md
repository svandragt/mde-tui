# mde-tui

A small terminal markdown editor + preview built with Textual and Rich.

Quick, minimal TUI for editing Markdown in the terminal and seeing a live preview.

---

## Requirements

- Python 3.13.0
- uv package manager (project uses `uv` for dependency management)

---

## Installation

1. Install dependencies using uv. If the project already has a lockfile (`uv.lock`) / `pyproject.toml`, you can install the pinned dependencies. If you need to add packages locally:

```shell script
# If dependencies are already listed and you want to install from pyproject/lock:
   uv install
```


---

## Usage

Run the application from the project root:

```shell script
uv run markdown-tui.py
```


Controls:

- F5 —  Toggle / refresh the preview (bound to the "Preview" action).

The app shows a split layout with:
- left: a text editor area for writing Markdown
- right: a Markdown preview pane

The preview updates automatically after brief debounce when typing.

---

## Development notes

- File: `markdown-tui.py` is the main entrypoint.
- The app uses Textual's `TextArea` and `MarkdownViewer`.
- Debounced updates are used to avoid too-frequent re-renders.

Known / TODO:
- Task list items (e.g., `- [ ] item`) are currently not rendered by the preview — TODO in the code to address this.
- The project is minimal and intended as a starting point; feel free to improve rendering, keyboard bindings, layout, and save/load behavior.

---

## Contributing

- Open an issue describing the change or bug.
- For code changes, create a branch, make changes, and open a pull request.
- Keep changes small and focused; add tests or brief manual test instructions when applicable.

---

## Troubleshooting

- If the preview does not update, try pressing F5 to force a refresh.
- If package installation fails, ensure you have Python 3.13 and `uv` available on PATH.
