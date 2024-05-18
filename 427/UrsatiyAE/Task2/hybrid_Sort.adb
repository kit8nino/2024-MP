with Ada.Text_IO; use Ada.Text_IO;
with Ada.Containers.Vectors;
with Ada.Containers.Indefinite_Vectors;
with Ada.Integer_Text_IO; use Ada.Integer_Text_IO;
with Ada.Numerics.Float_Random; use Ada.Numerics.Float_Random;

procedure Hybrid_Sort is
    package Integer_Vectors is new Ada.Containers.Vectors
        (Index_Type   => Positive,
         Element_Type => Integer);

    A : Integer_Vectors.Vector;

    -- Quick sort procedure
    procedure Quick_Sort(Arr : in out Integer_Vectors.Vector) is
        procedure Swap(Elem1, Elem2 : in out Integer) is
            Temp : Integer := Elem1;
        begin
            Elem1 := Elem2;
            Elem2 := Temp;
        end Swap;

        procedure Sort_Partition(Left, Right : Integer) is
            Pivot : Integer := Arr((Left + Right) / 2);
            I     : Integer := Left;
            J     : Integer := Right;
        begin
            while I <= J loop
                while Arr(I) < Pivot loop
                    I := I + 1;
                end loop;

                while Arr(J) > Pivot loop
                    J := J - 1;
                end loop;

                if I <= J then
                    Swap(Arr(I), Arr(J));
                    I := I + 1;
                    J := J - 1;
                end if;
            end loop;

            if Left < J then
                Sort_Partition(Left, J);
            end if;

            if I < Right then
                Sort_Partition(I, Right);
            end if;
        end Sort_Partition;
    begin -- Quick_Sort
        Sort_Partition(1, Arr.Length);
    end Quick_Sort;

    -- Merge sort procedure
    procedure Merge_Sort(Arr : in out Integer_Vectors.Vector) is
        Temp : Integer_Vectors.Vector;

        procedure Merge(Left, Middle, Right : Integer) is
            I : Integer := Left;
            J : Integer := Middle + 1;
            K : Integer := Left;
        begin
            while I <= Middle and J <= Right loop
                if Arr(I) <= Arr(J) then
                    Temp.Append_Element(Arr(I));
                    I := I + 1;
                else
                    Temp.Append_Element(Arr(J));
                    J := J + 1;
                end if;
            end loop;

            while I <= Middle loop
                Temp.Append_Element(Arr(I));
                I := I + 1;
            end loop;

            while J <= Right loop
                Temp.Append_Element(Arr(J));
                J := J + 1;
            end loop;

            for Index in Temp'Range loop
                Arr(Left + Index - 1) := Temp(Index);
            end loop;
            Temp.Clear;
        end Merge;

        procedure Sort(Left, Right : Integer) is
            Middle : constant Integer := (Left + Right) / 2;
        begin
            if Left < Right then
                Sort(Left, Middle);
                Sort(Middle + 1, Right);
                Merge(Left, Middle, Right);
            end if;
        end Sort;
    begin -- Merge_Sort
        Sort(1, Arr.Length);
    end Merge_Sort;

begin
    -- Initialize the array with random integers
    for I in 1..20 loop
        A.Append_Element(Integer(Float(Random) * 100.0));
    end loop;

    -- Output the unsorted array
    Put_Line("Unsorted Array:");
    for Item of A loop
        Put(Item'Img & " ");
    end loop;
    New_Line;

    -- Apply hybrid sorting (combination of quick sort and merge sort)
    if A.Length > 1 then
        if A.Length > 10 then
            Quick_Sort(A);
        else
            Merge_Sort(A);
        end if;
    end if;

    -- Output the sorted array
    Put_Line("Sorted Array:");
    for Item of A loop
        Put(Item'Img & " ");
    end loop;
    New_Line;
end Hybrid_Sort;
