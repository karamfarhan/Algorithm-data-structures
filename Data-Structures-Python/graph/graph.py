class graf:
	def __init__ (self,dates):
		self.dates = dates
		self.graf_dic = {}
		
		for i,j in self.dates:
			if i in self.graf_dic:
				self.graf_dic[i].append(j)
			else:
				self.graf_dic[i] = [j]
				
				
	def print(self):
		print (self.graf_dic)
	
	
	def add_node(self,node):
			if node[0] in self.graf_dic:
				self.graf_dic[node[0]].append(node[1])
			else:
				self.graf_dic[node[0]] = [node[1]]
		
	
	
	
	

