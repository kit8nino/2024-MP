with Ada.Text_IO; use Ada.Text_IO;
with Ada.Numerics.Complex_Types;
with Ada.Numerics.Elementary_Functions;

procedure Complex_Comb_Sort is
    -- Type for complex numbers
    package Complex_IO is new Ada.Text_IO.Float_IO (Num => Ada.Numerics.Complex_Types.Complex);
    use Ada.Numerics.Complex_Types;
    
    type Complex_Array is array (Positive range <>) of Complex;
    
    -- Swap two elements of an array
    procedure Swap (A : in out Complex_Array; I, J : in Positive) is
        Temp : Complex := A(I);
    begin
        A(I) := A(J);
        A(J) := Temp;
    end Swap;
    
    -- Comb sort algorithm for complex numbers
    procedure Comb_Sort (A : in out Complex_Array) is
        Gap : Natural := A'Length;
        Swapped : Boolean := True;
        J : Natural;
    begin
        while Gap > 1 or Swapped loop
            Gap := Gap * 10 / 13;
            if Gap = 9 or Gap = 10 then
                Gap := 11;
            end if;
            Swapped := False;
            for I in A'First .. A'Last - Gap loop
                J := I + Gap;
                if Ada.Numerics.Elementary_Functions.Modulus(A(I)) > Ada.Numerics.Elementary_Functions.Modulus(A(J)) then
                    Swap(A, I, J);
                    Swapped := True;
                end if;
            end loop;
        end loop;
    end Comb_Sort;

    -- Main program
    Arr_Size : constant Positive := 42000;
    Arr : Complex_Array(1..Arr_Size);

begin
    -- Initialize array with random complex numbers
    for I in Arr'Range loop
        Arr(I) := Complex(Arr_Size - I, Arr_Size - I);
    end loop;

    -- Sort the array
    Comb_Sort(Arr);

    -- Print the sorted array
    for I in Arr'Range loop
        Complex_IO.Put(Arr(I));
        New_Line;
    end loop;
end Complex_Comb_Sort;
