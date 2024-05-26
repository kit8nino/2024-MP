#include<iostream>
#include<algorithm>
#include<iomanip>
#include<map>
#include<tuple>
#include<list>
#include<bitset>
#include<ctime>
#include<queue>
#include<vector>
using namespace std;

map<string,short int> attestat{
    {"Математика",5},
    {"Физика",5},
    {"Информатика",5},
    {"Геометрия",5},
    {"Физкультура",5},
    {"Музыка",5},
    {"Технологии",5},
    {"Изо",5},
    {"Английский язык",5},
    {"История",2},
    {"Литература",2},
    {"Русский язык",2},
    {"География",2},
    {"Обществознание",2},
    {"Testpredmet",5}
};

tuple<string,string,string> actor={
    "Рэндольф", "Скотт", "23.01.1898"
};

vector <pair<string,string>> users={
    {"Иван","Иванов"},
    {"Иван","Петров"},
    {"Иван","Смирнов"},
    {"Андрей","Кузнецов"},
    {"Дмитрий","Сергеев"},
    {"Иван","Иванов"},
    {"Дмитрий","Кузнецов"},
    {"Иван","Сергеев"},
    {"Владимир","Иванов"}
};

string tamandua = "Балумба";

void question_1(){
    short int sum=0;
    for(auto x:attestat) sum+=x.second;
    cout<<"Средняя оценка в аттестате: "<<
    fixed<<setprecision(1)<<(double)sum/attestat.size()<<"\n\n";

}

void question_2(){
    map<string,int> find_uniq;
    for(auto x:users) find_uniq[x.first]++;
    if(find_uniq.size()!=0){
        cout<<"Уникальные имена: ";
        for(auto x:find_uniq) if(x.second==1) cout<<x.first<<" ";
        cout<<"\n\n";
    }
    else cout<<"Уникальных имен нет!\n\n";
}

void question_3(){
    short int sum=0;
    for(auto x:attestat) sum+=x.first.length();
    cout<<"Общая длина всех названий предметов: "<<sum<<"\n\n";
}

void question_4(){
    map<char,int> find_uniq;
    for(auto x:attestat){
        for(auto y:x.first) find_uniq[y]++;
    }
    if(find_uniq.size()!=0){
        cout<<"Уникальные буквы в названиях предметов: ";
        for(auto x:find_uniq) if(x.second==1) cout<<x.first<<" ";
        cout<<"\n\n";
    }
    else cout<<"Уникальных букв в названиях предметов нет!\n\n";
}

void question_5(){
    string ans="";
    for(auto x:tamandua){
        string buf=bitset<8>(int(x)-48).to_string();
        ans+=buf;
    }
    cout<<"Имя питомца в бинарном виде: "<<ans<<"\n\n";
}

void question_6(){
    short int dateofbirth[3];
    string buf="";
    short int i=0;
    for(auto x:get<2>(actor))
        if(x!='.') buf+=x;
        else {
            dateofbirth[i]=atoi(buf.c_str());
            i++;
            buf="";
        }
    dateofbirth[2]=atoi(buf.c_str());
    time_t now = time(0);
    tm* date=localtime(&now);
    if(dateofbirth[0]>date->tm_mday){
        cout<<"Количество дней от даты рождения: "<<
        (date->tm_year+1900-dateofbirth[2])*365+
        (date->tm_mon-dateofbirth[1]+1)*30+
        dateofbirth[0]-date->tm_mday<<"\n\n";
    }
    else cout<<"Количество дней от даты рождения: "<<
        (date->tm_year+1900-dateofbirth[2])*365+
        (date->tm_mon-dateofbirth[1]+1)*30
        -dateofbirth[0]+date->tm_mday<<"\n\n";
}

void question_7(){
    queue<string> FIFO;
    cout<<"Введите названия стройматериалов (для остановки введите stop): \n";
    while(true){
        string in;
        cin>>in;
        if(in=="stop"){
            if(FIFO.size()==0) cout<<"Очередь пуста!\n\n";
            else{
                cout<<"\nВведенные стройматериалы: ";
                while(!FIFO.empty()){
                    cout<<FIFO.front()<<" ";
                    FIFO.pop();
                }
                cout<<"\n\n";
            }
            break;
        }
        FIFO.push(in);
    }
}

void question_8(){
    sort(users.begin(),users.end());
    cout<<"Введите имя для замены: ";
    string rep,imp = "Цзи Цзэ";
    int trig=0;
    cin>>rep;
    for(int i=0;i<users.size();i++){
        if(users[i].first==rep){
            trig=1;
            users[i].first=imp;
        }
    }
    if(trig==0) cout<<"Введенного имени нет в списке имен и фамилий!\n";
    cout<<"\nОбновленный список имен и фамилий: \n";
    for(auto x:users) cout<<x.first<<" "<<x.second<<"\n";
}

class Node{
    public:
    string data;
    Node* next;
    Node(string data){
        this->data = data;
        this->next = NULL;
    }
};
class LinkedList{
    public:
    Node *head, *tail;
    LinkedList(){
        this->head = this->tail = NULL;
    }
    void push_back(string data){
        Node* node = new Node(data);
        if(head==NULL) head = node;
        if(tail!=NULL) tail->next=node;
        tail = node;
    }
    Node* getAt(int k){
        if(k<0) return NULL;
        Node* node = head;
        int n=0;
        while(node && n !=k && node->next){
            node = node->next;
            n++;
        }
        return (n == k)?node:NULL;
    }
    void insert(int k,string data){
        Node* left = getAt(k);
        if (left == NULL) return;
        Node* right = left->next;
        Node* node = new Node(data);
        left->next = node;
        node->next = right;
        if(right == NULL) tail = node;
    }
    void _delete(string data,int n){
        for(int k=0;k<n;k++){
            Node* node=getAt(k);
            if(node->data==data){
                if(k==0){
                    head=node->next;
                    delete node;
                    break;
                }
                if(k==n-1){
                    Node* nodepred = getAt(k-1);
                    nodepred->next=NULL;
                    delete node;
                    break;
                }
                Node* nodepred = getAt(k-1);
                nodepred->next=node->next;
                delete node;
                break;
            }
        } 
    }
    void print(){
        for(Node* node = head;node !=NULL;node=node->next)
        cout<<"\""<<node->data<<"\""<<" ";
    cout<<"\n";
    }

};

void question_9(){
    vector<string> data{
        "Большая Пысса", "Большие Пупсы", "Манды", 
        "Дешевки", "Новый русский спуск", "Такое", "Тухлянка",
        "Баклань", "Лохово", "Большое", "Струйкино","Иннах"
    };
    LinkedList ex;
    for(auto x:data) ex.push_back(x);
    cout<<"\nИзначальный связный список:\n";
    ex.print();
    cout<<"\nВведите название города, который следует удалить: ";
    string in;
    getline(cin,in);
    getline(cin,in);
    ex._delete(in,data.size());
    cout<<"\nОбновленный связный список: \n";
    ex.print();
    cout<<"\nВведите индекс, по месту которого вставится город \"Конец\": ";
    int k;
    cin>>k;
    ex.insert(k-2,"Конец");
    cout<<"\nОбновленный связный список: \n";
    ex.print();
}
int main(){
    question_1();
    question_2();
    question_3();
    question_4();
    question_5();
    question_6();
    question_7();
    question_8();
    question_9();
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