import pytest
from main import on_click
def test_on_click_currencies():
    message = MockMessage("Курсы валют")
    result = on_click(message)
    assert result == "Expected result for currencies"

def test_on_click_news():
    message = MockMessage("Получать новости")
    result = on_click(message)
    assert result == "Expected result for news"

# Define a MockMessage class to simulate the message object
class MockMessage:
    def __init__(self, text):
        self.text = text
        self.chat = MockChat()

class MockChat:
    def __init__(self):
        self.id = 403846704

if __name__ == "__main__":
    pytest.main()