with Ada.Text_IO; use Ada.Text_IO;
with Ada.Containers.Doubly_Linked_Lists;
--with Ada.Containers.Doubly_Linked_Lists.Cursors;

procedure Maze_Solver is
   -- Define types for maze coordinates and maze map
   type Coordinate is record
      X : Integer;
      Y : Integer;
   end record;

   type Maze_Array is array (Positive range <>, Positive range <>) of Character;

   -- Constants for maze symbols
   Wall    : constant Character := '#';
   Avatar  : constant Character := 'A';
   Key     : constant Character := 'K';
   Exi    : constant Character := 'E';
   Visited : constant Character := '.';

   -- Read maze from file
   procedure Read_Maze_From_File (File_Name : String; Maze : out Maze_Array) is
      Input_File : File_Type;
   begin
      Open (Input_File, In_File, File_Name);
      for I in Maze'Range (1) loop
         for J in Maze'Range (2) loop
            Get (Input_File, Maze(I, J));
         end loop;
         New_Line;
      end loop;
      Close (Input_File);
   exception
      when others =>
         raise Program_Error;
   end Read_Maze_From_File;

   -- Write maze to file
   procedure Write_Maze_To_File (File_Name : String; Maze : Maze_Array) is
      Output_File : File_Type;
   begin
      Open (Output_File, Out_File, File_Name);
      for I in Maze'Range (1) loop
         for J in Maze'Range (2) loop
            Put (Output_File, Maze(I, J));
         end loop;
         New_Line (Output_File);
      end loop;
      Close (Output_File);
   exception
      when others =>
         raise Program_Error;
   end Write_Maze_To_File;

   -- Depth-first search for finding the key
   procedure DFS_Find_Key (Maze       : in out Maze_Array;
                           Current    : in Coordinate;
                           Key_Coord  : out Coordinate) is
      Visited_Cells : Ada.Containers.Doubly_Linked_Lists.List;
      Current_Coord : Coordinate := Current;
   begin
      Ada.Containers.Doubly_Linked_Lists.Init (Visited_Cells);
      loop
         Maze(Current_Coord.X, Current_Coord.Y) := Visited;
         if Maze(Current_Coord.X, Current_Coord.Y + 1) /= Wall then
            Key_Coord := Current_Coord;
            exit;
         elsif Maze(Current_Coord.X + 1, Current_Coord.Y) /= Wall then
            Key_Coord := Current_Coord;
            exit;
         elsif Maze(Current_Coord.X, Current_Coord.Y - 1) /= Wall then
            Key_Coord := Current_Coord;
            exit;
         elsif Maze(Current_Coord.X - 1, Current_Coord.Y) /= Wall then
            Key_Coord := Current_Coord;
            exit;
         end if;

         if Maze(Current_Coord.X, Current_Coord.Y + 1) /= Wall and then
            Maze(Current_Coord.X, Current_Coord.Y + 1) /= Visited then
            Ada.Containers.Doubly_Linked_Lists.Append (Visited_Cells, Current_Coord);
            Current_Coord.Y := Current_Coord.Y + 1;
         elsif Maze(Current_Coord.X + 1, Current_Coord.Y) /= Wall and then
            Maze(Current_Coord.X + 1, Current_Coord.Y) /= Visited then
            Ada.Containers.Doubly_Linked_Lists.Append (Visited_Cells, Current_Coord);
            Current_Coord.X := Current_Coord.X + 1;
         elsif Maze(Current_Coord.X, Current_Coord.Y - 1) /= Wall and then
            Maze(Current_Coord.X, Current_Coord.Y - 1) /= Visited then
            Ada.Containers.Doubly_Linked_Lists.Append (Visited_Cells, Current_Coord);
            Current_Coord.Y := Current_Coord.Y - 1;
         elsif Maze(Current_Coord.X - 1, Current_Coord.Y) /= Wall and then
            Maze(Current_Coord.X - 1, Current_Coord.Y) /= Visited then
            Ada.Containers.Doubly_Linked_Lists.Append (Visited_Cells, Current_Coord);
            Current_Coord.X := Current_Coord.X - 1;
         elsif Ada.Containers.Doubly_Linked_Lists.Length (Visited_Cells) > 0 then
            Current_Coord := Ada.Containers.Doubly_Linked_Lists.Last_Element (Visited_Cells).Element;
            Ada.Containers.Doubly_Linked_Lists.Delete_Last (Visited_Cells);
         else
            exit; -- No path to key found
         end if;
      end loop;
   end DFS_Find_Key;

   -- A* search for finding the optimal path to the exit
   procedure AStar_Find_Exit (Maze      : in out Maze_Array;
                               Key_Coord : in Coordinate;
                               Exit_Coord: out Coordinate) is
      -- Define a type for storing path costs
      type Cost is record
         G : Integer; -- Cost from start to current node
         H : Integer; -- Heuristic (estimated cost from current node to goal)
      end record;

      -- Define a type for representing a node in the search
      type Node is record
         Coords : Coordinate;
         Parent : Coordinate;
         Cost   : Cost;
      end record;

      -- Define a list of open nodes
      package Open_Nodes is new Ada.Containers.Doubly_Linked_Lists (Element_Type => Node);
      use Open_Nodes;

      -- Define a list of closed nodes
      package Closed_Nodes is new Ada.Containers.Doubly_Linked_Lists (Element_Type => Coordinate);
      use Closed_Nodes;

      function Manhattan_Distance (A, B : Coordinate) return Integer is
      begin
         return Standard.Integer(Abs (A.X - B.X)) + Standard.Integer(Abs (A.Y - B.Y));
      end Manhattan_Distance;

      -- Calculate cost of moving from one node to another
      function Move_Cost (A, B : Coordinate) return Integer is
      begin
         if A.X = B.X or A.Y = B.Y then
            return 1;
         else
            return 2; -- Diagonal movement
         end if;
      end Move_Cost;

      -- Check if a coordinate is in open nodes list
      function In_Open_List (Coord : Coordinate) return Boolean is
      begin
         return Exists (Item => Coord, Container => Open_Nodes);
      end In_Open_List;

      -- Check if a coordinate is in closed nodes list
      function In_Closed_List (Coord : Coordinate) return Boolean is
      begin
         return Exists (Item => Coord, Container => Closed_Nodes);
      end In_Closed_List;

      -- Calculate F cost of a node
      function F_Cost (N : Node) return Integer is
      begin
         return N.Cost.G + N.Cost.H;
      end F_Cost;

      -- Find the node with the lowest F cost in open nodes list
      function Lowest_F_Cost_Node return Node is
         Lowest : Node := First_Element;
      begin
         declare
            Cursor : Cursors.Cursor := First_Cursor;
         begin
            while Has_Element (Cursor) loop
               if F_Cost (Element (Cursor)) < F_Cost (Lowest) then
                  Lowest := Element (Cursor);
               end if;
               Next (Cursor);
            end loop;
         end;
         return Lowest;
      end Lowest_F_Cost_Node;

      -- Trace back the path from exit to start
      procedure Trace_Path (Last_Node : Node) is
         Current : Coordinate := Last_Node.Coords;
      begin
         loop
            Maze(Current.X, Current.Y) := Visited;
            if Current /= Key_Coord then
               Maze(Current.X, Current.Y) := ',';
            end if;
            exit when Current = Key_Coord;
            Current := Last_Node.Parent;
         end loop;
      end Trace_Path;

      Start     : Coordinate := Key_Coord;
      Start_Cost: Cost;
      Current   : Node;
      Neighbor  : Node;
   begin
      Start_Cost.G := 0;
      Start_Cost.H := Manhattan_Distance (Start, Exit_Coord);
      Current.Coords := Start;
      Current.Parent := Start;
      Current.Cost := Start_Cost;

      Insert_Last (Open_Nodes, Current);

      while not Is_Empty loop
         Current := Lowest_F_Cost_Node;
         Delete (Open_Nodes, Current);

         if Current.Coords = Exit_Coord then
            Trace_Path (Current);
            exit;
         end if;

         declare
            Neighbor_Coord : Coordinate;
         begin
            -- Generate neighbors
            Neighbor_Coord := Current.Coords;
            Neighbor_Coord.Y := Neighbor_Coord.Y + 1;
            if Maze(Neighbor_Coord.X, Neighbor_Coord.Y) /= Wall and then not In_Closed_List (Neighbor_Coord) then
               Neighbor.Coords := Neighbor_Coord;
               Neighbor.Parent := Current.Coords;
               Neighbor.Cost.G := Current.Cost.G + Move_Cost (Current.Coords, Neighbor.Coords);
               Neighbor.Cost.H := Manhattan_Distance (Neighbor.Coords, Exit_Coord);
               if not In_Open_List (Neighbor.Coords) or else Neighbor.Cost.G < Current.Cost.G then
                  Insert_Last (Open_Nodes, Neighbor);
               end if;
            end if;

            Neighbor_Coord := Current.Coords;
            Neighbor_Coord.X := Neighbor_Coord.X + 1;
            if Maze(Neighbor_Coord.X, Neighbor_Coord.Y) /= Wall and then not In_Closed_List (Neighbor_Coord) then
               Neighbor.Coords := Neighbor_Coord;
               Neighbor.Parent := Current.Coords;
               Neighbor.Cost.G := Current.Cost.G + Move_Cost (Current.Coords, Neighbor.Coords);
               Neighbor.Cost.H := Manhattan_Distance (Neighbor.Coords, Exit_Coord);
               if not In_Open_List (Neighbor.Coords) or else Neighbor.Cost.G < Current.Cost.G then
                  Insert_Last (Open_Nodes, Neighbor);
               end if;
            end if;

            Neighbor_Coord := Current.Coords;
            Neighbor_Coord.Y := Neighbor_Coord.Y - 1;
            if Maze(Neighbor_Coord.X, Neighbor_Coord.Y) /= Wall and then not In_Closed_List (Neighbor_Coord) then
               Neighbor.Coords := Neighbor_Coord;
               Neighbor.Parent := Current.Coords;
               Neighbor.Cost.G := Current.Cost.G + Move_Cost (Current.Coords, Neighbor.Coords);
               Neighbor.Cost.H := Manhattan_Distance (Neighbor.Coords, Exit_Coord);
               if not In_Open_List (Neighbor.Coords) or else Neighbor.Cost.G < Current.Cost.G then
                  Insert_Last (Open_Nodes, Neighbor);
               end if;
            end if;

            Neighbor_Coord := Current.Coords;
            Neighbor_Coord.X := Neighbor_Coord.X - 1;
            if Maze(Neighbor_Coord.X, Neighbor_Coord.Y) /= Wall and then not In_Closed_List (Neighbor_Coord) then
               Neighbor.Coords := Neighbor_Coord;
               Neighbor.Parent := Current.Coords;
               Neighbor.Cost.G := Current.Cost.G + Move_Cost (Current.Coords, Neighbor.Coords);
               Neighbor.Cost.H := Manhattan_Distance (Neighbor.Coords, Exit_Coord);
               if not In_Open_List (Neighbor.Coords) or else Neighbor.Cost.G < Current.Cost.G then
                  Insert_Last (Open_Nodes, Neighbor);
               end if;
            end if;
         end;
      end loop;
   end AStar_Find_Exit;

   -- Main procedure
   Avatar_Coord : Coordinate;
   Key_Coord    : Coordinate;
   Exit_Coord   : Coordinate;
   Maze         : Maze_Array (1..20, 1..20);
begin
   Read_Maze_From_File ("maze-for-u.txt", Maze);

   -- Find the avatar and the key coordinates
   for I in Maze'Range (1) loop
      for J in Maze'Range (2) loop
         if Maze(I, J) = Avatar then
            Avatar_Coord.X := I;
            Avatar_Coord.Y := J;
         elsif Maze(I, J) = Key then
            Key_Coord.X := I;
            Key_Coord.Y := J;
         elsif Maze(I, J) = Exi then
            Exit_Coord.X := I;
            Exit_Coord.Y := J;
         end if;
      end loop;
   end loop;

   Ada.Text_IO.Put_Line ("Avatar coordinates: " & Integer'Image (Avatar_Coord.X) & "," & Integer'Image (Avatar_Coord.Y));
   Ada.Text_IO.Put_Line ("Key coordinates: " & Integer'Image (Key_Coord.X) & "," & Integer'Image (Key_Coord.Y));
   Ada.Text_IO.Put_Line ("Exit coordinates: " & Integer'Image (Exit_Coord.X) & "," & Integer'Image (Exit_Coord.Y));

   -- Find path from avatar to key using DFS
   DFS_Find_Key (Maze, Avatar_Coord, Key_Coord);

   -- Find path from key to exit using A*
   AStar_Find_Exit (Maze, Key_Coord, Exit_Coord);

   -- Mark key and exit on the maze
   Maze(Key_Coord.X, Key_Coord.Y) := '*';
   Maze(Exit_Coord.X, Exit_Coord.Y) := '*';

   -- Write the modified maze to file
   Write_Maze_To_File ("maze-for-me-done.txt", Maze);
end Maze_Solver;
