package com.ferhatelmas.eolimp.page70.q2169;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;
import java.util.TreeSet;

public class Main {

  private static TreeSet<String> results = new TreeSet<String>();

  public static void main(String[] args) {
    int n = new Scanner(System.in).nextInt();

    ArrayList<Integer> l = new ArrayList<Integer>();
    for(int i=0; i<n; i++) l.add(i+1);
    permute(l, 0);
    for(String s : results) System.out.println(s);
  }

  private static void permute(ArrayList<Integer> l, int offset) {
    for(int i=offset; i<l.size(); i++) {
      Collections.swap(l, i, offset);
      permute(l, offset+1);
      Collections.swap(l, offset, i);
    }
    if(offset == l.size()-1) results.add(getString(l));
  }

  private static String getString(ArrayList<Integer> l) {
    StringBuilder sb = new StringBuilder();
    for(int i : l) sb.append(i).append(" ");
    return sb.toString().trim();
  }
}
