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


typedef struct
{
	ElemType* elem;
	int length;
}SqList;


Status InitList(SqList& L);
Status GetElem(SqList& L, int i, ElemType& e);

int LocateElem(SqList& L, ElemType e);

Status ListInsert(SqList& L, int i, ElemType e);
Status ListDelete(SqList& L, int i);
Status isListEmpty(SqList& L);