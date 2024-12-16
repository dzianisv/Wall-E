# test_llm.py
import pytest
from unittest.mock import patch, MagicMock
from llm import LLM

@pytest.fixture
def llm_instance():
    return LLM(user_id="test_user")

def test_ask_weather(llm_instance):
    with patch.object(llm_instance.llm, 'invoke', return_value={'output': 'It is sunny today.'}):
        response = llm_instance.ask("What is the weather like?")
        print(response)
        assert len(response) > 0

def test_ask_fedfundrate(llm_instance):
    with patch.object(llm_instance.llm, 'invoke', return_value={'output': 'The current federal funds rate is 0.25%.'}):
        response = llm_instance.ask("What is the current federal funds rate?")
        print(response)
        assert len(response) > 0

def test_ask_youtube_context(llm_instance):
    youtube_url = "https://www.youtube.com/watch?v=uT0kHewjzkE"
    with patch.object(llm_instance.llm, 'invoke', return_value={'output': 'This video discusses the latest trends in technology.'}):
        response = llm_instance.ask(f"What is the context of the YouTube video {youtube_url}?")
        print(response)
        assert len(response) > 0