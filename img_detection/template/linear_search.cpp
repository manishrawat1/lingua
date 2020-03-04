#include<iostream>
using namespace std;
int linear(int*a,int i,int n,int key){
	if(i==n){
		return -1;
	}
	for(i=0;i<n;i++){
	if(a[i]==key){
		return i;

		}
	}
	return linear(a,i+1,n,key);
}

int main() {
	int n;
	cin >> n;
	int a[10005];
	for(int i=0;i<n;i++){
		cin >> a[i];
	}
	int key;
	cin >> key;
	cout << linear(a,0,n,key)<< " ";
	return 0;
}