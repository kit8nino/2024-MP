using System;

namespace work3
{
    internal class Pos
    {
        public int x { get; set; }
        public int y { get; set; }

        static public bool operator== (Pos pos1, Pos pos2)
        {
            return pos1.x == pos2.x && pos1.y == pos2.y;
        }

        static public bool operator!= (Pos pos1, Pos pos2)
        {
            return !(pos1 == pos2);
        }

        // for HashSet.contains
        public override bool Equals(object obj)
        {
            return this == (Pos)obj;
        }

        public override int GetHashCode()
        {
            return x.GetHashCode() + y.GetHashCode();
        }
    }

    internal class Node
    {
        public int dist { get; set; }
        public Pos pos { get; set; }
        public Node? prev { get; set; }
    }

    class Program
    {
        static char[,] maze;
        static int width, height;
        static Pos startPos, keyPos, exitPos;

        static void Main(string[] args)
        {
            MazeIn("C:\\Users\\Surface\\Desktop\\work3\\maze-for-u.txt");

            startPos = SetRandPos(width, height);
            keyPos = SetRandPos(width, height);
            exitPos = GetExitPos(width, height);

            MazeSetChar(keyPos, '*');

            Dijkstra(startPos);
            MazeOut("C:\\Users\\Surface\\Desktop\\work3\\maze-for-me.txt", maze);
        }

        static void MazeSetChar(Pos pos, char ch)
        {
            maze[pos.x, pos.y] = ch;
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
                    if (!visited.Contains(neighbour))
                    {
                        int dist = currentCell.dist + 1;
                        cellsToVisit.Enqueue(new Node { pos = neighbour, dist = dist, prev = currentCell }, dist);
                    }
                }
            }
        }

        static void DrawPath(Node node, char ch)
        {
            while (node.prev != null)
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

        static bool IsKey(Pos pos1)
        {
            return pos1 == keyPos;
        }

        static bool IsExit(Pos pos1)
        {
            return pos1 == exitPos;
        }

        static bool IsAvailable(int x, int y)
        {
            return (x >= 0 && x < width) && (y >= 0 && y < height) &&
                   (maze[x, y] == ' ' || maze[x, y] == '*');
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
            for (int x = 0; x < size_x; x++)
            {
                if (maze[x, y] == ' ')
                    return new Pos { x = x - 1, y = y - 1 };
            }
            return null;
        }

        static void GetSizes(string[] lines)
        {
            width = lines.Length;
            height = lines[0].Length;
        }

        static void MazeIn(string path)
        {
            string[] lines = File.ReadAllLines(path);
            GetSizes(lines);
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