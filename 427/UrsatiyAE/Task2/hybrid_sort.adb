with Ada.Text_IO; use Ada.Text_IO;
with Ada.Integer_Text_IO; use Ada.Integer_Text_IO;
with Ada.Numerics.Float_Random; use Ada.Numerics.Float_Random;
with ada.numerics.discrete_random;

procedure Hybrid_Sort is
    type Int_Array is array (Positive range <>) of Integer;

    procedure Hybrid_Sort_Array(Arr : in out Int_Array) is
        -- Insertion sort implementation
        procedure Insertion_Sort(A : in out Int_Array; First, Last : Positive) is
		Temp : Integer;
		Index : Positive;
		begin
			for I in First + 1 .. Last loop
				Temp := A(I);
				Index := I - 1;
				while Index >= First and then A(Index) > Temp loop
					A(Index + 1) := A(Index);
					Index := Index - 1;
				end loop;
				A(Index + 1) := Temp;
			end loop;
		end Insertion_Sort;


        -- Quicksort implementation
        procedure Quick_Sort(A : in out Int_Array; First, Last : Positive) is
            Pivot, Temp : Integer;
            Left, Right : Positive;
        begin
            if Last > First then
                Pivot := A((First + Last) / 2);
                Left := First;
                Right := Last;
                while Left <= Right loop
                    while A(Left) < Pivot loop
                        Left := Left + 1;
                    end loop;
                    while A(Right) > Pivot loop
                        Right := Right - 1;
                    end loop;
                    if Left <= Right then
                        Temp := A(Left);
                        A(Left) := A(Right);
                        A(Right) := Temp;
                        Left := Left + 1;
                        Right := Right - 1;
                    end if;
                end loop;
                if First < Right then
                    Quick_Sort(A, First, Right);
                end if;
                if Left < Last then
                    Quick_Sort(A, Left, Last);
                end if;
            end if;
        end Quick_Sort;

        -- Hybrid sort implementation
        procedure Hybrid_Sort_Helper(A : in out Int_Array; First, Last : Positive) is
            Threshold : constant Positive := 10; -- Threshold for using insertion sort
        begin
            if Last - First < Threshold then
                Insertion_Sort(A, First, Last);
            else
                Quick_Sort(A, First, Last);
            end if;
        end Hybrid_Sort_Helper;

    begin
        Hybrid_Sort_Helper(Arr, Arr'First, Arr'Last);
    end Hybrid_Sort_Array;

    -- Generate random array
    procedure Generate_Random_Array(Arr : out Int_Array) is
		type randRangeInt is new Integer range 1..999999;
		package Rand_Int is new ada.numerics.discrete_random(randRangeInt);
		use Rand_Int;
		Gen : Rand_Int.Generator;
    begin
        Reset(Gen);
        for I in Arr'Range loop
            Arr(I) := Standard.Integer(Random(Gen));
        end loop;
    end Generate_Random_Array;

    -- Print array
    procedure Print_Array(Arr : Int_Array) is
    begin
        for I in Arr'Range loop
            Put(Arr(I));
            Put(" ");
        end loop;
        New_Line;
    end Print_Array;

    -- Main procedure
    Arr : Int_Array(1 .. 9999
    );
begin
    Generate_Random_Array(Arr);
    Put_Line("Array before sorting:");
    Print_Array(Arr);

    Put_Line("Sorting...");
    Hybrid_Sort_Array(Arr);

    Put_Line("Array after sorting:");
    Print_Array(Arr);
end Hybrid_Sort;
