#include<iostream>

using namespace std;

#define MAXSIZE 100
#define ElemType int

enum Status
{
	ERROR,
	OK

};

typedef struct StackNode
{
	ElemType data;
	struct  StackNode* next;
	
}StackNode,*LinkStack;


Status InitStack(LinkStack& S) {
	S = NULL;
	return OK;
}

Status Push(LinkStack& S, ElemType e)
{
	p = new StackNode;
	p->data = e;
	p->next = S;
	S = p;
	return OK;
}

Status Pop(LinkStack& S, ElemType& e)
{
	if (S == NULL) return ERROR;
	e = S->data;
	p = S;
	S = S->next;
	delete p;

	return OK;
}

ElemType GetTop(LinkStack S)
{
	if (S != NULL)
		return S->data;
}

Status StackEmpty(LinkStack S) {
	if (S == Null)return OK;
	else return ERROR;
}
