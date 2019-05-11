#include<stdio.h>
int main()
{
int i,j,a,n,number[n];
printf("Enter the value for N:");
scanf("%d",&n);
printf("Enter the numbers to sort:");
for(i=0;i<n;++i)
{
 scanf("%d",&number[i]);
}
for(i=0;i<n;++i)
{
 for(j=i+1;j<n;++j)
 {
  if(number[i]>number[j])
  {
   a = number[i];
   number[i] = number[j];
   number[j] = a;
  }
 }
}
printf("Sorted array:");
for(i=0;i<n;++i)
{
 printf("%d\n",number[i]);
}
}
