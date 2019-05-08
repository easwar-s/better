#include<stdio.h>
int main()
{
 int c,n,fact = 1;
 printf("Enter the number for factorial:");
 scanf("%d",&n);
 for(c = 1;c<=n;c++)
 {
  fact = fact *c;
 }
 printf("factorial of %d is %d",n,fact);
 return 0;
} 
