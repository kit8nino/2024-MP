#include<iostream>
#include<vector>
using namespace std;

class Radar{
private:
	static Radar* instance;
	Radar(){};
public:
	static Radar* getInstance(){
		if (instance==nullptr){
			instance = new Radar();
		}
		return instance;
	}
	double x,y,z;
	void set_coords(double x,double y,double z){
		this->x=x;
		this->y=y;
		this->z=z;
	}
};
Radar* Radar::instance = nullptr;
Radar* radar = Radar::getInstance();

class Object{
public:
	Object() {};
	double x,y,z;
	double vx,vy,vz;

	void set_coords(double x,double y, double z){
		this->x=x;
		this->y=y;
		this->z=z;
	}
	void set_velocitry(double vx,double vy, double vz){
		this->vx=vx;
		this->vy=vy;
		this->vz=vz;
	}
};

vector<Object*> objects;
void start_input(Radar* radar){
	double x,y,z;
	cout<<"Enter coords of Radar: \n";
	cout<<"X = "; cin>>x;
	cout<<"Y = "; cin>>y;
	cout<<"Z = "; cin>>z;
	radar->set_coords(x,y,z);

	int n;
	cout<<"\nEnter number of objects: "; cin>>n;
	for(int i=0;i<n;i++){
		cout<<"\nObject "<<i+1<<".\n";
		cout<<"\nEnter x,y,z coords of object: "; cin>>x>>y>>z;
		Object* now = new Object;
		now->set_coords(x,y,z);

		double vx,vy,vz;
		cout<<"Enter vx,vy,vz coords of object: "; cin>>vx>>vy>>vz;
		now->set_velocitry(vx,vy,vz);

		objects.push_back(now);
	}
}
void get_spherical(Radar* radar, Object* object, int count){
	double x = object->x -radar->x;
	double y = object->y -radar->y;
	double z = object->z -radar->z;
	cout<<"Object "<<count<<": X = "<<x<<", Y = "<<y<<", Z = "<<z<<"\n";
}

void show_spherical_coords_now(Radar* radar){
	int i=0;
	cout<<"\nSpherical coords for objects in relation to Radar: \n";
	for(auto x:objects){
		i++;
		get_spherical(radar,x,i);
	}
}

void get_spherical_through_time(Radar* radar, Object* object, int count, int time){
	double x_then = object->x+=object->vx*time;
	double y_then = object->y+=object->vx*time;
	double z_then = object->z+=object->vx*time;
	get_spherical(radar,object,count);
}

void show_spherical_coords_through_time(Radar* radar){
	int time, i=0;
	cout<<"\nEnter time: "; cin>>time;
	cout<<"\nSpherical coords for objects in relation to Radar through time: \n";
	for(auto x:objects){
		i++;
		get_spherical_through_time(radar,x,i,time);
	}
};

int main(){
	start_input(radar);
	show_spherical_coords_now(radar);
	show_spherical_coords_through_time(radar);
}

/*
███╗░░░███╗░█████╗░██████╗░███████╗  ██████╗░██╗░░░██╗
████╗░████║██╔══██╗██╔══██╗██╔════╝  ██╔══██╗╚██╗░██╔╝
██╔████╔██║███████║██║░░██║█████╗░░  ██████╦╝░╚████╔╝░
██║╚██╔╝██║██╔══██║██║░░██║██╔══╝░░  ██╔══██╗░░╚██╔╝░░
██║░╚═╝░██║██║░░██║██████╔╝███████╗  ██████╦╝░░░██║░░░
╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═════╝░╚══════╝  ╚═════╝░░░░╚═╝░░░

██████╗░██╗███╗░░░███╗░█████╗░░██████╗██╗██╗░░██╗██╗░░██╗░██████╗
██╔══██╗██║████╗░████║██╔══██╗██╔════╝██║██║░██╔╝██║░██╔╝██╔════╝
██║░░██║██║██╔████╔██║███████║╚█████╗░██║█████═╝░█████═╝░╚█████╗░
██║░░██║██║██║╚██╔╝██║██╔══██║░╚═══██╗██║██╔═██╗░██╔═██╗░░╚═══██╗
██████╔╝██║██║░╚═╝░██║██║░░██║██████╔╝██║██║░╚██╗██║░╚██╗██████╔╝
╚═════╝░╚═╝╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═════╝░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░

░█████╗░███████╗
██╔══██╗██╔════╝
███████║█████╗░░
██╔══██║██╔══╝░░
██║░░██║██║░░░░░
╚═╝░░╚═╝╚═╝░░░░░
                     .ed"""" """$$$$be.
                   -"           ^""**$$$e.
                 ."                   '$$$c
                /                      "4$$b
               d  3                      $$$$
               $  *                   .$$$$$$
              .$  ^c           $$$$$e$$$$$$$$.
              d$L  4.         4$$$$$$$$$$$$$$b
              $$$$b ^ceeeee.  4$$ECL.F*$$$$$$$
  e$""=.      $$$$P d$$$$F $ $$$$$$$$$- $$$$$$
 z$$b. ^c     3$$$F "$$$$b   $"$$$$$$$  $$$$*"      .=""$c
4$$$$L        $$P"  "$$b   .$ $$$$$...e$$        .=  e$$$.
^*$$$$$c  %..   *c    ..    $$ 3$$$$$$$$$$eF     zP  d$$$$$
  "**$$$ec   "   %ce""    $$$  $$$$$$$$$$*    .r" =$$$$P""
        "*$b.  "c  *$e.    *** d$$$$$"L$$    .d"  e$$***"
          ^*$$c ^$c $$$      4J$$$$$% $$$ .e*".eeP"
             "$$$$$$"'$=e....$*$$**$cz$$" "..d$*"
               "*$$$  *=%4.$ L L$ P3$$$F $$$P"
                  "$   "%*ebJLzb$e$$$$$b $P"
                    %..      4$$$$$$$$$$ "
                     $$$e   z$$$$$$$$$$%
                      "*$c  "$$$$$$$P"
                       ."""*$$$$$$$$bc
                    .-"    .$***$$$"""*e.
                 .-"    .e$"     "*$c  ^*b.
          .=*""""    .e$*"          "*bc  "*$e..
        .$"        .z*"               ^*$e.   "*****e.
        $$ee$c   .d"                     "*$.        3.
        ^*$E")$..$"                         *   .ee==d%
           $.d$$$*                           *  J$$$e*
            """""                              "$$$"
*/
