#include "SequentialList.h"


Status InitList(SqList& L) {
	// 构造一个空的顺序表
	L.elem = new ElemType[MAXSIZE];

	if (!L.elem) exit(OVERFLOW);

	L.length = 0;

	return OK;


}

Status GetElem(SqList& L, int i, ElemType& e) {
	if (i < 1 || i >= L.length) return ERROR;

	e = L[i - 1];
	return OK;
}


int LocateElem(SqList& L, ElemType e) {

	int i = 0;
	for (; i < L.length; ++i)
	{
		if (L[i] == e)
		{
			return i + 1;
		}
	}
	if (i == L.length)
		return 0; // 查找失败

}


Status ListInsert(SqList& L, int i, ElemType e) {
	if ((i < 1) || (i > L.length + 1)) return ERROR;

	if (L.length == MAXSIZE) return ERROR;

	// 全体后移
	for (j = L.length - 1; j >= i - 1; j--)
		L.elem[j + 1] = L.elem[j];

	// 把新元素放到第i个的位置
	L.elem[i - 1] = e;
	++L.length;

	return OK;

}

Status ListDelete(SqList& L, int i) {
	if ((i < 1) || (i > L.length)) return ERROR;
	for (j = i; j <= L.length - 1; ++j)
		L.elem[j - 1] = L.elem[j];
	--L.length;
	return OK;
}

Status isListEmpty(SqList& L) {
	if (L.length == 0) return OK;

	return ERROR;
}
