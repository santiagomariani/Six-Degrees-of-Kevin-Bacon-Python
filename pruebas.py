
def main():

	dic = {}

	pelicula1 = "El secreto de sus ojos"
	actor1 = "Darin"
	actor2 = "Francella"

	dic[pelicula1] = {}

	dic[pelicula1][actor1] = None
	dic[pelicula1][actor2] = None

	for v in dic.keys():
		print("Actores pelicula {}:".format(v))
		for w in dic[v].keys():
			print(w)


main()


