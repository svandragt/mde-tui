"""
A simple markdown renderer using Rich library for terminal output.
"""

from textual.app import App, ComposeResult
from textual.containers import Horizontal
from textual.widgets import MarkdownViewer, Footer, TextArea, Log
from textual.binding import Binding
import asyncio


class MarkdownTui(App):
    CSS = """
    Horizontal {
        height: 100%;
    }
    #editor, #preview {
        width: 1fr;
        height: 100%;
        border: solid green;
    }
    """
    _update_task = None
    BINDINGS = [
        Binding("f5", "toggle_preview", "Preview"),
    ]

    def compose(self) -> ComposeResult:
        with Horizontal():
            yield TextArea(id="editor")
            yield MarkdownViewer(id="preview", show_table_of_contents=False)
        yield Footer()

    def action_toggle_preview(self) -> None:
        editor = self.query_one("#editor", TextArea)
        viewer = self.query_one("#preview", MarkdownViewer)
        # Textual's MarkdownViewer doesn't provide `update`.
        # Assign the markdown content to the `markdown` attribute instead.
        viewer.document.update(editor.text)

    async def debounce_update(self) -> None:
        await asyncio.sleep(0.2)
        self.action_toggle_preview()

    def on_text_area_changed(self, event: TextArea.Changed) -> None:
        if self._update_task:
            self._update_task.cancel()
        self._update_task = asyncio.create_task(self.debounce_update())


if __name__ == "__main__":
    print('start')
    app = MarkdownTui()
    app.run()
    print('started')

# TODO list items aren't rendered!