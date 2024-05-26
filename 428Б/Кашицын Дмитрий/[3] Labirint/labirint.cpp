#include<iostream>
#include<fstream>
#include<vector>
#include<queue>
#include<set>
#include<stack>
#include<algorithm>
#include<cmath>

using namespace std;

int startRow=0, startCol=1;
vector<string> maze;
void initialize_maze(){
    fstream labirint("maze-for-u.txt");
    string line="";
    while(getline(labirint,line)) maze.push_back(line);
}

int x_key, y_key;
void initialize_key(){
    while(true){
        x_key=rand()%500+20;
        y_key=rand()%500+20;
        if(maze[x_key][y_key]!='#'){
            maze[x_key][y_key]='*';
            break;
        }
    }
}

int x_exit,y_exit;
void find_exit_point_in_maze(){
    for(int i=0;i<maze[0].size();i++) if(maze[maze.size()-1][i]==' '){
        x_exit=i;
        y_exit=maze.size()-1;
        break;
    }
}

void printPath(stack<pair<int,int>>& path)
{
    stack<pair<int,int>> tempStack;
    while(!path.empty()){
        tempStack.push(path.top());
        path.pop();
    }
    while(!tempStack.empty()){
        pair<int,int> position = tempStack.top();
        maze[position.first][position.second]='.';
        tempStack.pop();
    }
}

set<pair<int,int>> visited;
stack<pair<int,int>>path;
bool findKeyDFS(const std::vector<string>& maze, int startRow, int startCol, std::set<std::pair<int, int>>& visited,
stack<pair<int,int>> path) {
    if (startRow < 0 || startRow >= maze.size() || startCol < 0 || startCol >= maze[0].size() || maze[startRow][startCol] == '#') {
        return false;
    }
    if (maze[startRow][startCol] == '*') {
        printPath(path);
        return true;
    }
    visited.insert({startRow, startCol});
    path.push({startRow,startCol});
    std::vector<std::pair<int, int>> directions = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
    for (const auto& dir : directions) {
        int newRow = startRow + dir.first;
        int newCol = startCol + dir.second;
        if (visited.find({newRow, newCol}) == visited.end() && findKeyDFS(maze, newRow, newCol, visited,path)) {
            return true;
        }
    }
    path.pop();
    return false;
}

struct Node {
    int x, y;
    int g, h, length; 
    Node* parent;
    Node(int _x, int _y) : x(_x), y(_y), g(0), h(0), length(0), parent(nullptr) {}
    bool operator<(const Node& other) const {
        return (g + h) > (other.g + other.h);
    }
};

bool isValid(int x, int y, const vector<string>& maze) {
    return x >= 0 && y >= 0 && x < maze.size() && y < maze[0].size() && maze[x][y]==' ';
}

int calculateH(Node* current, Node* goal) {
    return abs(current->x - goal->x) + abs(current->y - goal->y);
}

vector<Node*> AStar(const vector<string>& maze, Node* start, Node* goal, int max_length) {
    vector<Node*> path;
    set<Node*> openSet;
    set<Node*> closedSet;
    priority_queue<Node*> openQueue;

    start->g = 0;
    start->h = calculateH(start, goal);
    start->length = 0; 
    openSet.insert(start);
    openQueue.push(start);

    while (!openQueue.empty()) {
        Node* current = openQueue.top();
        openQueue.pop();

        if (current == goal) {
            while (current) {
                path.push_back(current);
                current = current->parent;
            }
            break;
        }
        openSet.erase(current);
        closedSet.insert(current);
        int dx[] = {1, -1, 0, 0};
        int dy[] = {0, 0, 1, -1};

        for (int i = 0; i < 4; ++i) {
            int nx = current->x + dx[i];
            int ny = current->y + dy[i];

            if (isValid(nx, ny, maze)) {
                Node* neighbor = new Node(nx, ny);
                neighbor->g = current->g + 1;
                neighbor->h = calculateH(neighbor, goal);
                neighbor->length = current->length + 1;

                if (closedSet.find(neighbor) != closedSet.end()) {
                    delete neighbor;
                    continue;
                }

                if (neighbor->length <= max_length) { 
                    if (openSet.find(neighbor) == openSet.end()) {
                        openSet.insert(neighbor);
                        openQueue.push(neighbor);
                        neighbor->parent = current;
                    } else {
                        delete neighbor;
                    }
                } else {
                    delete neighbor;
                }
            }
        }
    }
    for (Node* node : openSet) delete node;
    for (Node* node : closedSet) delete node;
    return path;
}

int main(){
    initialize_maze();
    initialize_key();
    find_exit_point_in_maze();
    findKeyDFS(maze, startRow, startCol, visited, path);
    Node* start = new Node(x_key,y_key);
    Node* goal = new Node(x_exit,y_exit);
    int max_length=20;
    vector<Node*> path = AStar(maze,start,goal,max_length);
    for(int i=0;i<path.size();i++){
        maze[path[i]->x][path[i]->y]=',';
    }
}
