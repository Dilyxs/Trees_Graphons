#include <iostream>
#include <vector>
#include <cmath>
#include <ctime>

/*
int main(){
    std :: cout <<"I like rasberries" <<std::endl;
    std:: cout <<"I like blueberries" <<std::endl;

    return 0;
}


int main(){
    int x;
    x=23;
    int y = 12;
   int z = x * y;
    double price = 21.12;
    char grade = 'q';
    bool student = true;
    std::string name ="adsayan";
     



    std::cout <<x <<"\n";
    std::cout << y<<"\n";
    std::cout << z<<"\n";
     std::cout << name<<"\n";
    std::cout << "Hello " << name;
    std::cout<< "You are "<<x<< "years old";
    
    return 0;

}

int main(){
     const double PI = 3.14159;
    double radius = 20;
    double circumference = 2* pi*radius;
    const double LIGHT_SPEED = 299943223;
    std::cout << "the answer is "<< circumference;
    return 0;


}


namespace first{
   int x=1;
}
int main(){
   int x=0;
    std::cout<<first::x;
}


typedef std::vector<std::pair<std::string, int>> pairlist_t;
//typedef std::string str_t;
using str_t = std::string;
int main(){
   int student = 22;
   student++;
   std::cout<<student;
    str_t name = "adsayan";
    std::cout<<name;
    int remainder = student %3;
    std::cout<<remainder;
    char x  = (char)100;
    std::cout<<X;

    return 0;
}

int main(){
    std::string name ;
    std::cout<<"what's your name";
    std::getline(std::cin, name);
    std::cout<<"Hello "<<name;

}

int main(){
    double x = 3;
    double y = 4;
    double z = pow(2,4);
    z= abs(-12321);
    std::cout<< z;
    return 0;

}

int main(){
    int a;
    int b;
    std::cout<<"Enter A value:";
    std::cin>> a;
    std::cout<<"Enter B value:";
    std::cin>> b;
    double A = pow(a,2);
    double B = pow(b,2);
    double AB = A + B;
    double c = sqrt(AB);

    std::cout<<c;

}

int main(){
   // int age;
   // std::cout<<"What's your age?";
  //  std::cin>> age;
  //  if (age >= 18){
   //     std::cout<<"WElcome to website";}
  //  else{
  //      std::cout<<"You are not welcomed here";}
  //  int month;
  //  std::cout<<"Enter your month birthdate";
  //  std::cin>> month;
 //   switch (month)
 //   {
 //   case 1:
 //       std::cout<<"It is january";
  //      break;
    
    
  //  default:
  //      break;
   // }
    char op;
    double numb1;
    double numb2;
    double result;

    std::cout<<"***************Calculator******************* "<<std::endl12;
    std::cout<<"Enter your first number";
    std::cin>>numb1;
    std::cout<<"Enter your second number";
    std::cin>>numb2;
    std::cout<<"Enter your operator";
    std::cin>>op;
    switch (op){
    
    case '+':
        result = numb1 + numb2;
        std::cout<<"THis is the result:"<<result;
        break;
    case '-':
        result = numb1 - numb2;
        std::cout<<"THis is the result:"<<result;
        break;
    case '/':
        result = numb1 / numb2;
        std::cout<<"THis is the result:"<<result;
        break;
    case '*':
        result = numb1 * numb2;
        std::cout<<"THis is the result:"<<result;
        break;
    
    default:
        std::cout<<"Make sure to put either +,-,*,/ as your operator";
        break;
    }
    


}


int main(){
 //   int grade = 75;
   // grade >= 60 ? std::cout<<"You passed":std::cout<<"YOU've failed";                         //&&== and. ||== or. !==changes bool to opposite(NOT)
    int temperature;
    std::cout<<"Enter the temperature:";
    std::cin>>temperature;
    if(temperature >0 && temperature<30){
        std::cout<<"The temperature is good";
    }
    else{
        std::cout<<"The temperature isn't good at the moment";
    }

}

int main(){

    double temp;
    char unit;
    double answer;
    std::cout<<"What temperature is it?";
    std::cin>>temp;
    std::cout<<"Which unit  C or F";
    std::cin>>unit;
    if (unit == "C"){
        (temp *1.8)+32 = answer;
        std::cout<<answer;}
    else{
        (temp-32)*1.8 = answer;
        std::cout<<answer;
    }
    

}


int main(){
  //  std::string name;
  //  std::cout<<"What is your name?";
  //  std::getline(std::cin,name);

  //  while (name.empty() == true){                                               note that while loops only excecute if the inside is TRUE, it checks if it s true
    //    std::cout<<"Put your name";
    
  //   }
  //   std::cout<<"Hello "<<  name;
  int number;
    do
    {
        std::cout<<"enter a negative number?";
    std::cin>>number;
    } while (number>0 ||     isdigit(number)==false);
    std::cout<<"Ty";

    




    }



int main(){
    for(int i =1; i<=20 ;i++){
        if (i=13){
            break;
        }
    std::cout<<i<<std::endl;

    }
std::cout<<"Happy new Year"<<std::endl;
}

int main(){
    for (int i = 1; i<=3; i++){
        


        for(int j=1; j <=10; j++){
            std::cout<<j<<std::endl;

        }
        std::cout<<std::endl;

    }}


int main(){
 //   srand(time(NULL));
  //  int num = (rand() % 20) +1;
 //   std::cout<<num;
    srand(time(NULL));
    int randaom = (rand() %5) +1;
    std::cout<<randaom;
    switch (randaom)
    {
    case 1:
        std::cout<<'YOu get a car'<<std::endl;
        break;
    case 2:
        std::cout<<'YOu get a pen'<<std::endl;
        break;
    case 3:
        std::cout<<'YOu lost your job'<<std::endl;
        break;
    case 4:
        std::cout<<'YOu get a schorlaship'<<std::endl;
        break;
    case 5:
        std::cout<<'YOu died'<<std::endl;
        break;
    
    default:
        break;
    }
    
*/

void happyBirthday(){
    std::cout<<"HAppy birthday to you!!"<<std::endl;
    std::cout<<"HAppy birthday to you!!"<<std::endl;
    std::cout<<"HAppy birthday to you!!"<<std::endl;
    std::cout<<"HAppy birthday to you!!"<<std::endl;
    std::cout<<"HAppy birthday to you!!"<<std::endl;


}





std::string concatStrings(std::string string1, std::string string2);
/*
int main(){
  //  int num;
  //  int guess;
  //  int tries;

  //  srand(time(NULL));
  //  num = (rand() % 100)+1;
 // happyBirthday();
 // happyBirthday();
 // happyBirthday();
std::string first_name = "Adsayan";
std::string last_name = "Selvan";
std::string full_name = concatStrings(first_name,last_name);
std::cout<<"Hello"<<full_name;
std::string concatStrings(std::string string1, std::string string2){
    return string1 + " " + string2

}

void bake_pizza(){
    std::cout<<"Here is your pizza!"<<std::endl;

}
void bake_pizza(std::string top1){
    std::cout<<"Here is your pizza with "<<top1;

}

void show_balance(double balance){
    std::cout<<"Your balance is "<<balance<<std::endl;  
}
double deposit(){
     double amount = 0;
    std::cout<<"How much would you like to deposit";
    std::cin>>amount;

}

double withdraw(double balance){
return 0;
}

 int main(){
  //  bake_pizza();
  double balance = 0;
  int choice = 0;

  do
  {std::cout<<"Pick a choice between 1. SB, 2. D or 3. W, 4.Exit"<<std::endl;
  std::cin>>choice;
  std::cin.clear();
  fflush(stdin);

  switch (choice)
  {
  case 1:
    show_balance(balance);
    break;
    case 2:
        balance+=deposit();
        show_balance(balance);
        break;
    case 3:
        balance -= withdraw(balance);
        show_balance(balance);
        break;
    case 4:
        std::cout<<"THat's for visiting";
        break;
  
  default:
  std::cout<<"Invalid choice";
    break;
  }
    
  } while (choice!= 4);
*/




/*

int main(){
    char player;
    char computer;

   std::string car[] = {"Corvette", "Mustang", "lambo"};
   
  std::string name = "Bro";
  char grade = 'F';
  double gpa = 2.5;
  std::cout<<sizeof(car) / sizeof(std::string)<<" elements \n";
  for (int i = 0; i <sizeof(car)/ sizeof(std::string); i++){
    std::cout<<car[i]<<'\n';
  }
  for (std::string car : car){
    std::cout<<car<<'\n';
  }






}
*/
double getTotal(double prices[]){
    for(int i = 0; i<sizeof(prices)/sizeof(double); i++){
         double total = total + prices[1];
    }

}

int searchArray(int array[], int size, int element){
    for(int i = 0; i<size;i++){
        if (array[i] == element){
            return i;
        }
    }
    return -1;
}


int main(){
   // double prices[] = {49.32, 1.23, 12312.131, 154};
   // double total = getTotal(prices);
   // std::cout<<"total";
  // int numbers[]{1,2,3,4,5,6,7,8,9,10};
 //  int size = sizeof(numbers)/sizeof(numbers[1]);
  // int index;
//   int myNum;
  // std::cout<<"Enter element to search for"<<'\n';
 //  std::cin>>myNum;
  // index = searchArray(numbers,size, myNum);
 //  if (index != -1){
  //  std::cout<<"Element is at "<<index;
  // }
  //// else{
  //  std::cout<<"element is not there";
  // }
/*
    void sort(int array[], int size){
        int temp;
        for (int i = 0, i<size-1;i++){
            for (int j= 0, j<size-1;j++){
                if (array[j]< array[j+1]){
                    temp = array[j];
                    array [j] = array[j+1];
                    array [j+1] = temp;
                }

            }
        }

    }
    int array[]{1,2,3,4,5,6,7,8,9,10};
  int size = sizeof(array)/sizeof(array[1]);
  sort(array, size);
  for (int element : array ){
    std::cout<<element<<""<<'\n';
    */

    std::string foods[1000];
    fill(foods, foods+1000, "pizza");
    for ( int i = 0; i < sizeof(foods)/sizeof(foods[1]); i++){
        std::cout<<foods[i]<<'\n';
    }




}


  
  
  

    




    



















