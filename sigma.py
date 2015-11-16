""" sigma.py
For use with Sigma js: http://sigmajs.org/
Turn a Python adjacency matrix into a sigma-parsable JSON representation
"""


def to_json(adj):
	"""Process an adjacency matrix into a Sigma-style dict."""
	assert len(adj) == len(adj[0]), "Adjacency matrix must have dimensions n by n."
	nodes = []
	edges = []
	n = 0
	for n_row in adj:
		# Create node object
		nodes += [{"id":"n"+str(n), "label":"Node "+str(n), "x":n, "y":n^2, "size":2}]
		m = 0
		for out in n_row:
			if n_row[m] != 0:
				# There's an edge between N and M
				edges += [{"id":"e"+str(n)+str(m), "source":"n"+str(n), "target":"n"+str(m)}]
			m += 1
		n += 1
	obj = {}
	obj['nodes'] = nodes
	obj['edges'] = edges
	return obj


def apply_labels(obj, labels):
	"""Applies each label in labels to the node at the corresponding index in the Sigma-style dict obj"""
	assert len(labels) == len(obj['nodes']), "Nodes and labels length mismatch: " + len(obj['nodes']) + " nodes, " + len(labels) + " labels."
	assert min([(type(x) == str) for x in labels]) == True, "Labels must be of type str."
	for i in range(0, len(labels)):
		obj['nodes'][i]["label"] = labels[i]
	return obj


def apply_sizes(obj, sizes):
	"""Applies each size in sizes to the node at the corresponding index in the Sigma-style dict obj"""
	assert len(sizes) == len(obj['nodes']), "Nodes and sizes length mismatch: " + len(obj['nodes']) + " nodes, " + len(sizes) + " sizes."
	assert min([(type(x) == int or type(x) == float) for x in sizes]) == True, "Sizes must be of type int or float."
	for i in range(0, len(sizes)):
		obj['nodes'][i]["size"] = sizes[i]
	return obj


def to_string(obj):
	"""Process Sigma-style dict into string JSON representation"""
	import json
	return json.dumps(obj)