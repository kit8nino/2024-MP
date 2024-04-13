using System;

namespace work2
{
    internal class SortingAlgorithms
    {
        public int[] BubbleSort(int[] arr)
        {
            bool unsorted = true;
            int r = arr.Length - 1;
            while (unsorted)
            {
                unsorted = false;
                for (int i = 0; i < r; i++)
                {
                    if (arr[i + 1] < arr[i])
                    {
                        (arr[i + 1], arr[i]) = (arr[i], arr[i + 1]);    // swap
                        unsorted = true;
                    }
                }
                r -= 1;
            }

            return arr;
        }

        public int[] GnomeSort(int[] arr)
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

        public int[] SelectionSort(int[] arr)
        {
            int n = arr.Length;
            for (int i = 0; i < n - 1; i++)
            {
                int minInd = i;
                for (int j = i + 1; j < n; j++)
                {
                    if (arr[j] < arr[minInd])
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
            if (arr.Length < 2) return arr;

            if (left < right)
            {
                int pivotInd = (left + right) / 2;
                int i = left;
                int j = right;

                while (i <= j)
                {
                    while (arr[i] < arr[pivotInd]) i++;
                    while (arr[j] > arr[pivotInd]) j--;

                    if (i <= j)
                    {
                        (arr[i], arr[j]) = (arr[j], arr[i]);
                        i++;
                        j--;
                    }
                }

                QuickSort(arr, left, j);
                QuickSort(arr, i, right);
            }

            return arr;
        }
    }
}
