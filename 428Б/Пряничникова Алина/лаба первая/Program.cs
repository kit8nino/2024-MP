using System;
using System.Collections.Generic;
using System.Text;

class Task0ne
{
    static List<string> generate_popylar_names()
    {
        List<string> popular_man_firtnames = new List<string> { "Иван", "Александр", "Сергей", "Андрей", "Дмитрий", "Алексей", "Максим", "Владимир", "Евгений", "Игорь" };
        List<string> popular_man_lastnames = new List<string> { "Иванов", "Петров", "Смирнов", "Сергеев", "Попов", "Волков", "Кузнецов", "Васильев" };

        List<string> popular_woman_firtnames = new List<string> { "Мария", "Екатерина", "Анастасия", "Елена", "Анна", "Ольга", "Наталья", "Ирина", "Виктория", "Татьяна" };
        List<string> popular_woman_lastnames = new List<string> { "Иванова", "Петрова", "Смирнова", "Романова", "Попова", "Волкова", "Кузнецова", "Новикова" };

        var random = new Random();
        List<string> names = new List<string>();
        List<string> men_names = new List<string>();
        List<string> women_names = new List<string>();

        for (int i = 0; i < 16; i++)
        {
            string man_firstname = popular_man_firtnames[random.Next(0, popular_man_firtnames.Count)];
            string man_lastname = popular_man_lastnames[random.Next(0, popular_man_lastnames.Count)];
            men_names.Add(man_firstname + " " + man_lastname);

            string woman_firstname = popular_woman_firtnames[random.Next(0, popular_woman_firtnames.Count)];
            string woman_lastname = popular_woman_lastnames[random.Next(0, popular_woman_lastnames.Count)];
            women_names.Add(woman_firstname + " " + woman_lastname);
        }

        names.AddRange(men_names);
        names.AddRange(women_names);

        return names;
    }
    static void Main()
    {
        Dictionary<string, int> grades = new Dictionary<string, int>()
        {
            {"астрономия", 5},
            {"заклинания", 5},
            {"защита от темных искусств", 5},
            {"зельеварение", 5},
            {"история магии", 4},
            {"травология", 5},
            {"трансфигурация", 5},
            {"полеты на метлах", 5},
            {"изучение древних рун", 5},
            {"магловедение", 5},
            {"нумерология", 5},
            {"прорицания", 5},
            {"уход за магическими существами", 4},
            {"алхимия", 5},
            {"курс трансгрессии", 4}
        };


        List<string> names = generate_popylar_names();
        /*foreach (string name in names)
        {
            Console.WriteLine(name);
        }*/

        (string firstname, string lastname, string birth) person_wester = ("Энтони", " Куинн", "21.04.1915");

        string home_tamandua_name = "Cinnamon Bun";

        Console.WriteLine("Задание 1");
        int  sum = 0;
        int count = 0;

        foreach (var grade in grades)
        {
            sum += grade.Value;
            count++;
        }
        double average = (double)sum / count;
        Console.WriteLine("Средняя оценка: " + average);

        Console.WriteLine("Задание 2");
        var unique_names = names.Select(n => n.Split(' ')[0]).Distinct();
        Console.WriteLine("Уникальные имена:");
        foreach (var name in unique_names)
        {
            Console.WriteLine(name);
        }
        Console.WriteLine("Задание 3");
        int total_length = 0;
        foreach (var grade in grades)
        {
            total_length += grade.Key.Length;
        }
        Console.WriteLine("Общая длина всех названий предметов: " + total_length);

        Console.WriteLine("Задание 4");
        string subjects = string.Join("", grades.Keys);
        var unique_chars = subjects.Where(c => c != ' ').Distinct(); ;
        Console.WriteLine("Уникальные буквы в названиях предметов:");
        foreach (var ch in unique_chars)
        {
            Console.Write(ch + " ");
        }

        Console.WriteLine("/n");
        Console.WriteLine("Задание 5");
      
        byte[] bytes = Encoding.UTF8.GetBytes(home_tamandua_name);
        string binary = string.Join(" ", bytes.Select(b => Convert.ToString(b, 2).PadLeft(8, '0')));
        Console.WriteLine("Имя домашнего тамандуа в бинарном виде:" + binary);


        Console.WriteLine("Задание 6");
        DateTime birth_date = DateTime.ParseExact(person_wester.birth, "dd.MM.yyyy", null);
        DateTime current_date = DateTime.Now;
        TimeSpan diff = current_date - birth_date;
        int days = diff.Days;
        Console.WriteLine($"Количество дней от даты рождения {person_wester.firstname} {person_wester.lastname} до текущей даты: {days}");


        Console.WriteLine("Задание 7");
        Queue<string> materials = new Queue<string>();
        while (true)
        {
            Console.Write("Введите название стройматериала для покупки или 'стоп', когда список закончен: ");
            string input = Console.ReadLine();

            if (input.ToLower() == "стоп")
            {
                break;
            }

            materials.Enqueue(input);
        }

        Console.WriteLine("Вы ввели следующие стройматериалы:");

        while (materials.Count > 0)
        {
            Console.WriteLine(materials.Dequeue());
        }

        Console.WriteLine("Задание 8");
        Console.Write("Введите индекс имени, которое хотите заменить: ");
        int index = Convert.ToInt32(Console.ReadLine());
        if (index >= 0 && index < names.Count)
        {
            names[index] = "У-ван Чжоу";
        }
        else
        {
            Console.WriteLine("Введен некорректный индекс.");
        }

        foreach (string name in names)
        {
            Console.WriteLine(name);
        }


        Console.WriteLine("Задание 9");
        LinkedList<string> strange_towns = new LinkedList<string>(new[]
        {
            "Добрые пчелы",
            "Жабино",
            "Старые Черви",
            "Косяковка",
            "Дураково",
            "Большое Бухалово",
            "Ломки",
            "Минструактивная",
            "Голодранкино",
            "Манды",
            "Забойная ",
        });

        Console.WriteLine("Связный список странных названий населенных пунктов:");
        foreach (string town in strange_towns)
        {
            Console.WriteLine(town);
        }

      

        Console.WriteLine("Введите название города для удаления:");
        string town_to_delete = Console.ReadLine();

        if (strange_towns.Contains(town_to_delete))
        {
            strange_towns.Remove(town_to_delete);
        }
        else
        {
            Console.WriteLine("Город не найден в списке.");
        }
        

        Console.WriteLine("Введите индекс для вставки города 'Конец':");
        int indexx = int.Parse(Console.ReadLine());

        if (indexx >= 0 && indexx < strange_towns.Count)
            {
                strange_towns.AddBefore(strange_towns.Find(strange_towns.ElementAt(indexx)), "Конец");
            }
        else
            {
                Console.WriteLine("Неправильно указан индекс.");
            }

        foreach (string town in strange_towns)
            {
                Console.WriteLine(town);
            }

    }




}
