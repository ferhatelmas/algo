class SRMRoomAssignmentPhase:
    def countCompetitors(self, ratings, K):
        return sum(i > ratings[0] for i in ratings[1:]) // K
