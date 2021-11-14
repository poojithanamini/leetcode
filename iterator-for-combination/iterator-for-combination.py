class CombinationIterator(object):

	def __init__(self, characters, combinationLength):
		"""
		:type characters: str
		:type combinationLength: int
		"""
		characters_list = list(characters)
		self.characters_len = len(characters_list)
		self.combination_list = list()
		candidate_combination_list = list()
		combination_length = combinationLength
		self.combinations(characters_list, candidate_combination_list, combination_length, 0)
		self.idx = 0
		self.combinations_len = len(self.combination_list)

	def combinations(self, characters_list, candidate_combination_list, combination_length, start_idx):
		if len(candidate_combination_list) == combination_length:
			self.combination_list.append(''.join(candidate_combination_list))
			return
		for i in range(start_idx, self.characters_len):
			select_item = characters_list[i]
			candidate_combination_list.append(select_item)
			self.combinations(characters_list, candidate_combination_list, combination_length, i+1)
			candidate_combination_list.pop()   

	def next(self):
		"""
		:rtype: str
		"""
		next_item = self.combination_list[self.idx]
		self.idx += 1
		return next_item

	def hasNext(self):
		"""
		:rtype: bool
		"""
		return True if self.idx<self.combinations_len else False