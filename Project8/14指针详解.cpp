#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include<string.h>//ʹstrlen��������
#include<Windows.h>
#include<stdlib.h>


//void test(int arr[])
//{
//	printf("%p\n", arr);
//	int sz = sizeof(arr) / sizeof(arr[0]);//��64λƽ̨�н��Ϊ2
//	printf("%d\n", sz);
//}
//
//int main()
//{
//	int arr[] = { 1,2,3,4 };
//	test(arr);
//	return 0;
//}



//int main()
//{//�������ִ�ӡ֮��Ĳ�ͬ
//	int arr1[] = { 1,2,3 };
//	printf("%p\n", arr1);//���������޷�ֱ��������ӡ ����������ֵ
//	printf("%d\n", arr1[0]);
//
//	char arr[] = "abcdef";
//	char* pc = arr;
//	printf("%p\n", arr);
//	printf("%p\n", pc);
//
//	printf("%s\n", arr);
//	printf("%s\n", pc);//ע������Ҳ���Դ�ӡ���������ַ�����
//	return 0;
//}



int main()
{
	char a[] = "abc";//�����ͣ����"abc"�� ������Ϊconst ���г����� 
	a[0] = 'b';
	printf("%s\n", a);//���Կ������������������޸Ĳ�û�б�������������ӡ


	//char* p = "abcdef";//����ʦ����ʾ�� "abcdef"��Ϊһ�������ַ���  ����Ὣa�ĵ�ַ����p   ������������д�ᱨ�� 
	const char* p = "abcdef";//����Ҫ����const���ܸ�ֵ  �������߶����г����� �Ͳ��ᱨ�� 
	printf("%p\n", *p);

	//*p=   �������޷�ͨ��pȥ�޸�
 	//printf("%p\n", *p);
	return 0;
}




//int main()
//{
//
//	return 0;
//}