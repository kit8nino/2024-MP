with Ada.Text_IO; use Ada.Text_IO;
with Ada.Float_Text_IO; use Ada.Float_Text_IO;
with Ada.Numerics.Float_Random; use Ada.Numerics.Float_Random;
with Ada.Containers.Vectors; use Ada.Containers;

procedure Radix_Sort is
    type Real_Array is array (Positive range <>) of Float;

    procedure Radix_Sort_Array(Arr : in out Real_Array) is
        package Real_Vector_IO is new Ada.Containers.Vectors.Generic_IO(Float, Float_IO);
        use Real_Vector_IO;

        package Real_Vector is new Vectors(Float);
        use Real_Vector;

        -- Counting sort for real numbers based on the specified digit position
        procedure Counting_Sort(Arr : in out Real_Vector.Vector; Exp : Float) is
            Count : array(0..9) of Integer := (others => 0);
            Output : Real_Vector.Vector(Arr'Range);
        begin
            for I in Arr'Range loop
                declare
                    MSB : Integer := Integer(Arr(I) * 10.0**Exp) mod 10;
                begin
                    Count(MSB) := Count(MSB) + 1;
                end;
            end loop;

            for I in 1..9 loop
                Count(I) := Count(I) + Count(I - 1);
            end loop;

            for I in reverse Arr'Range loop
                declare
                    MSB : Integer := Integer(Arr(I) * 10.0**Exp) mod 10;
                begin
                    Output(Count(MSB) - 1) := Arr(I);
                    Count(MSB) := Count(MSB) - 1;
                end;
            end loop;

            Arr := Output;
        end Counting_Sort;

        -- Find the maximum number of digits after the decimal point
        function Max_Decimal_Digits(Arr : Real_Vector.Vector) return Integer is
            Max : Integer := 0;
        begin
            for I in Arr'Range loop
                declare
                    Decimals : Integer := Integer(Float'Floor(Arr(I)))'Length;
                begin
                    if Decimals > Max then
                        Max := Decimals;
                    end if;
                end;
            end loop;
            return Max;
        end Max_Decimal_Digits;

    begin
        declare
            Max_Decimals : Integer := Max_Decimal_Digits(To_Vector(Arr));
            Exp : Float := -1.0;
        begin
            while Exp >= -Max_Decimals loop
                Counting_Sort(To_Vector(Arr), -Exp);
                Exp := Exp - 1.0;
            end loop;
        end;
    end Radix_Sort_Array;

    -- Generate random real array
    procedure Generate_Random_Real_Array(Arr : out Real_Array) is
        Gen : Generator;
    begin
        Reset(Gen);
        for I in Arr'Range loop
            Arr(I) := Random(Gen);
