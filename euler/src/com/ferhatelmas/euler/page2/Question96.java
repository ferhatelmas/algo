package com.ferhatelmas.euler.page2;

import java.io.BufferedReader;
import java.io.FileReader;

public class Question96 {

  public static void main(String[] args) throws Exception {
    BufferedReader br = new BufferedReader(new FileReader("sudoku.txt"));

    int sum = 0;
    int[][] cells = new int[9][9];
    for(int i=0; i<50; i++) {
      br.readLine();
      for(int j=0; j<9; j++) {
        String line = br.readLine();
        for(int k=0; k<line.length(); k++)
          cells[j][k] = line.charAt(k) - '0';
      }
      solve(0, 0, cells);
      sum += (100*cells[0][0] + 10*cells[0][1] + cells[0][2]);
    }
    System.out.println(sum);
  }

  static boolean solve(int i, int j, int[][] cells) {
  	if (i == 9) {
  	    i = 0;
  	    if (++j == 9)
  		return true;
  	}
  	if (cells[i][j] != 0)  // skip filled cells
  	    return solve(i+1,j,cells);

  	for (int val = 1; val <= 9; ++val) {
  	    if (legal(i,j,val,cells)) {
  		cells[i][j] = val;
  		if (solve(i+1,j,cells))
  		    return true;
  	    }
  	}
  	cells[i][j] = 0; // reset on backtrack
  	return false;
  }

  static boolean legal(int i, int j, int val, int[][] cells) {
  	for (int k = 0; k < 9; ++k)  // row
  	    if (val == cells[k][j])
  		return false;

  	for (int k = 0; k < 9; ++k) // col
  	    if (val == cells[i][k])
  		return false;

  	int boxRowOffset = (i / 3)*3;
  	int boxColOffset = (j / 3)*3;
  	for (int k = 0; k < 3; ++k) // box
  	    for (int m = 0; m < 3; ++m)
  		if (val == cells[boxRowOffset+k][boxColOffset+m])
  		    return false;

  	return true; // no violations, so it's legal
  }

}
