with Ada.Text_IO;use Ada.Text_IO;
with Ada.Float_Text_IO;use Ada.Float_Text_IO;
with Ada.Integer_Text_IO;use Ada.Integer_Text_IO;
with Ada.Numerics.Elementary_Functions;use Ada.Numerics.Elementary_Functions;
with Ada.Numerics.Generic_Elementary_Functions;
with Ada.Numerics;use Ada.Numerics;
procedure Radar_Simulation is

   type Coordinate is record
      X : Float;
      Y : Float;
      Z : Float;
   end record;

   type Velocity is record
      Vx : Float;
      Vy : Float;
      Vz : Float;
   end record;

   type Spherical_Coordinate is record
      R : Float;
      Theta : Float; -- Azimuth angle
      Phi : Float;   -- Elevation angle
   end record;

   package Singleton_Radar is
      function Instance return Coordinate;
   private
      Radar : Coordinate := (0.0, 0.0, 0.0);
   end Singleton_Radar;

   package body Singleton_Radar is
      function Instance return Coordinate is
      begin
         return Radar;
      end Instance;
   end Singleton_Radar;

   type FlyingObject is tagged record
      Position : Coordinate;
      Velo : Velocity;
   end record;

   procedure Update_Position (Obj : in out FlyingObject; Time : Float) is
   begin
      Obj.Position.X := Obj.Position.X + Obj.Velo.Vx * Time;
      Obj.Position.Y := Obj.Position.Y + Obj.Velo.Vy * Time;
      Obj.Position.Z := Obj.Position.Z + Obj.Velo.Vz * Time;
   end Update_Position;

   function To_Spherical (Radar : Coordinate; Obj : Coordinate) return Spherical_Coordinate is
      Dx, Dy, Dz, R, Theta, Phi : Float;
   begin
      Dx := Obj.X - Radar.X;
      Dy := Obj.Y - Radar.Y;
      Dz := Obj.Z - Radar.Z;
      R := Sqrt(Dx*Dx + Dy*Dy + Dz*Dz);
      Theta := Arctan(Dy, Dx) * (180.0 / Pi);  -- Convert radians to degrees
      Phi := Arctan(Dz, Sqrt(Dx*Dx + Dy*Dy)) * (180.0 / Pi);  -- Convert radians to degrees
      return (R, Theta, Phi);
   end To_Spherical;

   procedure Print_Spherical_Coordinate (Coord : Spherical_Coordinate) is
   begin
      Put_Line("R: " & Float'Image(Coord.R) & " m, Theta: " & Float'Image(Coord.Theta) & " degrees, Phi: " & Float'Image(Coord.Phi) & " degrees");
   end Print_Spherical_Coordinate;

   Radar_Position : Coordinate := Singleton_Radar.Instance;

   procedure Main is
      N : Integer;
      Time : Float;
   begin
      Put("Enter the number of flying objects: ");
      Get(Item =>N);
      
      declare
         Flying_Objects : array(1 .. N) of FlyingObject;
      begin
         for I in 1 .. N loop
            Put("Enter coordinates (X, Y, Z) and velocities (Vx, Vy, Vz) for object " & Integer'Image(I) & ": ");
            Get(Item => Flying_Objects(I).Position.X);
            Get(Item => Flying_Objects(I).Position.Y);
            Get(Item => Flying_Objects(I).Position.Z);
            Get(Item => Flying_Objects(I).Velo.Vx);
            Get(Item => Flying_Objects(I).Velo.Vy);
            Get(Item => Flying_Objects(I).Velo.Vz);
         end loop;

         Put_Line("Current spherical coordinates of objects relative to radar:");
         for I in 1 .. N loop
            Print_Spherical_Coordinate(To_Spherical(Radar_Position, Flying_Objects(I).Position));
         end loop;

         Put("Enter the time in seconds: ");
         Get(Item => Time);

         for I in 1 .. N loop
            Update_Position(Flying_Objects(I), Time);
         end loop;

         Put_Line("Spherical coordinates of objects relative to radar after " & Float'Image(Time) & " seconds:");
         for I in 1 .. N loop
            Print_Spherical_Coordinate(To_Spherical(Radar_Position, Flying_Objects(I).Position));
         end loop;
      end;
   end Main;
begin
   Main;
end Radar_Simulation;
