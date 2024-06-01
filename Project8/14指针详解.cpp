#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include<string.h>//使strlen可以运行
#include<Windows.h>
#include<stdlib.h>


//void test(int arr[])
//{
//	printf("%p\n", arr);
//	int sz = sizeof(arr) / sizeof(arr[0]);//在64位平台中结果为2
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
//{//这样各种打印之间的不同
//	int arr1[] = { 1,2,3 };
//	printf("%p\n", arr1);//整型数组无法直接这样打印 结果会是随机值
//	printf("%d\n", arr1[0]);
//
//	char arr[] = "abcdef";
//	char* pc = arr;
//	printf("%p\n", arr);
//	printf("%p\n", pc);
//
//	printf("%s\n", arr);
//	printf("%s\n", pc);//注意这样也可以打印出完整的字符数组
//	return 0;
//}



int main()
{
	char a[] = "abc";//将鼠标停留在"abc"上 发现其为const 具有常属性 
	a[0] = 'b';
	printf("%s\n", a);//可以看到在这里这样进行修改并没有报错，且能正常打印


	//char* p = "abcdef";//在老师的演示中 "abcdef"作为一个常量字符串  这里会将a的地址赋给p   但是现在这样写会报错 
	const char* p = "abcdef";//必须要带上const才能赋值  这样两边都具有常属性 就不会报错 
	printf("%p\n", *p);

	//*p=   这样就无法通过p去修改
 	//printf("%p\n", *p);
	return 0;
}




//int main()
//{
//
//	return 0;
//}