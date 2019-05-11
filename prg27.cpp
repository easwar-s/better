#include<iostream>
using namespace std;
bool isnumber(string s)
{
 for(int i=0;i<s.length();i++)
 {
  if(isdigit(s[i]) == false)
  {
   return false;
  }
 }
 return true;
}
int main()
{
 string str;
 cout<<"Enter the input:";
 cin>>str;
 if(isnumber(str))
  cout<<"yes it is integer";
 else
  cout<<"no it is string";
 return 0;
}
