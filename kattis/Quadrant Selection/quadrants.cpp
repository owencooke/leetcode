/*/////////////////////////////////////
	Name: Owen Cooke
	Date: January 13, 2022
	Problem: Quadrant Selection
	Credit: Kattis
/////////////////////////////////////*/

#include <iostream>
using namespace std;

int main() {
	// Get input from stdin
	int x, y, quad;
	cin >> x >> y;

	// Use conditional statement blocks to determine quadrant #
	if (x > 0) {
		if (y > 0) {
			quad = 1;
		}
		else {
			quad = 4;
		}
	}
	else {
		if (y > 0) {
			quad = 2;
		}
		else {
			quad = 3;
		}
	}

	// Ouput resulting quadrant
	cout << quad << endl;
	return 0;
}
