Some topics to study for competitive programming, and some algorithms, concepts, and Kattis problems related to those topics.

See also:

- [awesome-competitive-programming](https://github.com/lnishan/awesome-competitive-programming)
- [algorithmic-resources](https://github.com/hkirat/Algorithmic-Resources)
- [Methods to Solve](https://cpbook.net/methodstosolve)

# Topics

## Graphs

### Graph Colouring & Bipartite Graphs

Study:

- [Brook's theorem](https://en.wikipedia.org/wiki/Brooks%27_theorem) gives an upper bound on the chromatic number of a graph.
- Brute force search, as there is no fast algorithm to find the exact optimal colouring.
- [Greedy colouring](https://en.wikipedia.org/wiki/Greedy_coloring).
- [Bipartite graphs](https://en.wikipedia.org/wiki/Bipartite_graph) are graphs that can be coloured with 2 colours.

Practise:

- [`basincity`](https://open.kattis.com/problems/basincity)
- [`bookclub`](https://open.kattis.com/problems/bookclub)
- [`cleaningpipes`](https://open.kattis.com/problems/cleaningpipes)
- [`coloring`](https://open.kattis.com/problems/coloring)
- [`escapeplan`](https://open.kattis.com/problems/escapeplan)
- [`gopher2`](https://open.kattis.com/problems/gopher2)
- [`mapcolouring`](https://open.kattis.com/problems/mapcolouring)
- [`vivoparc`](https://open.kattis.com/problems/vivoparc)

### Minimum Spanning Tree

Study:

- [Kruskal's algorithm](https://en.wikipedia.org/wiki/Kruskal%27s_algorithm), which adds edges that do not create a cycle.
- [Prim's algorithm](https://en.wikipedia.org/wiki/Prim%27s_algorithm), which adds the next closest non-included vertex.

Practise:

- [`cats`](https://open.kattis.com/problems/cats)
- [`lostmap`](https://open.kattis.com/problems/lostmap)
- [`minspantree`](https://open.kattis.com/problems/minspantree)
- [`freckles`](https://open.kattis.com/problems/freckles)

## Number Theory

### Prime Numbers

Study:

- [Sieve of Eratosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes) to generate prime numbers up to some `N`, in `O(N log log N)`, with `O(N)` space complexity. You can speed it up by using wheels; ie. skipping all even numbers, or with a strategy to skip multiples of 3 as well.

Practise:

- [`emergency`](https://open.kattis.com/problems/emergency)
- [`enlarginghashtables`](https://open.kattis.com/problems/enlarginghashtables)
- [`fundamentalneighbors`](https://open.kattis.com/problems/fundamentalneighbors)
- [`olderbrother`](https://open.kattis.com/problems/olderbrother)
- [`pascal`](https://open.kattis.com/problems/pascal)
- [`primalrepresentation`](https://open.kattis.com/problems/primalrepresentation)
- [`primereduction`](https://open.kattis.com/problems/primereduction)
- [`primesieve`](https://open.kattis.com/problems/primesieve)

## Geometry

### Trigonometry

Study:

- The [Law of cosines](https://en.wikipedia.org/wiki/Law_of_cosines), a generalisation of Pythagoras.

Practise:

- [`triangleornaments`](https://open.kattis.com/problems/triangleornaments)

### Polygons

Study:

- [Shoelace formula](https://en.wikipedia.org/wiki/Shoelace_formula) for polygon area.
- [Even-odd rule](https://en.wikipedia.org/wiki/Even%E2%80%93odd_rule) to test if a point is inside a polygon.
- [Convex hull](https://en.wikipedia.org/wiki/Convex_hull).
- [Rotating callipers](https://en.wikipedia.org/wiki/Rotating_calipers) for min/max width of a polygon.

Practise:

- [`blowingcandles`](https://open.kattis.com/problems/blowingcandles)
- [`convexhull`](https://open.kattis.com/problems/convexhull)
- [`convexhull2`](https://open.kattis.com/problems/convexhull2)
- [`cuttingcorners`](https://open.kattis.com/problems/cuttingcorners)
- [`pointinpolygon`](https://open.kattis.com/problems/pointinpolygon)
- [`polygonarea`](https://open.kattis.com/problems/polygonarea)
- [`roberthood`](https://open.kattis.com/problems/roberthood)
- [`robotprotection`](https://open.kattis.com/problems/robotprotection)
