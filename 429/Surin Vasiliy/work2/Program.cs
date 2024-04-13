using System;
using System.Text.RegularExpressions;

namespace work2
{
    internal class Program
    {
        const int birth_day = 28; 
        const int birth_month = 1;
        const string FILE_PATH = "D:\\Файлы\\ProgIng\\429\\Surin Vasiliy\\work2\\book.txt";

        static void Main(string[] args)
        {
            int n = 999999;
            RandomExt extRand = new RandomExt(100500);
            int[] num1 = extRand.randShuffle(listGenerator(n));

            n = 99999;
            double[] num2 = new double[n];
            for (int i = 0; i < n; i++)
            {
                num2[i] = extRand.randRange(-1, 1);
            }

            Complex[] num3 = complexListGenerator(42000);
            string[] words = splitFile(FILE_PATH);

            // ------------------
            printArr(extRand.randomlySelectedSort(), false);    // 8, 7, 2, 10
            Console.WriteLine();

            SortingAlgorithms sorts = new SortingAlgorithms();
            printArr(sorts.QuickSort(num1, 0, num1.Length - 1), false);
            Console.WriteLine();
            printArr(sorts.GnomeSort(num2), false);
            Console.WriteLine();
            printArr(sorts.SelectionSort(num3), false);
            Console.WriteLine();
            printArr(sorts.BubbleSort(words), false);
        }

        private static void printArr(Complex[] arr, bool newLine = true)
        {
            for (int i = 0; i < arr.Length; i++)
            {
                if (newLine)
                    Console.WriteLine(arr[i].x_ + "+j" + arr[i].y_);
                else
                    Console.Write(arr[i].x_ + "+j" + arr[i].y_ + "\t");
            }

            if (!newLine) Console.WriteLine();
        }

        private static void printArr<T>(T[] arr, bool newLine = true)
        {
            for (int i = 0; i < arr.Length; i++)
            {
                if (newLine)
                    Console.WriteLine(arr[i]);
                else
                    Console.Write(arr[i] + " ");
            }

            if (!newLine) Console.WriteLine();
        }

        private static string[] splitFile(string path)
        {
            string text = File.ReadAllText(path);
            return Regex.Split(text, @"\W+");
        }

        private static int[] listGenerator(int n)
        {
            int[] res = new int[n + 1];
            for (int i = 0; i <= n; i++)
                res[i] = i;

            return res;
        }

        private static Complex[] complexListGenerator(int n)
        {
            double r = birth_day / birth_month;
            RandomExt extRand = new RandomExt();
            Complex[] res = new Complex[n];

            int i = 0;
            while (i < n)
            {
                double x = extRand.randRange(-r, r);
                double y = extRand.randRange(-r, r);
                if (x * x + y * y < r)
                {
                    res[i] = new Complex(x, y);
                    i += 1;
                }
            }

            return res;
        }
    }
}