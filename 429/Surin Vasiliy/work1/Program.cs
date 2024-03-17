
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

        string tamandua_name = "Curious Explorer";


        // Work with data
        // 1
        Console.WriteLine(averMark(subjects) + "\n");

        // 2
        HashSet<string> names = new HashSet<string>();
        for (int i = 0; i < fios.Count; i++)
        {
            names.Add(fios[i].Split(" ")[0]);
        }
        foreach (string n in names)
            Console.WriteLine(n);
        Console.WriteLine();

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
        foreach (char n in chars)
            Console.Write(n);
        Console.WriteLine("\n");

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