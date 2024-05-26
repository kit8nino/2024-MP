using System;

namespace work2
{
    internal class RandomExt
    {
        int seed = DateTime.Now.Millisecond;

        public RandomExt(int _seed)
        {
            seed = _seed;
        }

        public RandomExt() {}

        public int[] randomlySelectedSort()
        {
            Random rnd = new Random(seed);
            return new int[] { rnd.Next(1, 18), rnd.Next(1, 18), rnd.Next(1, 18), rnd.Next(1, 18) };
        }

        public double randRange(double a, double b)
        {
            Random rnd = new Random();
            return a + (b - a) * rnd.NextDouble();
        }

        public int[] randShuffle(int[] arr)
        {
            Random rnd = new Random();
            for (int i = 0; i < arr.Length; i++)
            {
                int ind = rnd.Next(0, arr.Length - 1);

                (arr[i], arr[ind]) = (arr[ind], arr[i]);
            }

            return arr;
        }
    }
}
