from protorpc import messages

class StringMessage(messages.Message):
  value = messages.StringField(1, required = True)
  
