# Shortest Path Finder With UCS And A*

![image](https://user-images.githubusercontent.com/91037907/230951095-9c7ca17a-0c09-4547-95c9-1054b83f762c.png)

## Overview

This project is a Python project that implements UCS and A* algorithm to find shortest path between two locations in a map.

### Problem Description

The UCS (Uniform Cost Search) and A* (or A-star) algorithms can be used to determine the shortest path from one point to another. This can be used to find the shortest path between two locations in the streets of Bandung City. The streets in Bandung can be represented as a weighted graph where road intersections become nodes. Interconnected road intersections are then depicted as graph edges with their distances as weights in km. This problem is solved by creating a simple program that contains a .txt file containing intersection points on the streets of Bandung City.

The program can accept a .txt file in the following format:
The first line contains n, the number of locations (nodes).
Line ke-(2i) contains the name of the location (node), and line ke-(2i+1) contains the coordinates (latitude, longitude) separated by commas (without spaces between them). With 0 < i ≤ n.
The next n lines are a weighted adjacency matrix that shows the neighboring nodes.
The input file example can be seen in `test` folder.
The user can then choose which algorithm to use to solve the problem.
This project can also visualized the map inputted by the user if run through app.py

This project is built to meet the following [guidelines](https://informatika.stei.itb.ac.id/~rinaldi.munir/Stmik/2022-2023/Tucil3-Stima-2023.pdf).

## Prerequisites

- Python
- `Flask` python package installed
- `Folium` python package installed

## How To Run
1. Clone this repository.

```
 $ git clone https://github.com/chaerla/Tucil3_13521044_13521079.git
```

2. Open terminal and navigate to the root directory of this folder

```
 $ cd Tucil3_13521044_13521079
```

3. Run `python src/app.py` in terminal. (make sure you're running from the root)

```
 $ python src/app.py
```
![image](https://user-images.githubusercontent.com/91037907/230952814-ba55f077-742d-47e3-bed1-ef7093ab1222.png)

4. Insert the file name along with the extension (relative to the test folder)
![image](https://user-images.githubusercontent.com/91037907/230952918-f66c7ccf-a9d9-401d-9a42-8f741a959c3c.png)

5. Pick the start and goal node
![image](https://user-images.githubusercontent.com/91037907/230953005-87373c47-d6e1-4f27-b81b-a8f0dde30793.png)

6. Pick the algorithm to use
![image](https://user-images.githubusercontent.com/91037907/230953104-053a7814-c429-413a-8c33-b24d7454e19d.png)

7. The path and distance will be shown
![image](https://user-images.githubusercontent.com/91037907/230953152-aec6a17b-9640-4ef3-92cd-aaa4dd4ecec5.png)

8. Open localhost in a browser to look at the visualization
![image](https://user-images.githubusercontent.com/91037907/230953236-a8a59c39-dc4a-4c70-9bd5-aa50e5984f22.png)


## Authors

| Name                  | GitHub                                            | NIM                  |
| --------------------- | ------------------------------------------------- | --------------------- |
| Rachel Gabriela Chen  | [chaerla](https://github.com/chaerla)             | 13521044 |
| Hobert Anthony Jonathan  | [HobertJ](https://github.com/melvinkj)           | 13521079 |
