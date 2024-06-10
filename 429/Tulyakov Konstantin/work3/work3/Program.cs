using System;
using System.Collections.Generic;
using System.IO;

namespace work3
{
    internal class Pos : IEquatable<Pos>
    {
        public int x { get; set; }
        public int y { get; set; }

        public override bool Equals(object obj)
        {
            return Equals(obj as Pos);
        }

        public bool Equals(Pos other)
        {
            return other != null && x == other.x && y == other.y;
        }

        public override int GetHashCode()
        {
            return HashCode.Combine(x, y);
        }
    }

    internal class Node
    {
        public int dist { get; set; }
        public Pos pos { get; set; }
        public Node prev { get; set; }
    }

    class Program
    {
        private static char[,] maze;
        private static int width, height;
        private static Pos StartPos, KeyPos, ExitPos;

        static void Main(string[] args)
        {
            MazeIn("C:\\Users\\Костя\\OneDrive\\Рабочий стол\\maze-for-u.txt");

            StartPos = SetRandPos(width, height);
            KeyPos = SetRandPos(width, height);
            ExitPos = GetExitPos(width, height);

            Dijkstra(StartPos);
            AStar(KeyPos, 7000);

            MazeOut("C:\\Users\\Костя\\OneDrive\\Рабочий стол\\maze-for-me.txt", maze);
        }

        static void Dijkstra(Pos start)
        {
            var cellsToVisit = new PriorityQueue<Node, int>();
            var visited = new HashSet<Pos>();

            MazeSetChar(start, 'S');
            cellsToVisit.Enqueue(new Node { pos = start, dist = 0, prev = null }, 0);

            while (cellsToVisit.Count > 0)
            {
                var currentCell = cellsToVisit.Dequeue();
                Pos pos = currentCell.pos;

                if (IsKey(pos))
                {
                    DrawPath(currentCell.prev, '.');
                    MazeSetChar(pos, '*');
                    return;
                }

                visited.Add(pos);

                foreach (var neighbour in Neighbours(pos))
                {
                    if (!IsVisited(visited, neighbour))
                    {
                        int dist = currentCell.dist + 1;
                        cellsToVisit.Enqueue(new Node { pos = neighbour, dist = dist, prev = currentCell }, dist);
                    }
                }
            }
        }

        static double AStarDist(Node node)
        {
            Pos pos = node.pos;
            double g = node.dist;
            double f = Math.Sqrt(Math.Pow(ExitPos.x - pos.x, 2) + Math.Pow(ExitPos.y - pos.y, 2));
            return g + f;
        }

        static void AStar(Pos start, int maxLen)
        {
            var cellsToVisit = new PriorityQueue<Node, double>();
            var visited = new HashSet<Pos>();

            Node temp = new Node { pos = start, dist = 0, prev = null };
            cellsToVisit.Enqueue(temp, AStarDist(temp));
            while (cellsToVisit.Count > 0)
            {
                var currentCell = cellsToVisit.Dequeue();
                Pos pos = currentCell.pos;

                if (IsExit(pos))
                {
                    DrawPath(currentCell.prev, ',');
                    MazeSetChar(pos, 'E');
                    return;
                }

                visited.Add(pos);
                foreach (var neighbour in Neighbours(pos))
                {
                    if (currentCell.dist + 1 <= maxLen && !IsVisited(visited, neighbour))
                    {
                        Node t = new Node { pos = neighbour, dist = currentCell.dist + 1, prev = currentCell };
                        cellsToVisit.Enqueue(t, AStarDist(t));
                    }
                }
            }
        }

        static void DrawPath(Node node, char ch)
        {
            while (node?.prev != null)
            {
                MazeSetChar(node.pos, ch);
                node = node.prev;
            }
        }

        static List<Pos> Neighbours(Pos pos)
        {
            int[] dx = new int[] { -1, 1, 0, 0 };
            int[] dy = new int[] { 0, 0, -1, 1 };
            var neighbours = new List<Pos>();

            for (int i = 0; i < 4; i++)
            {
                if (IsAvailable(pos.x + dx[i], pos.y + dy[i]))
                {
                    neighbours.Add(new Pos { x = pos.x + dx[i], y = pos.y + dy[i] });
                }
            }

            return neighbours;
        }

        static bool IsVisited(HashSet<Pos> set, Pos pos)
        {
            return set.Contains(pos);
        }

        static bool IsKey(Pos pos1)
        {
            return pos1.Equals(KeyPos);
        }

        static bool IsExit(Pos pos1)
        {
            return pos1.Equals(ExitPos);
        }

        static bool IsInBoundaries(int x, int y)
        {
            return (x >= 0 && x < width) && (y >= 0 && y < height);
        }

        static bool IsAvailable(int x, int y)
        {
            return IsInBoundaries(x, y) && (maze[x, y] == ' ' || maze[x, y] == '.');
        }

        static Pos SetRandPos(int size_x, int size_y)
        {
            Random r = new Random();
            int x, y;
            do
            {
                x = r.Next(0, size_x - 1);
                y = r.Next(0, size_y - 1);
            } while (maze[x, y] != ' ');

            return new Pos { x = x, y = y };
        }

        static Pos GetExitPos(int size_x, int size_y)
        {
            int y = size_y - 1;
            int x = 0;
            for (x = 0; x < size_x; x++)
            {
                if (maze[x, y] == ' ')
                    break;
            }
            return new Pos { x = x - 1, y = y - 1 };
        }

        static void MazeSetChar(Pos pos, char ch)
        {
            maze[pos.x, pos.y] = ch;
        }

        static void MazeIn(string path)
        {
            string[] lines = File.ReadAllLines(path);
            width = lines.Length;
            height = lines[0].Length;
            maze = new char[width, height];
            for (int i = 0; i < width; i++)
            {
                for (int j = 0; j < height; j++)
                {
                    maze[i, j] = lines[i][j];
                }
            }
        }

        static void MazeOut(string path, char[,] maze)
        {
            using (StreamWriter writer = new StreamWriter(path))
            {
                for (int i = 0; i < width; i++)
                {
                    for (int j = 0; j < height; j++)
                    {
                        writer.Write(maze[i, j]);
                    }
                    writer.WriteLine();
                }
            }
        }
    }
}

