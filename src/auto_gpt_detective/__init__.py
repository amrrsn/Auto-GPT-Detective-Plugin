"""This is a template for Auto-GPT plugins."""
import os
from typing import Any, Dict, List, Optional, Tuple, TypeVar, TypedDict
from auto_gpt_plugin_template import AutoGPTPluginTemplate

PromptGenerator = TypeVar("PromptGenerator")


class Message(TypedDict):
    role: str
    content: str


class AutoGPTDetective(AutoGPTPluginTemplate):
    """
    Detect AI generated text.
    """

    def __init__(self):
        super().__init__()
        self._name = "Auto-GPT-Detective-Plugin"
        self._version = "0.0.2"
        self._description = "Detect AI generated text."
        self.load_sapling = (
                os.getenv("DETECTIVE_ENGINE").lower() == "saplingai"
                and os.getenv("SAPLINGAI_API_KEY")
        )

        if self.load_sapling is None:
            print("Warning: Detective Engine not set!")

    def can_handle_post_prompt(self) -> bool:
        return True

    def post_prompt(self, prompt: PromptGenerator) -> PromptGenerator:
        if self.load_sapling:
            from .sapling_ai import _sapling_detect

            prompt.add_command(
                "sapling_detect",
                "Detect AI Generated Text",
                {"text": "<text>"},
                _sapling_detect,
            )
        else:
            print(
                "Warning: Detective Engine not loaded. "
                "Please set DETECTIVE_ENGINE and the "
                "appropriate API key environment variables. "
                "(SAPLINGAI_API_KEY)"
            )

        return prompt

    def can_handle_pre_command(self) -> bool:
        return True

    def pre_command(
            self, command_name: str, arguments: Dict[str, Any]
    ) -> Tuple[str, Dict[str, Any]]:
        if command_name == "detect_ai" and self.load_sapling:
            return "sapling_detect", arguments
        else:
            return command_name, arguments

    def can_handle_post_command(self) -> bool:
        return False

    def post_command(self, command_name: str, response: str) -> str:
        pass

    def can_handle_on_planning(self) -> bool:
        return False

    def on_planning(
            self, prompt: PromptGenerator, messages: List[Message]
    ) -> Optional[str]:
        pass

    def can_handle_on_response(self) -> bool:
        return False

    def on_response(self, response: str, *args, **kwargs) -> str:
        pass

    def can_handle_post_planning(self) -> bool:
        return False

    def post_planning(self, response: str) -> str:
        pass

    def can_handle_pre_instruction(self) -> bool:
        return False

    def pre_instruction(self, messages: List[Message]) -> List[Message]:
        pass

    def can_handle_on_instruction(self) -> bool:
        return False

    def on_instruction(self, messages: List[Message]) -> Optional[str]:
        pass

    def can_handle_post_instruction(self) -> bool:
        return False

    def post_instruction(self, response: str) -> str:
        pass

    def can_handle_chat_completion(
            self, messages: Dict[Any, Any], model: str,
            temperature: float, max_tokens: int
    ) -> bool:
        return False

    def handle_chat_completion(
            self, messages: List[Message], model: str,
            temperature: float, max_tokens: int
    ) -> str:
        pass
