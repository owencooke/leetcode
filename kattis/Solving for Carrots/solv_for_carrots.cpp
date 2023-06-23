/*/////////////////////////////////////
	Name: Owen Cooke
	Date: January 13, 2022
	Problem: Solving for Carrots
	Credit: Kattis
/////////////////////////////////////*/

#include <iostream>
#include <string>
using namespace std;

int main() {
	/* Trick problem!! "In this contest, you earn a carrot for each problem solved".
	The number of problems solved is the second integer given on the first line of
	input, so desired output is simply echoing the second integer given. */
	int contestants, carrots;

	// Get input for # of contestants and # of problems solved == # of carrots
	cin >> contestants >> carrots;

	// Iterate through descriptions to allow for input formatted as specified
	string desc;
	for (int i = 1; i <= contestants; i++) {
		getline(cin, desc);
	}
	// Output second integer from input stream
	cout << carrots << endl;
	return 0;
}
