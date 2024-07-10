with Ada.Text_IO; use Ada.Text_IO;
with Ada.Containers; use Ada.Containers;
with Ada.Containers.Indefinite_Doubly_Linked_Lists;
with Ada.Numerics.Float_Random;

procedure Maze_Solver is
    type Maze_Array is array(Integer range <>, Integer range <>) of Character;
    type Coordinate is record
        X : Integer;
        Y : Integer;
    end record;

    function Read_Maze_From_File(File_Name : String) return Maze_Array is
        Maze : Maze_Array(1..10, 1..10);  -- Предполагается, что лабиринт 10x10
        File : File_Type;
    begin
        Open(File, In_File, File_Name);
        for I in 1..10 loop
            for J in 1..10 loop
                Read(File, Maze(I, J));
            end loop;
        end loop;
        Close(File);
        return Maze;
    end Read_Maze_From_File;

    procedure Print_Maze(Maze : Maze_Array) is
    begin
        for I in Maze'Range(1) loop
            for J in Maze'Range(2) loop
                Put(Maze(I, J));
            end loop;
            New_Line;
        end loop;
    end Print_Maze;

    function Is_Valid_Coordinate(Coord : Coordinate) return Boolean is
    begin
        return Coord.X >= 1 and then Coord.X <= 10 and then
               Coord.Y >= 1 and then Coord.Y <= 10;
    end Is_Valid_Coordinate;

    function DFS(Maze : Maze_Array; Start : Coordinate; Goal : out Coordinate) return Boolean is
        Visited : array(1..10, 1..10) of Boolean := (others => (others => False));
        Stack : Indefinite_Doubly_Linked_Lists.List := Indefinite_Doubly_Linked_Lists.Empty_List;
        Current : Coordinate := Start;
        Next : Coordinate;
    begin
        Stack.Append(Current);
        while not Stack.Is_Empty loop
            Current := Stack.Element;
            Stack.Delete_First;
            if Maze(Current.X, Current.Y) = '*' then
                Goal := Current;
                return True;
            end if;
            Visited(Current.X, Current.Y) := True;
            -- Проверяем соседей
            Next := Current;
            Next.X := Current.X + 1;
            if Is_Valid_Coordinate(Next) and then Maze(Next.X, Next.Y) /= '#' and then not Visited(Next.X, Next.Y) then
                Stack.Append(Next);
            end if;
            Next := Current;
            Next.X := Current.X - 1;
            if Is_Valid_Coordinate(Next) and then Maze(Next.X, Next.Y) /= '#' and then not Visited(Next.X, Next.Y) then
                Stack.Append(Next);
            end if;
            Next := Current;
            Next.Y := Current.Y + 1;
            if Is_Valid_Coordinate(Next) and then Maze(Next.X, Next.Y) /= '#' and then not Visited(Next.X, Next.Y) then
                Stack.Append(Next);
            end if;
            Next := Current;
            Next.Y := Current.Y - 1;
            if Is_Valid_Coordinate(Next) and then Maze(Next.X, Next.Y) /= '#' and then not Visited(Next.X, Next.Y) then
                Stack.Append(Next);
            end if;
        end loop;
        return False;
    end DFS;

    function A_Star(Maze : Maze_Array; Start : Coordinate; Goal : Coordinate) return List is
        -- Ваш код A* здесь
        -- Для простоты, здесь представлен пустой список в качестве примера
        Empty_List : List;
    begin
        return Empty_List;
    end A_Star;

    procedure Save_Maze_With_Path(Maze : Maze_Array; Path : List; Key : Coordinate; File_Name : String) is
        File : File_Type;
        Current : Coordinate := Key;
    begin
        Open(File, Out_File, File_Name);
        for I in Maze'Range(1) loop
            for J in Maze'Range(2) loop
                if Current.X = I and Current.Y = J then
                    Put(File, '*');
                elsif Contains(Path, (X => I, Y => J)) then
                    Put(File, '.');
                else
                    Put(File, Maze(I, J));
                end if;
            end loop;
            New_Line(File);
        end loop;
        Close(File);
    end Save_Maze_With_Path;

    -- Основной код программы
    Maze : Maze_Array;
    Start, Key, Exi : Coordinate;
    Path_To_Key, Path_To_Exit : List;
begin
    Maze := Read_Maze_From_File("maze-for-u.txt");
    Start.X := 1;  -- Начальные координаты аватара
    Start.Y := 1;
    
    -- Поиск пути к ключу с помощью DFS
    if DFS(Maze, Start, Key) then
        Put_Line("Found key at (" & Integer'Image(Key.X) & ", " & Integer'Image(Key.Y) & ")");
    else
        Put_Line("Key not found!");
        return;
    end if;

    -- Поиск оптимального пути к выходу с использованием A*
    -- Предполагается, что Key найден, иначе нужно было бы обработать этот случай
    Exi.X := 10;  -- Предполагается, что выход находится на крайней правой стене
    Exi.Y := Key.Y;

    Path_To_Exit := A_Star(Maze, Key, Exi);

    -- Сохранение лабиринта с маршрутом в файл
    Save_Maze_With_Path(Maze, Path_To_Exit, Key, "maze-for-me-done.txt");

    Put_Line("Maze with path saved to maze-for-me-done.txt");
end Maze_Solver;
