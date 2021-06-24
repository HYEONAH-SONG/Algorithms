#include <stdio.h>
#include <string.h>
void Affine(int,char*,int,int,int);
int main(){
	int i=0,k1=0,k2=0,str_size=0,select =1;
	char str[50]={0,};
	
	printf("암호문 또는 평문을 입력: ");
	gets(str); //enter plaintext or ciphertext
	
	printf("암호는 1번, 복호는 2번을 선택 : ");
	scanf("%d",&select); //choose encryption or decryption selection
	fflush(stdin);
	
    printf("Please enter to cipher key(k1, k2 format) : "); 
    scanf("%d, %d", &k1, &k2); //k1*p + k2
    k1 %= 26; k2 %= 26; // 항상 0 ~ 25 사이의 범위 
		
	str_size=strlen(str); // calculate plaintext or ciphertext length
	
	Affine(select,str,str_size,k1,k2);//affin cipher function
	
	printf("\n암호화 또는 복호화된 결과 출력:");
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
				str[i]-='A'; // 숫자로 변환
				if((k1 * str[i] + k2)<0)
				{
					str[i]+=26;
				} 
				str[i]=(k1 * str[i] + k2 )%26;
				str[i]+='A'; // 문자로 변환
				 
			}
			else if((str[i]>='a')&&(str[i]<='z'))
			{
				str[i]-='a'; // 숫자로 변환
				if((k1 * str[i] + k2)<0)
				{
					str[i]+=26;
				} 
				str[i]=(k1 * str[i] + k2) %26;
				str[i]+='a'; // 문자로 변환			
			}
			else ;			
		}
		if(select ==2){
			if((str[i]>='A')&&(str[i]<='Z'))
			{
				str[i]-='A'; // 숫자로 변환
				if((str[i]-k2)/k1<0)
				{
					str[i]+=26;
				} 
				str[i]=((str[i]-k2)/k1) %26;
				str[i]+='A'; // 문자로 변환
				 
			}
			else if((str[i]>='a')&&(str[i]<='z'))
			{
				str[i]-='a'; // 숫자로 변환
				if((str[i]-k2)/k1<0)
				{
					str[i]+=26;
				} 
				str[i]=((str[i]-k2)/k1)%26;
				str[i]+='a'; // 문자로 변환			
			}
			else ;			
		}
	}	
}
