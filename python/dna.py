
gender = {"female": "TGAAGGACCTTC", "male": "TGCAGGAACTTC"}
race = {"white": "AAAACCTCA", "black": "CGACTACAG",  "asian": "CGCGGGCCG"}
hair = {"black": "CCAGCAATCGC", "brown": "GCCAGTGCCG", "blonde": "TTAGCTATCGC"}
eye = {"blue": "TTGTGGTGGC", "green" : "GGGAGGTGGC", "brown": "AAGTAGTGAC"}
face = {"square": "GCCACGG", "round" : "ACCACAA", "oval": "AGGCCTCA"}



people = {"eva" : ["female", "white", "blonde", "blue", "oval"],
          "larisa" : ["female", "white", "brown", "brown", "oval"],
          "matej" : ["male", "white", "black", "blue", "oval"],
          "miha" : ["male", "white", "brown", "green", "square"]}

dna = "ACAAGATGCCATTGTCCCCCGGCCTCCTGCTGCTGCTGCTCTCCGGGGCCACGGCCACCGCTGCCCTGCCCCTGGAGGGTGGCCCCACCGGCCGAGACAGCGAGCATATGCAGGAAGCGGCAGGAATAAGGAAAAGCAGCCTCCTGACTTTCCTCGCTTGGTGGTTTGAGTGGACCTCCCAGGCCAGTGCCGGGCCCCTCATAGGAGAGGAAGCTCGGGAGGTGGCCAGGCGGCAGGAAGGCGCACCCCCCCAGCAATCCGCGCGCCGGGACAGAATGCCCTGCAGGAACTTCTTCTGGAAGACCTTCTCCTCCTGCAAATAAAACCTCACCCATGAATGCTCACGCAAGTTTAATTACAGACCTGAA"

person = []

for i in gender:
    if gender[i] in dna:
        print(i)
        person.append(i)
for i in race:
    if race[i] in dna:
        print(i)
        person.append(i)
for i in hair:
    if hair[i] in dna:
        print(i)
        person.append(i)
for i in eye:
    if eye[i] in dna:
        print(i)
        person.append(i)
for i in face:
    if face[i] in dna:
        print(i)
        person.append(i)

for p in people:
    if people[p] == person:
        print("The criminal is %s" % p.capitalize())
        break