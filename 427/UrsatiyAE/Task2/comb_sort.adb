with Ada.Text_IO; use Ada.Text_IO;
with Ada.Float_Text_IO; use Ada.Float_Text_IO;
with Ada.Numerics.Float_Random; use Ada.Numerics.Float_Random;
with Ada.Numerics.Complex_Types;

procedure Comb_Sort is
    use Ada.Text_IO;
    use Ada.Numerics.Complex_Types;

    subtype Modulus_Index is Integer range 1 .. 42000;
    type Complex_Array is array (Modulus_Index) of Complex;

    -- Swap two elements in an array
    procedure Swap(Elems: in out Complex_Array; Index1, Index2: in Modulus_Index) is
        Temp: Complex;
    begin
        Temp := Elems(Index1);
        Elems(Index1) := Elems(Index2);
        Elems(Index2) := Temp;
    end Swap;

    -- Comb Sort Algorithm
    procedure Comb_Sort(Arr: in out Complex_Array) is
        Gap: Integer := Arr'Length;
        Swapped: Boolean := True;
        J: Modulus_Index;
    begin
        while Swapped or else Gap > 1 loop
            Gap := Gap * 10 / 13;
            if Gap < 1 then
                Gap := 1;
            end if;
            Swapped := False;
            for I in Modulus_Index'First .. Modulus_Index'Last - Gap loop
                J := I + Modulus_Index(Gap);
                if abs(Arr(I)) > abs(Arr(J)) then
                    Swap(Arr, I, J);
                    Swapped := True;
                end if;
            end loop;
        end loop;
    end Comb_Sort;

    -- Main program
    Arr: Complex_Array;
    a:Complex;
    gen: Ada.Numerics.Float_Random.Generator;
begin
    -- Generate random complex numbers
    reset(gen);
    for I in Modulus_Index loop
        a := Complex'(random(gen) * 5.5 - 2.75, random(gen) * 5.5 - 2.75);
        if (abs(a)>2.75)then
			Arr(I):=Complex'(abs(Re(a))-1.0,abs(Im(a))-1.0);
		else
			Arr(I):=a;
        end if;
    end loop;

    -- Sort the array using Comb Sort
    Comb_Sort(Arr);

    -- Output sorted array
    for I in Modulus_Index loop
        Put_Line("Modulus: " & Float'Image(abs(Arr(I))) & ", Real Part: " & Float'Image(Re(Arr(I))) & ", Imaginary Part: " & Float'Image(Im(Arr(I))));
    end loop;
end Comb_Sort;
