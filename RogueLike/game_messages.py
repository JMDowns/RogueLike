import textwrap

class Message:
    def __init__(self, text, color=(255,255,255)):
        self.text = text
        self.color = color

class MessageLog:
    def __init__(self, x, width, height):
        self.messages = []
        self.x = x
        self.width = width
        self.height = height

    def add_message(self, message):
        # Split the message if necessary, over multiple lines
        new_msg_lines = textwrap.wrap(message.text, self.width)

        for line in new_msg_lines:
            # If the buffer is full, remove first line to make room for new one
            if len(self.messages) == self.height:
                del self.messages[0]

            #Add new line as Message object, with text and color
            self.messages.append(Message(line, message.color))
