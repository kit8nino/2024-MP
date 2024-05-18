with Ada.Text_IO; use Ada.Text_IO;
with Ada.Strings.Unbounded; use Ada.Strings.Unbounded;
with Ada.Containers.Indefinite_Vectors;
with Ada.Containers.Vectors;
with Ada.Text_IO.Unbounded_IO;

procedure ShellSort is
    type Word_Array is array(Integer range <>) of Unbounded_String;

    Words : Word_Array(1..10000); -- Assuming a maximum of 100 words
    Word_Count : Integer := 0;

    -- Read text from file and fill array with individual words
    procedure Read_Text(File : File_Type) is
        Line : Unbounded_String;
        Word : Unbounded_String;
        Word_Start : Integer;
        Word_End : Integer;
    begin
        while not End_Of_File(File) loop
            Line:=Unbounded_IO.Get_Line(File);
            Word_Start := 1;
            while Word_Start < Length(Line) loop
                while Word_Start < Length(Line) and then Element(Line,Word_Start) = ' ' loop
                    Word_Start := Word_Start + 1;
                end loop;

                Word_End := Word_Start;
                while Word_End < Length(Line) and then Element(Line,Word_End) /= ' ' loop
                    Word_End := Word_End + 1;
                end loop;
                Word := To_Unbounded_String(To_String(Line)(Word_Start..Word_End-1));
                Word_Count := Word_Count + 1;
                Words(Word_Count) := Word;
                Word_Start := Word_End;
            end loop;
        end loop;
    end Read_Text;

    -- Calculate weight of each word
    function Calculate_Weight(Word : Unbounded_String) return Integer is
        Weight : Integer := 0;
    begin
        for I in 1..Length(Word) loop
            Weight := Weight + Character'Pos(Element(Word,I));
        end loop;
        return Weight;
    end Calculate_Weight;

    -- Shellsort algorithm
    procedure Shell_Sort is
        Temp : Unbounded_String;
    begin
        for I in 1..Word_Count-1 loop
            for J in I+1..Word_Count loop
                if Calculate_Weight(Words(I)) > Calculate_Weight(Words(J)) then
                    Temp := Words(I);
                    Words(I) := Words(J);
                    Words(J) := Temp;
                end if;
            end loop;
        end loop;
    end Shell_Sort;

    -- Main program
    File : File_Type;
begin
    Open(File, In_File, "1984.txt");
    Read_Text(File);
    Close(File);

    Put_Line("Unsorted words:");
    for I in 1..Word_Count loop
        Put_Line(To_String(Words(I)));
    end loop;

    Shell_Sort;

    Put_Line("Sorted words based on weight:");
    for I in 1..Word_Count loop
        Put_Line(To_String(Words(I)));
    end loop;
end ShellSort;
