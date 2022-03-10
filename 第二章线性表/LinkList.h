#pragma once
#include<iostream>

using namespace std;

#define MAXSIZE 100
#define ElemType int

enum Status
{
	ERROR,
	OK

};

//������Ĵ洢�ṹ
typedef struct LNode
{
	ElemType data;
	struct LNode* next;

}LNode,*LinkList;

Status InitList(LinkList& L) {
	L = new LNode;
	L->next = NULL;

	return OK;

}


Status GetElem(LinkList L, int i, ElemType& e) {
	auto p = L->next; j = 1;
	while (p && j < i) {
		p = p->next;
		++j;
	}
	if (!p || j > i)return ERROR;
	e = p->data;
	
	p = NULL;
	delete p;

	return OK

}

LNode* LocateElem(LinkList &L, ElemType e) {
	auto p = L->next;

	while (p && p->data != e)p = p->next;

	return p; // �������ʧ�ܵĻ������ص���NULL
}


Status ListInsert(LinkList& L, int i, ElemType e) {
	auto p = L; j = 0;
	while (p && (j < i - 1))
	{
		p = p->next; ++j;
	}

	if (!p || j > i - 1) return ERROR;
	s = new LNode;
	s->data = e;
	s->next = p->next;
	p->next = s;

	return OK;


}

Status ListDelete(LinkList& L, int i) {
	auto p = L; j = 0;
	while((p->next) && (j<i-1))
	{
		p = p->next; ++j;
	}
	if (!(p->next) || (j > i - 1)) return ERROR;
	q = p->next;
	p->next = q->next;
	delete q;
	return OK;
}


//�ж��Ƿ�Ϊ��
int ListEmpty(LinkList& L) {
	if (L->next)
		return ERROR;
	else
		return OK;
}

void CreateList_H(LinkList& L, int n) {

	L = new LNode;
	L->next = NULL;
	for (int i = 0; i < n; ++i) {
		p = new LNode;
		cin >> p->data;
		p->next = L->next;
		L->next = p;
	}
}

void CreateList_R(LinkList& L, int n) {

	L = new LNode;
	L->next = NULL;
	auto r = L;

	for (int i = 0; i < n; ++i) {
		p = new LNode;
		cin >> p->data;
		p->next = NULL;
		r->next = p;
		r = p;
	}
}

