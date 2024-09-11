with Ada.Text_IO; use Ada.Text_IO;
with Ada.Float_Text_IO; use Ada.Float_Text_IO;
with Ada.Numerics.Float_Random; use Ada.Numerics.Float_Random;

procedure Sort_Float_Array is
    type Float_Array is array (Positive range <>) of Float;
    subtype Index is Positive range 1..99999;
    --
    procedure Swap(Elems: in out Float_Array; Index1, Index2: Index) is
        Temp: constant Float := Elems(Index1);
    begin
        Elems(Index1) := Elems(Index2);
        Elems(Index2) := Temp;
    end Swap;

    procedure Quick_Sort(Elems: in out Float_Array; Left, Right: Index) is
        Pivot: constant Float := Elems((Left + Right) / 2);
        I: Index := Left;
        J: Index := Right;
    begin
        while I <= J loop
            while Elems(I) < Pivot loop
                I := I + 1;
            end loop;
            while Elems(J) > Pivot loop
                J := J - 1;
            end loop;
            if I <= J then
                Swap(Elems, I, J);
                I := I + 1;
                J := J - 1;
            end if;
        end loop;
        if Left < J then
            Quick_Sort(Elems, Left, J);
        end if;
        if I < Right then
            Quick_Sort(Elems, I, Right);
        end if;
    end Quick_Sort;

    procedure Sort_Floats(Elems: in out Float_Array) is
    begin
        Quick_Sort(Elems, Elems'First, Elems'Last);
    end Sort_Floats;

    procedure Display_Float_Array(Elems: Float_Array) is
    begin
        for I in Elems'Range loop
            Put(Float'Image(Elems(I)));
            New_Line;
        end loop;
    end Display_Float_Array;

    -- Generate random float numbers in the range [0, 1]
    genFloat: Ada.Numerics.Float_Random.Generator;
    F_Array: Float_Array (1 .. 99999);
begin
	reset(genFloat);
    for I in F_Array'Range loop
        F_Array(I) := Standard.Float(random(genFloat));
    end loop;
    
    -- Display unsorted array
    Put_Line("Unsorted array:");
    Display_Float_Array(F_Array);
    
    -- Sort array
    Sort_Floats(F_Array);
    
    -- Display sorted array
    Put_Line("Sorted array:");
    Display_Float_Array(F_Array);
end Sort_Float_Array;
