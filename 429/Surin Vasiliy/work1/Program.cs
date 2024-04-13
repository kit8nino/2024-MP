using System;
using System.Collections;
using work1;

class TestClass
{
    static void Main(string[] args)
    {
        // Data
        Dictionary<string, int> subjects = new Dictionary<string, int>()
        {
            { "Mathematics", 5 },
            { "Russian", 4 },
            { "History", 4 },
            { "Geography", 5 },
            { "Physics", 4 },
            { "Chemistry", 4 },
            { "Biology", 5 },
            { "English", 5 },
            { "Physical Education", 5 },
            { "Computer Science", 4 },
            { "Art", 3 },
            { "Music", 4 },
            { "Economics", 5 },
            { "Literature", 4 },
        };

        Tuple<string, DateTime> actor = new Tuple<string, DateTime>("Charles Bronson", new DateTime(1921, 11, 3));

        List<string> fios = generateFio();

        string tamandua_name = "New Tamandua1";


        // Work with data
        // 1
        Console.WriteLine(averMark(subjects) + "\n");

        // 2
        HashSet<string> names = new HashSet<string>();
        for (int i = 0; i < fios.Count; i++)
        {
            names.Add(fios[i].Split(" ")[0]);
        }
        PrintValues(names);

        // 3
        string all_subj = "";
        foreach (string s in subjects.Keys)
        {
            all_subj += s;
        }
        Console.WriteLine(all_subj.Length + "\n");

        // 4
        HashSet<char> chars = new HashSet<char>();
        foreach (char c in all_subj)
        {
            chars.Add(c);
        }
        PrintValues(chars);

        // 5
        byte[] bytes = System.Text.Encoding.ASCII.GetBytes(tamandua_name);
        foreach (byte b in bytes)
        {
            Console.Write(Convert.ToString(b, 2).PadLeft(8, '0') + " ");
        }
        Console.WriteLine("\n");

        // 6
        Console.WriteLine((DateTime.Now - actor.Item2).Days);
        Console.WriteLine();

        // 7
        string[] b_maters = new string[] { "boards", "concrete", "bricks" };
        Console.WriteLine("Available indexes: 1 - 3");
        Queue<string> materials = new Queue<string>();
        while (true)
        {
            int index = int.Parse(Console.ReadLine());
            if (index < 1 || index > b_maters.Length)
            {
                break;
            }

            materials.Enqueue(b_maters[index - 1]);
        }

        while (materials.Count > 0)
        {
            Console.WriteLine(materials.Dequeue());
        }
        Console.WriteLine();

        // 8
        fios.Sort();
        //DateTime date = actor.Item2;
        //Console.WriteLine((date.Day + date.Month * date.Month + date.Year) % 39 + 1);     // return 18  "Чжоу Хуэй-ван"
        int ind = int.Parse(Console.ReadLine());
        fios[ind] = "Чжоу Хуэй-ван";
        PrintValues(fios);

        // 9
        LinkedList list = new LinkedList();

        list.Add("Большая Пысса");
        list.Add("Большие Пупсы");
        list.Add("Такое");
        list.Add("Тухлянка");
        list.Add("Баклань");
        list.Add("Лохово");
        list.Add("Факфак");
        list.Add("Большое Струйкино");
        list.Add("Дно");
        list.Add("Трусово");
        printList(list);

        list.Remove(Console.ReadLine());
        printList(list);

        list.Insert("Конец", 1);
        printList(list);
    }

    public static void printList(LinkedList list)
    {
        for (int i = 0; i < list.length; i++)
            Console.Write(list.Get(i).value + "   ");
        Console.WriteLine("\n");
    }

    public static void PrintValues(IEnumerable myCollection)
    {
        foreach (Object obj in myCollection)
            Console.Write(obj + "  ");
        Console.WriteLine("\n");
    }

    private static double averMark(Dictionary<string, int> dict)
    {
        double sum = 0;
        foreach (int i in dict.Values)
            sum += i;

        return sum / dict.Count;
    }

    private static List<string> generateFio()
    {
        List<string> fios = new List<string>();
        string[] names = new string[] { "Ivan", "Alexander", "Sergey", 
                                        "Andrey", "Dmitry", "Alexey", 
                                        "Maxim", "Evgeniy", "Vladimir", "Denis" };
        string[] surnames = new string[] { "Ivanov", "Petrov", "Sergeev", 
                                           "Smirnov", "Kuznetsov", "Popov", 
                                           "Volkov", "Vasiliev" };

        Random rand = new Random();
        int len1 = names.Length, len2 = surnames.Length;
        for (int i = 0; i < 20; i++)
        {
            fios.Add(names[rand.Next(len1 - 1)] + " " + surnames[rand.Next(len2 - 1)]);
        }

        return fios;
    }
}