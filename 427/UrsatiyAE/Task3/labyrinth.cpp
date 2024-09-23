// Пример программы на C++ для выполнения задачи по поиску пути в лабиринте

#include <iostream>
#include <fstream>
#include <vector>
#include <stack>
#include <queue>
#include <algorithm>

using namespace std;

// Структура для представления точки в лабиринте
struct Point {
    int x, y;
};

// Функция для загрузки лабиринта из файла
vector<string> loadMazeFromFile(string filename) {
    vector<string> maze;
    string line;
    ifstream file(filename);
    
    if (file.is_open()) {
        while (getline(file, line)) {
            maze.push_back(line);
        }
        file.close();
    }
    
    return maze;
}

// Функция для проверки, является ли точка в лабиринте стеной
bool isWall(const vector<string>& maze, int x, int y) {
    return maze[y][x] == '#';
}

// Функция для проверки, является ли точка в лабиринте ключом
bool isKey(const vector<string>& maze, int x, int y) {
    return maze[y][x] == '*';
}
// Функция для выполнения поиска с использованием A* в лабиринте
struct Node {
    Point point;
    int g; // Вес g(x)
    int h; // Вес h(x)
};

// Функция для вычисления эвристики h(x) (расстояние до ключа)
int calculateHeuristic(Point current, Point key) {
    return abs(current.x - key.x) + abs(current.y - key.y);
}

bool operator<(const Node& a, const Node& b) {
    return a.g + a.h > b.g + b.h;
}

vector <Point> aStarSearch(const vector<string>& maze, Point start, Point key) {
    vector<vector<bool>> closedList(maze.size(), vector<bool>(maze[0].size(), false));
    priority_queue<Node> openList;
    
    openList.push({start, 0, calculateHeuristic(start, key)});
    vector <Point>poit;
    poit.push_back(start);
    while (!openList.empty()) {
        Node current = openList.top();
        openList.pop();
        
        Point currentPoint = current.point;
        // Проверка достижения ключа
        if (currentPoint.x == key.x && currentPoint.y == key.y) {
            cout << "Оптимальный путь к ключу найден" << endl;
            return poit;
        }
        
        closedList[currentPoint.y][currentPoint.x] = true;
        
        // Перебор соседних точек
        vector<Point> neighbors = {
            {currentPoint.x - 1, currentPoint.y}, // Влево
            {currentPoint.x + 1, currentPoint.y}, // Вправо
            {currentPoint.x, currentPoint.y - 1}, // Вверх
            {currentPoint.x, currentPoint.y + 1}  // Вниз
        };
        
        for (const Point& neighbor : neighbors) {
            int x = neighbor.x;
            int y = neighbor.y;
            
            if (x >= 0 && x < maze[0].size() && y >= 0 && y < maze.size() && !closedList[y][x] && maze[y][x] != '#') {
                int g = current.g + 1; // Шаг в соседнюю точку считается за 1
                poit.push_back(current.point);
                openList.push({neighbor, g, calculateHeuristic(neighbor, key)});
            }
        }
    }
    
    cout << "Оптимальный путь к ключу не найден" << endl;
}

void saveMazeWithRoute(const vector<string>& maze, Point start, Point key, const vector<Point>& route1,const vector<Point>& route2, string filename) {
    vector<string> mazeWithRoute = maze;
    
    // Пометить ключ в лабиринте
    mazeWithRoute[key.y][key.x] = '*';
    
    // Построить маршрут от начальной точки до ключа
    for (const Point& point : route1) {
        mazeWithRoute[point.y][point.x] = '.';
    }
    
    // Построить маршрут от ключа до выхода
    for (int i = 1; i < route2.size(); ++i) {
        Point prev = route2[i - 1];
        Point current = route2[i];
        if (prev.x == key.x && prev.y == key.y) {
            mazeWithRoute[current.y][current.x] = '*';
        } else {
            mazeWithRoute[current.y][current.x] = ',';
        }
    }
    
    ofstream outFile(filename);
    if (outFile.is_open()) {
        for (const string& line : mazeWithRoute) {
            outFile << line << endl;
        }
        outFile.close();
        cout << "Лабиринт с маршрутом сохранен в файл '" << filename << "'" << endl;
    } else {
        cerr << "Не удалось открыть файл для записи" << endl;
    }
}
vector <Point> aExitSearch(const vector<string>& maze, Point start, Point key) {
    vector<vector<bool>> closedList(maze.size(), vector<bool>(maze[0].size(), false));
    priority_queue<Node> openList;
    
    openList.push({start, 0, calculateHeuristic(start, key)});
    vector <Point>poit;
    poit.push_back(start);
    while (!openList.empty()) {
        Node current = openList.top();
        openList.pop();
        
        Point currentPoint = current.point;
        // Проверка достижения выхода
        if (currentPoint.x == key.x && currentPoint.y == key.y) {
            cout << "Оптимальный путь к выходу найден" << endl;
            return poit;
        }
        
        closedList[currentPoint.y][currentPoint.x] = true;
        
        // Перебор соседних точек
        vector<Point> neighbors = {
            {currentPoint.x - 1, currentPoint.y}, // Влево
            {currentPoint.x + 1, currentPoint.y}, // Вправо
            {currentPoint.x, currentPoint.y - 1}, // Вверх
            {currentPoint.x, currentPoint.y + 1}  // Вниз
        };
        
        for (const Point& neighbor : neighbors) {
            int x = neighbor.x;
            int y = neighbor.y;
            
            if (x >= 0 && x < maze[0].size() && y >= 0 && y < maze.size() && !closedList[y][x] && maze[y][x] != '#') {
                int g = current.g + 1; // Шаг в соседнюю точку считается за 1
                poit.push_back(current.point);
                openList.push({neighbor, g, calculateHeuristic(neighbor, key)});
            }
        }
    }
    
    cout << "Оптимальный путь к выходу не найден" << endl;
}

int main() {
    vector<string> maze = loadMazeFromFile("maze-for-u.txt");
    
    // Начальная точка аватара и координаты ключа
    Point start = {1, 4}; // Пример начальной точки
    Point key = {2, 3}; // Пример координат ключа
    Point exi = {1, 0}; // Пример координат выхода
    
    // Найдем маршрут от начальной точки до ключа с помощью поиска в глубину
    vector <Point> route1=aStarSearch(maze, start, key);
    
    // Найдем оптимальный путь к ближайшему выходу с использованием A*
    vector <Point> route2=aExitSearch(maze, key, exi);
    
    // Сохранение результата в файл "maze-for-me-done.txt"
    saveMazeWithRoute(maze, start, key,route1,route2,"maze-for-me-done.txt");
    
    return 0;
}
