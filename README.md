I would like to practise competitive programming in a more structured way. This file contains a list of some topics to study, associated algorithms and formulae, and a collection of problems related to each topic.

Also in this repository are some few implementations of these algorithms.

See my [competitive programming solutions repo](https://github.com/iandioch/solutions), which contains solutions to some of the problems listed here.

The following links may be of interest too:

- [awesome-competitive-programming](https://github.com/lnishan/awesome-competitive-programming)
- [algorithmic-resources](https://github.com/hkirat/Algorithmic-Resources)
- [Methods to Solve](https://cpbook.net/methodstosolve)

# Topics

## Graphs

### Graph Colouring & Bipartite Graphs

Study:

- [Brook's theorem](https://en.wikipedia.org/wiki/Brooks%27_theorem) gives an upper bound on the chromatic number (number of colours) of a graph.
- Brute force search, as there is no fast algorithm to find the exact optimal colouring.
- [Greedy colouring](https://en.wikipedia.org/wiki/Greedy_coloring).
- [Bipartite graphs](https://en.wikipedia.org/wiki/Bipartite_graph) are graphs that can be coloured with 2 colours.

Practise:

- [`kattis:basincity`](https://open.kattis.com/problems/basincity)
- [`kattis:bookclub`](https://open.kattis.com/problems/bookclub)
- [`kattis:cleaningpipes`](https://open.kattis.com/problems/cleaningpipes)
- [`kattis:coloring`](https://open.kattis.com/problems/coloring)
- [`kattis:escapeplan`](https://open.kattis.com/problems/escapeplan)
- [`kattis:gopher2`](https://open.kattis.com/problems/gopher2)
- [`kattis:mapcolouring`](https://open.kattis.com/problems/mapcolouring)
- [`kattis:vivoparc`](https://open.kattis.com/problems/vivoparc)

### Minimum Spanning Tree

Study:

- [Kruskal's algorithm](https://en.wikipedia.org/wiki/Kruskal%27s_algorithm), which adds edges that do not create a cycle.
- [Prim's algorithm](https://en.wikipedia.org/wiki/Prim%27s_algorithm), which adds the next closest non-included vertex.

Practise:

- [`kattis:cats`](https://open.kattis.com/problems/cats)
- [`kattis:freckles`](https://open.kattis.com/problems/freckles)
- [`kattis:lostmap`](https://open.kattis.com/problems/lostmap)
- [`kattis:minspantree`](https://open.kattis.com/problems/minspantree)

## Number Theory

### Prime Numbers

Study:

- [Sieve of Eratosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes) to generate prime numbers up to some `N`, in `O(N log log N)`, with `O(N)` space complexity. You can speed it up by using wheels; ie. skipping all even numbers, or with a strategy to skip multiples of 3 as well.

Practise:

- [`kattis:emergency`](https://open.kattis.com/problems/emergency)
- [`kattis:enlarginghashtables`](https://open.kattis.com/problems/enlarginghashtables)
- [`kattis:fundamentalneighbors`](https://open.kattis.com/problems/fundamentalneighbors)
- [`kattis:olderbrother`](https://open.kattis.com/problems/olderbrother)
- [`kattis:pascal`](https://open.kattis.com/problems/pascal)
- [`kattis:primalrepresentation`](https://open.kattis.com/problems/primalrepresentation)
- [`kattis:primereduction`](https://open.kattis.com/problems/primereduction)
- [`kattis:primesieve`](https://open.kattis.com/problems/primesieve)

## Geometry

### Trigonometry

Study:

- The [Law of cosines](https://en.wikipedia.org/wiki/Law_of_cosines), a generalisation of Pythagoras.

Practise:

- [`kattis:triangleornaments`](https://open.kattis.com/problems/triangleornaments)

### Polygons

Study:

- [Shoelace formula](https://en.wikipedia.org/wiki/Shoelace_formula) for polygon area.
- [Even-odd rule](https://en.wikipedia.org/wiki/Even%E2%80%93odd_rule) to test if a point is inside a polygon.
- [Convex hull](https://en.wikipedia.org/wiki/Convex_hull).
- [Rotating callipers](https://en.wikipedia.org/wiki/Rotating_calipers) for min/max width of a polygon.

Practise:

- [`kattis:blowingcandles`](https://open.kattis.com/problems/blowingcandles)
- [`kattis:convexhull`](https://open.kattis.com/problems/convexhull)
- [`kattis:convexhull2`](https://open.kattis.com/problems/convexhull2)
- [`kattis:cuttingcorners`](https://open.kattis.com/problems/cuttingcorners)
- [`kattis:pointinpolygon`](https://open.kattis.com/problems/pointinpolygon)
- [`kattis:polygonarea`](https://open.kattis.com/problems/polygonarea)
- [`kattis:roberthood`](https://open.kattis.com/problems/roberthood)
- [`kattis:robotprotection`](https://open.kattis.com/problems/robotprotection)

## Strings

### Longest substring

Practise:

- [`leetcode:longest-palindromic-substring`](https://leetcode.com/problems/longest-palindromic-substring)
- [`leetcode:longest-substring-without-repeating-characters`](https://leetcode.com/problems/longest-substring-without-repeating-characters/)
