from typing import List, Tuple
import math

def search(
	query: List[float],
	candidates: List[Tuple[str, List[float]]],
) -> List[Tuple[str, float]]:
	factor = 1.0 / max(abs(x) for x in query)
	result = []

	for candidate in candidates:
		score = factor * cosine_similarity(query, candidate[1])

		# penality
		if (candidate[1][0] < 0):
			score = score/3.0

		result.append((candidate[0], score))

	result.sort(key=lambda candidate: candidate[1], reverse=True)
	return result

def cosine_similarity(v1, v2):
	dot_product = sum(x * y for x, y in zip(v1, v2))

	norm_v1 = math.sqrt(sum(x**2 for x in v1))
	norm_v2 = math.sqrt(sum(x**2 for x in v2))

	if norm_v1 == 0 or norm_v2 == 0:
		return 0.0

	return dot_product / (norm_v1 * norm_v2)
