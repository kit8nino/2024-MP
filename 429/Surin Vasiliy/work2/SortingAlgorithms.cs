using System;

namespace work2
{
    internal class SortingAlgorithms
    {
        public string[] BubbleSort(string[] arr)
        {
            bool unsorted = true;
            int r = arr.Length - 1;
            while (unsorted)
            {
                unsorted = false;
                for (int i = 0; i < r; i++)
                {
                    if (stringSize(arr[i + 1]) < stringSize(arr[i]))
                    {
                        (arr[i + 1], arr[i]) = (arr[i], arr[i + 1]);    // swap
                        unsorted = true;
                    }
                }
                r -= 1;
            }

            return arr;
        }

        public double[] GnomeSort(double[] arr)
        {
            int n = arr.Length;
            if (n < 2) return arr;

            int i = 1, j = 2;
            while (i < n)
            {
                if (arr[i - 1] < arr[i])
                {
                    i = j;
                    j = j + 1;
                } 
                else
                {
                    (arr[i - 1], arr[i]) = (arr[i], arr[i - 1]);
                    i = i - 1;
                    if (i == 0)
                    {
                        i = j;
                        j = j + 1;
                    }
                }
            }

            return arr;
        }

        public Complex[] SelectionSort(Complex[] arr)
        {
            int n = arr.Length;
            for (int i = 0; i < n - 1; i++)
            {
                int minInd = i;
                for (int j = i + 1; j < n; j++)
                {
                    if (arr[j].abs() < arr[minInd].abs())
                    {
                        minInd = j;
                    }
                }

                (arr[i], arr[minInd]) = (arr[minInd], arr[i]);
            }

            return arr;
        }

        public int[] QuickSort(int[] arr, int left, int right)
        {
            if (left < right)
            {
                int pivot = arr[right];
                int i = left - 1;

                for (int j = left; j < right; j++)
                {
                    if (arr[j] < pivot)
                    {
                        i += 1;
                        (arr[i], arr[j]) = (arr[j], arr[i]);
                    }
                }

                (arr[i + 1], arr[right]) = (arr[right], arr[i + 1]);

                int pivotIndex = i + 1;

                QuickSort(arr, left, pivotIndex - 1);
                QuickSort(arr, pivotIndex + 1, right);
            }

            return arr;
        }

        private int stringSize(string str)
        {
            int res = 0;

            foreach (char c in str)
            {
                res += (int)c;
            }

            return res;
        }
    }
}
