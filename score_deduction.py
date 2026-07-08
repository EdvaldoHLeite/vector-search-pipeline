from pipeline import cosine_similarity

query = [0.312209, -0.220883, -0.541543, -0.310608, -0.681168]
vectors = [
	[-0.356586, -0.612822, -0.58462, -0.254122, -0.301558],
	[-0.381331, 0.577147, -0.189148, -0.363327, 0.59473],
	[-0.548951, 0.641553, 0.235364, 0.436778, 0.202216]
]
scores = [
	0.305834,
	-0.213537,
	-0.349383
]

for i in range(len(vectors)):
	vector = vectors[i]
	score = scores[i]
	factor = 1.0 / max(abs(x) for x in query)

	cosine = cosine_similarity(query, vector)
	print (factor * cosine/3.0)


