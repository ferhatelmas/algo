class UserName:
    def newMember(self, existingNames, newName):
        if newName in existingNames:
            i = 1
            while "{}{}".format(newName, i) in existingNames:
                i += 1
            return newName + str(i)
        return newName
