#include<iostream>

using namespace std;

#define MAXSIZE 100
#define SElemType int

enum Status
{
	ERROR,
	OK

};

typedef struct
{
	SElemType* base;
	SElemType* top;
	int stacksize;
}SqStack;


Status InitStack(SqStack& S) {
	S.base = new SElemType[MAXSIZE];
	if (!S.base) exit(OVERFLOW);
	S.top = S.base;
	S.stacksize = MAXSIZE;
	return OK;
}

Status Push(SqStack& S, SElemType e) {
	if (S.top - S.base == S.stacksize) return ERROR;
	*S.top++ = e;
	return OK;
}

Status Pop(SqStack& S, SElemType& e) {
	if (S.top == S.base) return ERROR;
	e = *--top;

	return OK;
}

SElemType GetTop(SqStack S) {
	if (S.top != S.base)
		return *(S.top - 1);
}

int StackLength(SqStack S)
{
	return S.top - S.base;
}

Status ClearStack(SqStack S) {
	if (S.base)S.top = S.base;
	return OK;
}

Status StackEmpty(SqStack S) {
	if (S.top == S.base)return OK;
	else
		return ERROR;
}
