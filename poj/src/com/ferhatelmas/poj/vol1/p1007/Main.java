package com.ferhatelmas.poj.vol1.p1007;

import java.util.PriorityQueue;
import java.util.Scanner;

public class Main {

  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int n = in.nextInt(), m = in.nextInt();

    PriorityQueue<DNA> pq = new PriorityQueue<DNA>();
    while(m-- > 0) {
      String line = in.next();
      pq.add(new DNA(line));
    }

    while(!pq.isEmpty()) {
      System.out.println(pq.remove().dna);
    }
  }

  static class DNA implements Comparable<DNA> {

    String dna;
    int s;

    public DNA(String dna) {
      this.dna = dna;
      this.s = getSortedCount();
    }

    private int getSortedCount() {
      char[] chars = dna.toCharArray();
      int n = chars.length;

      int cnt = 0;
      for(int i=0; i<n; i++)
        for(int j=i+1; j<n; j++)
          if(chars[i] > chars[j]) cnt++;

      return cnt;
    }

    public int compareTo(DNA o) {
      return s-o.s;
    }

  }

}
