/*
Соответсвие наборов данных и выпавших алгоритмов сортировки:
1-14
2-5
3-3
4-2
*/

#include<iostream>
#include<random>
#include<cstdlib>
#include<fstream>
#include<string>
#include<algorithm>
#include<vector>
using namespace std;

//1 - cписок целых чисел от 0 до 999999 - миллион рандомных целых чисел в диапазоне;
const int N1=1000000;
int INT[N1];
void generate_int(){
    for(int i=0;i<N1;i++) INT[i]=rand()%999999+0;
}

//2 - список из 99999 случайных вещественных чисел в диапазоне [-1, 1];
const int N2=99999;
double REAL[N2];
void generate_real(){
    for(int i=0;i<N2;i++){ 
        REAL[i]=(double)rand()/RAND_MAX;
        if((rand()%2+1)%2==0) REAL[i]*=-1;
    }
}

//3 - 42000 разных точки комплексной плоскости, окружность радиуса 16/4=4;
const int N3=42000;
double COMPLEX_MODULE[N3];
void generate_complex(){
    vector<pair<double,double>> COMPLEX(N3);
    for(int i=0;i<N3;i++) COMPLEX[i]=make_pair((double)rand()/RAND_MAX+0.5,(double)rand()/RAND_MAX+0.5);
    for(int i=0;i<N3;i++){
        COMPLEX_MODULE[i]=sqrt(COMPLEX[i].first*COMPLEX[i].first+
        COMPLEX[i].second*COMPLEX[i].second);
    }
}

//4 - отрывок из книги 10000 символов
const int N4=10000;
string WORDS[N4];
ifstream book("book.txt");
void generate_words(){
    string line="", buf="";
    int count=0,trigger=0;
    char not_accepted[]={',','.','-',';',':','"','!','?',' ','\'','(',')','<',
                         '0','1','2','3','4','5','6','7','8','9'};
    while(getline(book,line)){
        line+=" ";
        string buf="";
        for(int i=0;i<line.length();i++){
            if(find(not_accepted,not_accepted+size(not_accepted),line[i])==
            not_accepted+size(not_accepted)){
                buf+=line[i];
            }
            else{
                if(buf!=""){
                    WORDS[count]=buf;
                    count++;
                    if(count==10000){
                        trigger=1;
                        break;
                    };
                    buf="";
                }
            }
        }
        if(trigger) break;
    }
}

//RADIX SORT
int GetMax(int arr[],int size){
    int max = arr[0];
    for(int i=1; i<size; i++){
        if (arr[i]>max) max = arr[i];
    }
    return max;
}
void CountingSort(int arr[], int size, int div){
    int output[size];
    int count[10] = {0};
    for(int i=0;i<size;i++) count[(arr[i]/div)%10]++;
    for(int i=1;i<10;i++) count[i]+=count[i-1];
    for(int i=size-1;i>=0;i--){
        output[count[(arr[i]/div)%10]-1] = arr[i];
        count[(arr[i]/div)%10]--;
    }
    for(int i=0;i<size;i++) arr[i]=output[i];
}
void RADIX_SORT(int arr[],int size){
    int m = GetMax(arr,size);
    for(int div=1; m/div>0; div*=10){
        CountingSort(arr,size,div);
    }
    cout<<"RADIX SORT: ";
    for(int i=0;i<N1;i++) cout<<arr[i]<<" ";
    cout<<"\n\n";
}

//SHELL SORT
void SHELL_SORT(double arr[],int size){
    for(int gap=size/2; gap>0; gap/=2){
        for(int j=gap;j<size;j++){
            double temp=arr[j];
            int i=0;
            for(i=j;(i>=gap)&&(arr[i-gap]>temp);i-=gap) 
                arr[i]=arr[i-gap];
            arr[i] = temp;
        }
    }
    cout<<"SHELL SORT: ";
    for(int i=0;i<N2;i++) cout<<arr[i]<<" ";
    cout<<"\n\n";
}


//COMB SORT
void COMB_SORT(double* arr,int size){
    int step = size;
    bool is_swaps=true;
    while (step>1 || is_swaps==true){
        step=(int)(step/1.247);
        is_swaps=false;
        for(int i=0;i<size-step;i++){
            if(arr[i]>arr[i+step]){
                swap(arr[i],arr[i+step]);
                is_swaps=true;
            }
        }
    }
    cout<<"COMB SORT: ";
    for(int i=0;i<N3;i++) cout<<arr[i]<<" ";
    cout<<"\n\n";
}

//BUBBLE SORT
void BUBBLE_SORT(string* arr, int size){
    for(int i=0;i<size;i++){
        for(int j=i+1;j<size;j++){
            if(arr[i].length()>arr[j].length()) swap(arr[i],arr[j]);
            else{
                if(arr[i]>arr[j] &&
                arr[i].length()==arr[j].length()) swap(arr[i],arr[j]);
            }
        }
    }
    cout<<"BUBBLE SORT: ";
    for(int i=0;i<N4;i++) cout<<arr[i]<<" ";
    cout<<"\n\n";
}
int main(){
    generate_int();
    generate_real();
    generate_complex();
    generate_words();

    RADIX_SORT(INT,N1);
    SHELL_SORT(REAL,N2);
    COMB_SORT(COMPLEX_MODULE,N3);
    BUBBLE_SORT(WORDS,N4);
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
