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
		
	
	
	
	def get_paths(self,start,end,path=[]):
		path = path + [start]
		if start == end :
			return path
		if start not in self.graf_dic:
			return []
		paths = []
		for node in self.graf_dic[start]:
			if node not in path:
				n = self.get_paths(node,end,path)
				for ns in n:
					paths.append(ns)
					#if ns == end:
					#	paths.append('*')
		return paths
	
	
	def short_path(self,start,end,path=[]):
		path = path + [start]
		if start == end :
			return path
		if start not in self.graf_dic:
			return []
		theshort = None
		for node in self.graf_dic[start]:
			if node not in path:
				n = self.short_path(node,end,path)
				if n:
					if theshort is None or len(n) < len(theshort):
						theshort = n
		return theshort
					
	

#################################
msarat =[
('mombi','paris'),
('mombi','dubi'),
('paris','dubi'),
('paris','new york'),
('dubi','new york'),
('new york','toronto')]
mygraf = graf(msarat)

print ('ALL PATHS')
print (mygraf.get_paths('mombi','new york'))
print ('SHORTEST PATH')
print (mygraf.short_path('mombi','new york'))
print ("*"*40)
#mygraf.print()
#mygraf.add_node(('mombi','iraq'))
#mygraf.add_node(('egypt','vena'))
#mygraf.print()
