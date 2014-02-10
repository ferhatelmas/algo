class TheQuestionsAndAnswersDivTwo:
    def find(self, questions):
        return 2 ** len(set(questions))
