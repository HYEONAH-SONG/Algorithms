#include <stdio.h> 
#include <string.h> 
#include <stdlib.h>

int main(){
	int row_num =0, col_num=0, size=0,select=0,cnt=0, rail_num =0, m=0, k=-1;
	char text[64],tmp_text[2][32],c_text[64],d_text[64];
	
	printf("��ȣ�� 1��, ��ȣ�� 2���� ���� : ");
	scanf("%d",&select);
	
	printf("Rail's number  : ");
	scanf("%d",&rail_num);
		
	if(select ==1){
		printf("���Է�: ");
		scanf("%s",text);
		size=strlen(text); 
	}
	else if (select==2){
		printf("��ȣ�� �Է�: ");
		scanf("%s",text);
		size=strlen(text); 	
	}
	else; 
	
	if(select ==1){ //Encryption function
		char rail_matrix[rail_num][size];//rail matrix ���� (���� ����: rail�� ����, ���� ����: �Է��� ���ڿ� ����)	 	
        int k=-1;
		// matrix initiallized    
		for(int i=0;i<rail_num;++i)
			for(int j=0;j<size;++j)
				rail_matrix[i][j]= '\n'; 

		for(int i=0;i<size;++i){
			rail_matrix[row_num][col_num++]=text[i];
			
			if(row_num ==0||row_num==rail_num-1)
				k=k*(-1);
				
			row_num =row_num +k;	
		}
		printf("\n ��ȣȭ�� �޽���:");
		for(int i=0;i<rail_num;i++)
			for(int j=0;j<size;++j)
				if(rail_matrix[i][j]!='\n')
					printf("%c",rail_matrix[i][j]);		
			
	}	
	else if(select==2){ //Decryption Function
		char rail_matrix[rail_num][size];//rail matrix ���� (���� ����: rail�� ����, ���� ����: �Է��� ���ڿ� ����)	 		
		// matrix initiallized		
		for(int i=0;i<rail_num;++i)
			for(int j=0;j<size;++j)
				rail_matrix[i][j]= '\n'; 

		for(int i=0;i<size;++i){
			rail_matrix[row_num][col_num++]='*';
			
			if(row_num ==0||row_num==rail_num-1)
				k=k*(-1);
			
			row_num =row_num +k;
		}
		
		for(int i=0;i<rail_num;++i)
			for(int j=0;j<size;++j)
				if(rail_matrix[i][j]=='*')
					rail_matrix[i][j]=text[m++];
					
		row_num=col_num=0;
		k=-1;
		
		printf("\n ��ȣȭ�� �޽���: ");
		for(int i=0;i<size;++i){
			printf("%c",rail_matrix[row_num][col_num++]);
			
			if(row_num ==0||row_num==rail_num-1)
				k=k*(-1);
				
			row_num =row_num +k;			
		}				
	}
	return 0;
} 
