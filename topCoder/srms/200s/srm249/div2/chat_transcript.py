class ChatTranscript:
    def howMany(self, transcript, name):
        return len(filter(lambda l: l.startswith(name + ':'), transcript))
