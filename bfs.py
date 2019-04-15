from collections import deque

def bfs(grafo,origen):
	visitados = {}
	padre = {}
	orden = {}

	q = deque()
	q.append(origen)

	visitados[origen] = True
	orden[origen] = 0
	padre[origen] = None

	while q:
		v = q.pop()
		for w in grafo.adyacentes(v):
			if w not in visitados:
				visitados[w] = True
				padre[w] = v
				orden[w] = orden[v] + 1
				q.append(w)
	return padre,orden