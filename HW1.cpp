#include <stdio.h>
#include <string.h>
void Affine(int,char*,int,int,int);
int main(){
	int i=0,k1=0,k2=0,str_size=0,select =1;
	char str[50]={0,};
	
	printf("��ȣ�� �Ǵ� ���� �Է�: ");
	gets(str); //enter plaintext or ciphertext
	
	printf("��ȣ�� 1��, ��ȣ�� 2���� ���� : ");
	scanf("%d",&select); //choose encryption or decryption selection
	fflush(stdin);
	
    printf("Please enter to cipher key(k1, k2 format) : "); 
    scanf("%d, %d", &k1, &k2); //k1*p + k2
    k1 %= 26; k2 %= 26; // �׻� 0 ~ 25 ������ ���� 
		
	str_size=strlen(str); // calculate plaintext or ciphertext length
	
	Affine(select,str,str_size,k1,k2);//affin cipher function
	
	printf("\n��ȣȭ �Ǵ� ��ȣȭ�� ��� ���:");
	puts(str); //encryption or decryption output
	
	return 0; 	 	
}

void Affine(int select, char*str, int str_size, int k1, int k2)
{
	int i;
	for(i=0;i<str_size;i++){
		if(select ==1){
			if((str[i]>='A')&&(str[i]<='Z'))
			{
				str[i]-='A'; // ���ڷ� ��ȯ
				if((k1 * str[i] + k2)<0)
				{
					str[i]+=26;
				} 
				str[i]=(k1 * str[i] + k2 )%26;
				str[i]+='A'; // ���ڷ� ��ȯ
				 
			}
			else if((str[i]>='a')&&(str[i]<='z'))
			{
				str[i]-='a'; // ���ڷ� ��ȯ
				if((k1 * str[i] + k2)<0)
				{
					str[i]+=26;
				} 
				str[i]=(k1 * str[i] + k2) %26;
				str[i]+='a'; // ���ڷ� ��ȯ			
			}
			else ;			
		}
		if(select ==2){
			if((str[i]>='A')&&(str[i]<='Z'))
			{
				str[i]-='A'; // ���ڷ� ��ȯ
				if((str[i]-k2)/k1<0)
				{
					str[i]+=26;
				} 
				str[i]=((str[i]-k2)/k1) %26;
				str[i]+='A'; // ���ڷ� ��ȯ
				 
			}
			else if((str[i]>='a')&&(str[i]<='z'))
			{
				str[i]-='a'; // ���ڷ� ��ȯ
				if((str[i]-k2)/k1<0)
				{
					str[i]+=26;
				} 
				str[i]=((str[i]-k2)/k1)%26;
				str[i]+='a'; // ���ڷ� ��ȯ			
			}
			else ;			
		}
	}	
}
