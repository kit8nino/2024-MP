with Ada.Text_IO;use Ada.Text_IO;
with Ada.Float_Text_IO; use Ada.Float_Text_IO;
with Ada.Integer_Text_IO; use Ada.Integer_Text_IO;
with Ada.Strings.Unbounded; use Ada.Strings.Unbounded;
with Ada.Text_IO.Unbounded_IO; use Ada.Text_IO.Unbounded_IO;
with Ada.Calendar;            use Ada.Calendar;
with Ada.Calendar.Formatting; use Ada.Calendar.Formatting;
with ada.numerics.discrete_random;
with actor_struct;
with Ada.Containers.Vectors;
with Ada.Containers.Doubly_Linked_Lists;

procedure Work_struct is
	procedure Study is
	type Mark is range 2 .. 5;
	type Lesson is (Russian, Algebra, Geografi,English, Geometry, Chemistry, Physics, DarkDungeon, GachiMuchi, Fizra, History, It, Mp, Music, Literature);
	str : String(1..105);
	type Attestat is
		array (Lesson) of Mark;
	Atestat : constant Attestat := (4,5,3,4,3,2,4,5,4,2,4,5,5,3,5);
	cal, ave: Float;
	len:Ada.Strings.Unbounded.Unbounded_String;
	len2:Ada.Strings.Unbounded.Unbounded_String;
	val : Boolean := True;
		begin
		ave:=0.0;
		cal:=0.0;
		for i in Lesson loop
			len:=len&(Lesson'Image(i));
			cal:=cal+1.0;
			ave:=ave+Standard.Float(Atestat(i));
		end loop;
		ave:=ave/cal;
		Put(ave);
		Put_line("");
		str:=Ada.Strings.Unbounded.To_String(len);
		Put(Ada.Strings.Unbounded.Length(len));
		Put_line("");
		for i of str loop
			for j of Ada.Strings.Unbounded.To_String(len2) loop
				if(i=j)then
					val := False;
				end if;
			end loop;
			if val then
				len2:=len2 & i;
			end if;
			val := True;
		end loop;
		Put_line(len2);
		Put_line("");
	end Study;
	
	procedure Western is
	Now: Time := Clock;
	Now_Year: Year_Number;
	Now_Month: Month_Number;
	Now_Day: Day_Number;
	Now_Seconds : Day_Duration;
	number:Integer;
	ye:Integer;
	mo:Integer;
	da:Integer;
		begin
		Split (Now,
          Now_Year,
          Now_Month,
          Now_Day,
          Now_Seconds);
		Put_line(actor_struct.Name);
		Put_line(actor_struct.Surname);
		Put(actor_struct.Year);
		ye:=Now_Year-actor_struct.Year;
		mo:=Now_Month-actor_struct.Month;
		da:=Now_Day-actor_struct.Day;
		number := (actor_struct.Day + actor_struct.Month*actor_struct.Month + actor_struct.Year) mod 39 + 1;
		Put_line("");
		Put(number);
		Put_line("");
		Put(Standard.Integer(ye*365+mo*31+da));
		Put_line("");
		Put_line("");
	end Western;
	
	procedure Name is
	function tub (Source : String) return Ada.Strings.Unbounded.Unbounded_String
    renames Ada.Strings.Unbounded.To_Unbounded_String;
	type randRange1 is new Integer range 1..20;
	type randRange2 is new Integer range 1..8;
	package Rand_Int1 is new ada.numerics.discrete_random(randRange1);
	use Rand_Int1;
	gen1 : Rand_Int1.Generator;
	package Rand_Int2 is new ada.numerics.discrete_random(randRange2);
	use Rand_Int2;
	gen2 : Rand_Int2.Generator;
	name : randRange1;
	surname : randRange2;
	type namem is array(1..10) of Ada.Strings.Unbounded.Unbounded_String;
	type namew is array(1..10) of Ada.Strings.Unbounded.Unbounded_String;
	type surnamem is array(1..8) of Ada.Strings.Unbounded.Unbounded_String;
	type surnamew is array(1..8) of Ada.Strings.Unbounded.Unbounded_String;
	type allname is array(1..30) of Ada.Strings.Unbounded.Unbounded_String;
	type unicname is array(1..20) of Ada.Strings.Unbounded.Unbounded_String;
	Anamem: namem:=(tub("Ivan"), tub("Alexsandr"), tub("Sergey"), tub("Andrey"), tub("Dmitriy"), tub("Alexey"), tub("Ruslan"), tub("Maksim"), tub("Marat"), tub("Artur"));
	Anamew: namew:=(tub("Maria"), tub("Ekatirina"), tub("Alina"), tub("Elena"), tub("Olga"), tub("Anastasia"), tub("Lily"), tub("Irina"), tub("Marina"), tub("Alsu"));
	Asurnamem: surnamem:=(tub("Ivanov"), tub("Petrov"), tub("Smirnov"), tub("Vacilev"), tub("Safin"), tub("Zaripov"), tub("Khairullin"), tub("Shakirov"));
	Asurnamew: surnamew:=(tub("Ivanova"), tub("Petrova"), tub("Smirnova"), tub("Safina"), tub("Romanova"), tub("Shakirova"), tub("Khairullina"), tub("Zakirova"));
	aname:allname;
	unname:unicname;
	k:Integer;
	N:Ada.Strings.Unbounded.Unbounded_String;
	val : Boolean := True;
	China:Ada.Strings.Unbounded.Unbounded_String:=tub("Zhou Ai-wan");
		begin
		reset(gen1);
		reset(gen2);
		k:=0;
		for i in 1..30 loop
			name:=random(gen1);
			surname:=random(gen2);
			if (name>10) then 
				aname(i):=Anamew(Integer(name)-10)&" "&Asurnamew(integer(surname));
				for j in 1..k loop
					if unname(j)=Anamew(Integer(name)-10) then
						val:=False;
					end if;
				end loop;
				if val then 
					unname(k+1):=Anamew(Integer(name)-10);
					k:=k+1;
				end if;
			else
				aname(i):=Anamem(Integer(name))&" "&Asurnamem(Integer(surname));
				for j in 1..k loop
					if unname(j)=Anamem(Integer(name)) then
						val:=False;
					end if;
				end loop;
				if val then 
					unname(k+1):=Anamem(Integer(name));
					k:=k+1;
				end if;
			end if;
			Put_line(aname(i));
			val:=True;
		end loop;
		N:=Ada.Strings.Unbounded.To_Unbounded_String(Ada.Text_IO.Get_Line);
		aname(Integer'Value(To_String(N))):=China;
		Put_line(" ");
		for i in 1..30 loop
			Put_line(aname(i));
		end loop;
		for i in 1..(k-1) loop
			Put(unname(i)&", ");
		end loop;
		Put(unname(k));
		Put_line(" ");
		Put_line(" ");
	end Name;
	
	procedure Stacke is
	package st is new Ada.Containers.Doubly_Linked_Lists (Ada.Strings.Unbounded.Unbounded_String);
	S:st.List;
	k:Integer:=1;
	begin
	Put_line("      ");
	S.Append(Ada.Strings.Unbounded.To_Unbounded_String(Ada.Text_IO.Get_Line));
	while S.Last_Element/=Ada.Strings.Unbounded.To_Unbounded_String("") loop
		k:=k+1;
		S.Append(Ada.Strings.Unbounded.To_Unbounded_String(Ada.Text_IO.Get_Line));
	end loop;
	for i of reverse S loop
		Put_line(i);
	end loop;
	Put_line(" ");
	end Stacke;
	
	procedure Tamandua is
	function tub (Source : String) return Ada.Strings.Unbounded.Unbounded_String
    renames Ada.Strings.Unbounded.To_Unbounded_String;
	type String is array (Positive range <>) of Character;
	type pm is array (Positive range <>) of Ada.Strings.Unbounded.Unbounded_String;
	S:String(1..9):=('F','u','r','r','y',' ','a','s','s');
	k,j:Integer;
	prom:pm(1..10);
	bin:Ada.Strings.Unbounded.Unbounded_String;
	begin
	for i in S'Range loop
		Put(S(i));
	end loop;
	Put_line(" ");
	for i in  S'Range loop
		j:=Character'Pos(S(i));
		k:=1;
		prom:=(tub(""),tub(""),tub(""),tub(""),tub(""),tub(""),tub(""),tub(""),tub(""),tub(""));
		while (j>0) loop
			prom(k):=prom(k) &( Integer'Image (j mod 2));
			j:=j /2;
			k:=k+1;
		end loop;
		for l in reverse prom'Range loop
			bin:=bin&prom(l);
		end loop;
	end loop;
	Put_line(bin);
	end Tamandua;

	procedure Linklist is
	function tub (Source : String) return Ada.Strings.Unbounded.Unbounded_String
	renames Ada.Strings.Unbounded.To_Unbounded_String;
	package Number_Lists   is new Ada.Containers.Doubly_Linked_Lists (Ada.Strings.Unbounded.Unbounded_String);
	package Number_Sorting is new Number_Lists.Generic_Sorting;
	use Number_Lists, Ada.Text_Io;
	List : Number_Lists.List;
	N:Ada.Strings.Unbounded.Unbounded_String;
	ser :Integer;
	S:Ada.Strings.Unbounded.Unbounded_String;
	begin
	List.Append (tub("Большая Пысса"));List.Append (tub("Большие Пупсы"));List.Append (tub("Дешевки"));List.Append (tub("Такое"));List.Append (tub("Кокаиновые горы"));
	N:=Ada.Strings.Unbounded.To_Unbounded_String(Ada.Text_IO.Get_Line);
	ser:=(Integer'Value(To_String(N)));
	for E of List loop
		put_line(E);
	end loop;
	for E of List loop
		if (ser=1) then
			S:=E;
		end if;
		ser:=ser-1;
	end loop;
	List.Insert(Before => List.Find(S),
							New_Item => To_Unbounded_String("Конец"));
	put_line("");
	for E of List loop
		put_line(E);
	end loop;
	end Linklist;
	
	begin
	
	Study;
	Western;
	Name;
	Tamandua;
	
	Stacke;
	Linklist;
end Work_struct;
--test = ["Большая Пысса", "Большие Пупсы", "Манды", "Дешевки", 'Новый русский спуск', 'Такое', 'Тухлянка ',
--        'Баклань', 'Лохово', 'Большое', 'Струйкино',
--        'Овнище', 'Дно', 'Трусово', 'Кокаиновые горы', 'Косяковка ',
--        'Куриловка', 'Ширяево', 'Ломки', 'Большой', 'Куяш', 'Иннах']
