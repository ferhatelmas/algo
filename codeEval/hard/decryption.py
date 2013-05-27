from string import ascii_uppercase as alphabet
message = "012222 1114142503 0313012513 03141418192102 0113 2419182119021713 06131715070119"
key = "BHISOECRTMGWYVALUZDNFJKPQX"

decrypted, m = [], ""
for l in message:
  if l == " ":
    decrypted.append(l)
  elif m == "":
    m = l
  else:
    decrypted.append(alphabet[key.index(alphabet[int(m+l)])])
    m = ""
print "".join(decrypted)