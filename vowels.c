#include<stdio.h>
int main()
{
    char v;
    printf("Enter the character\n");
    scanf("%c",&v);
    if(v=='a'||v=='A'||v=='e'||v=='E'||v=='i'||v=='I'||v=='o'||v=='O'||v=='u'||v=='U')
        printf("%c is vowel.\n",v);
    else
       printf("%c is a consonant.",v);
    return 0;
}
