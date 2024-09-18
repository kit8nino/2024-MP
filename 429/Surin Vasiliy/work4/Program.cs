using System;

namespace work4
{
    public class Radar
    {
        public static Radar? _instance = null;

        protected Radar() { }

        public static Radar getInstance()
        {
            if (_instance == null)
                _instance = new Radar();
            return _instance;
        }

        public double X { get; set; }
        public double Y { get; set; }
        public double Z { get; set; }
    }

    public class Object
    {
        // Cartesian
        public double X { get; set; }
        public double Y { get; set; }
        public double Z { get; set; }
        // Spherical
        public double r { get; set; }
        public double theta { get; set; }
        public double phi { get; set; }

        public double[] speeds { get; set; }

        public Object((double, double, double, double[]) data) 
        {
            X = data.Item1;
            Y = data.Item2;
            Z = data.Item3;
            speeds = data.Item4;
        }

        public (double, double, double) getSpherical()
        {
            r = Math.Sqrt(Math.Pow(X, 2) + Math.Pow(Y, 2) + Math.Pow(Z, 2));
            theta = Math.Atan2(Z, Math.Sqrt(Math.Pow(X, 2) + Math.Pow(Y, 2)));
            phi = Math.Atan2(Y, X);

            return (r, theta, phi);
        }
    }

    class TestClass
    {
        static Radar radar;
        static List<Object> objects;
        static double dt = 0;
        public static void Main(string[] args)
        {
            InitInput();

            for (int i = 0; i < objects.Count; i++)
            {
                (double, double, double) coords = objects[i].getSpherical();
                Console.WriteLine($"{i}, t = 0: r = {coords.Item1}, theta = {coords.Item2}, phi = {coords.Item3}"); ;

                Update(dt, i);

                coords = objects[i].getSpherical();
                Console.WriteLine($"{i}, t = dt: r = {coords.Item1}, theta = {coords.Item2}, phi = {coords.Item3}"); ;
            }
        }

        public static void InitInput()
        {
            radar = Radar.getInstance();
            Console.WriteLine("Координаты радара: ");
            radar.X = double.Parse(Console.ReadLine());
            radar.Y = double.Parse(Console.ReadLine());
            radar.Z = double.Parse(Console.ReadLine());

            objects = new List<Object>();
            Console.Write("Количество объектов: ");
            int N = int.Parse(Console.ReadLine());

            Console.WriteLine("(x, y, z, speeds[]):");
            for (int i = 0; i < N; i++)
            {
                objects.Add(new Object(ParseObject()));
            }

            Console.Write("Промежуток времени, c: ");
            dt = double.Parse(Console.ReadLine());
        }

        public static void Update(double dt, int num)
        {
            objects[num].X += objects[num].speeds[0] * dt;
            objects[num].Y += objects[num].speeds[1] * dt;
            objects[num].Z += objects[num].speeds[2] * dt;
        }

        public static (double, double, double) ParseRadar()
        {
            double x = 0, y = 0, z = 0;
            int j = 0;
            string str = Console.ReadLine();
            for (int i = 0; i < str.Length; i++)
            {
                string temp = getWord(str, i);
                i += temp.Length;
                switch (j)
                {
                    case 0:
                        x = int.Parse(temp); 
                        break;
                    case 1:
                        y = int.Parse(temp);
                        break;
                    case 2:
                        z = int.Parse(temp);
                        break;
                }
                j += 1;
            }

            return (x, y, z);
        }

        public static (double, double, double, double[]) ParseObject()
        {
            double x = 0, y = 0, z = 0;
            double[] speeds = new double[3];

            int j = 0;
            string str = Console.ReadLine();
            for (int i = 0; i < str.Length; i++)
            {
                string temp = getWord(str, i);
                i += temp.Length;
                switch (j)
                {
                    case 0:
                        x = double.Parse(temp) - radar.X;
                        break;
                    case 1:
                        y = double.Parse(temp) - radar.Y;
                        break;
                    case 2:
                        z = double.Parse(temp) - radar.Z;
                        break;
                    default:
                        speeds[j - 3] = double.Parse(temp);
                        break;
                }
                j += 1;
            }

            return (x, y, z, speeds);
        }

        public static string getWord(string str, int i)
        {
            string temp = "";
            while (i < str.Length && str[i] != ' ')
            {
                temp += str[i];
                i += 1;
            }

            return temp;
        }
    }
}