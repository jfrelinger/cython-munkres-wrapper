/*
 * Munkres.h
 *
 *  Created on: Sep 29, 2010
 *      Author: jolly
 */

#ifndef MUNKRES_H_
#define MUNKRES_H_
//using namespace std;
//using std::vector;
#include <vector>
#include <algorithm> 

enum path_type { STARRED, PRIMED };
class path_item {
public:
	path_item(int, int, path_type);
	virtual ~path_item();
	int row;
	int col;
	path_type type;
};

class Munkres {
public:
	Munkres();
	virtual ~Munkres();
	void solve(double* icost, double* answer, int m, int n);
private:
	double *cost;
	bool *starred;
	bool *covered_rows;
	bool *covered_cols;
	bool * primed;
	double k;
	int rows;
	int cols;
	int smallest;
	int largest;


	void step0();
	void step1();
	void step2();
	void step3();
	void step4();
	void step5(int, int);
	void step6(double);

	bool is_starred_in_row_col(int, int);
	int starred_in_row(int);
	void cover_col(int);
	void uncover_col(int);
	void cover_row(int);
	void uncover_row(int);
	bool is_covered(int, int);
	bool is_covered_col(int);
	bool is_covered_row(int);
	void prime(int, int);
	bool find_zero(std::vector<std::vector<double> >, int*, int*);
	float min_uncovered();
	int find_starred_zero_in_col(int);
	int find_primed_zero_in_row(int);

};

#endif /* MUNKRES_H_ */

int main();
