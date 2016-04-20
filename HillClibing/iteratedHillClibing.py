from hillClibing import HillClibing

class IteratedHillClibing():
	"""docstring for IteratedHillClibing"""

	result_list = list()

	def __init__(self, n_turns, hillClibing):
		self.max_turns   = n_turns
		self.hillClibing = hillClibing
		
	def run(self):
		best_result = self.hillClibing.run()
		turn = 1

		while turn < self.max_turns:
			candidate_result = self.hillClibing.run()
			turn += 1
			
			if best_result[2] < candidate_result[2]:
				best_result = candidate_result

		self.result_list.append((best_result[1], best_result[2]))
		return best_result


			