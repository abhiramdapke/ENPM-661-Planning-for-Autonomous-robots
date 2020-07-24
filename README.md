Path-Planning-for-Autonomous-robots  
This is a path planning course. It involves projects related to path planning of autonomous robots and all the projects are done in C++/Python.  

# Project 1  

## 8 Puzzle Solver  

Problem statement is in the Project 1 folder  

![image](https://user-images.githubusercontent.com/47953521/88434004-389ca080-cdcd-11ea-8451-41a879e45d8e.png)  

## Explanation  

In this project, the 8 puzzle problem was given and we had to use Brute force approach to find all the possible states from the given initial state. The states should be unique.     

Brute Force Search is a general problem solving technique which explores and checks each and every possible state with the goal state and runs until the goal is found. As it does not consider the cost to reach the goal state, it can have a very big time and space complexity. Once we find the goal state, the backward process will lead to the initial state.  

### How to execute the code    

•	Libraries to import: math, numpy  
•	The code works in spyder (from Anaconda navigator)  
1.	Run the file ‘Project1 code’ file.  
2.	Enter numbers separated with a comma. For eg: 1,2,3,4,8,5,6,7,0
3.	Get the output i.e. either the solution will exist or not.  

Note: The node path, nodes and node info would automatically go into the working directory.  

# Project 2  

Problem statement is in the Project 2 folder  

## Implementation of Dijkstra and A Star algorithms on a point and rigid robot  

## Explanation  

In this project, we were given a point robot and a rigid robot. A point robot has 0 radius and clearance and a rigid robot has some radius and clearance from the obstacle. The aim was to implement Dijkstra and Astar algorithm to find a path between the start and the goal node in a map. The robot can move in 8 directions overall. We represented the obstacles by using half planes and algebraic equations.  

The algorithm was implemented by using C++, OOP and Data structures. Let me tell you a bit about the the algorithms. So, Dijkstra is a very popular path planning algorithm to find the shortest path between two vertices and it uses the principle of relaxation of vertices and uses a priority queue data structure to explore nodes. It picks the unvisited vertex with the lowest distance, calculates the distance through it to each unvisited neighbor and updates the neighbor’s distance, if smaller. This is done until the goal node is reached or the queue is empty. Dijkstra promises an optimal path if one exists.  
Drawback – Doesn’t work for negative edges.  

A star is a heuristic search algorithm and is also known as Extended Dijkstra. It is very similar to Dijkstra, only it uses a heuristic function to reduce the number of nodes to be explored which is an advantage. The heuristic function can be calculated by using either Manhattan distance or Euclidean distance. Manhattan distance is the sum of horizontal and vertical distances between two points and Euclidean is the direct physical distance between two points. So, we used Euclidean distance to find the minimum distance to all the nodes from the goal node and then implemented A star on the point and rigid robot.  

The final outcome that we found the shorted path from start to the goal node by successful implementation of these two algorithms.  

### How to execute  

Input all the parameters
Enter radius:
Enter clearance:
Enter resolution:
Enter Start point separated by space: 
Enter goal point separated by space:

In both algorithms, if radius is zero, it is a point robot otherwise, its a rigid robot.

Language used: Python  

# Project 3  

## Implementation of A star on a differential drive non-holonomic robot  

Problem statement is in the Project 3 folder  

## Explanation  

In this project, we had to navigate the Turtlebot in the Robot Realization lab environment setup from a start point to the goal point. The velocities for the left and right wheels were given, the radius of the wheels were given and the distance between the wheels was provided.  
We have to define a reasonable threshold value for the distance to the goal point. Due to the limited number of moves, the robot cannot reach the exact goal location, so to terminate the program a threshold distance has to be defined.  

Then I implemented A star on this robot. The inputs to be taken form the user were the start point coordinates, end point coordinates and the speed of the wheels.  

### How to execute  

The file contains Project3_V_Rep.py, Readme.tst, Proj 3 output video, remode.dll(64-bit), vrep.py and vrepConst.py.
Project3_V_Rep.py is the actual python code file to be executed along with Vrep.  

### Instructions on how to run the prgram:  

The user has to enter the initial x, y, initial orientation and final x, y in each separate line.
Eg: I have executed the program by putting these coordinates:
Please input x value for initial node -4
Please input y value for initial node -4
Please input value for initial theta in radians 0
Please input x value for goal node -4
Please input y value for goal node 0
Then put y for yes.

At first, it takes time to generate nodes and then when the nodes and the path is generated the simulation starts.

The initial position and orientation is needed to be set manually in the vrep and is to be same as the input given.

### Output Video  

![Proj 3 output video](https://user-images.githubusercontent.com/47953521/88433357-e4dd8780-cdcb-11ea-8aba-ea51ddc06f59.gif)  

# Project 4  

## Implementation of Motion Planning on Baxter Robot  

### Output Video  

![Proj 4 output video](https://user-images.githubusercontent.com/47953521/88434364-02abec00-cdce-11ea-8a65-34f8a228f7ce.gif)  

# Project 5  

Problem Statement is in the Project 5 folder  

## Path Planning for Multiple Warehouse Autonomous Ground Vehicles  

### Explanation  

In this project, we simulated an artificial Amazon warehouse environment and planned the path for 8 AGVs that moved from the pickup station to the delivery station. This project was done in Python using Data structures.
So, to describe about the workspace, there were 8 horizontal and 8 vertical spaces in the whole workspace which were called shelves and there were 3 boxes in each shelf.  

The challenges in this scenario were bottlenecks and collisions. To tackle this, prioritized planning approach was the best. This approach is used by the D star algorithm. We implemented D star Lite algorithm on the workspace for the AGVs to navigate from their pickup station to the delivery station.  

D star lite is the extension of lifelong planning A* in which, the edge weights are modified as we traverse the graph. This can also be viewed as re-planning through relaxation of path costs. The re-computation is minimized in D star. An RHS cost is calculated from the goal node to all the nodes that are yet to be traversed and updated timely. Here, an RHS cost is the distance from the goal node to the node that is currently being taken into consideration.  

The final outcome was that we were successful in finding the path between pickup and delivery stations for 8 autonomous ground vehicles without bottlenecks and collisions.  

### Workspace used for the Project  

![image](https://user-images.githubusercontent.com/47953521/88433855-e6f41600-cdcc-11ea-9bb9-7353e54c811b.png)  

### How to execute the code  

1. Run main.py  
2. Change start and goal nodes for each robot by editing the lists "startNodes" and "endNodes"  

### Output Video  

We are considering 3 types of test cases to plot our results. Test cases considered are as follows:  
1.	All target locations at the left  
2.	All target locations at the right  
3.	Split left-right  

![screen-capture-1](https://user-images.githubusercontent.com/47953521/88433536-47cf1e80-cdcc-11ea-8104-93bfb943b4b4.gif)  

> .gif showing paths followed by robots in Case (1)  

![screen-capture-2](https://user-images.githubusercontent.com/47953521/88433594-61706600-cdcc-11ea-9182-32b37f8c83c0.gif)  

> .gif showing paths followed by robots in Case (2)  

![screen-capture-3](https://user-images.githubusercontent.com/47953521/88433617-6c2afb00-cdcc-11ea-9048-f8a5d0eb2045.gif)  

> .gif showing paths followed by robots in Case (3)  
