package page27.q2662;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int[] ns = new int[in.nextInt()];
    for(int i=0; i<ns.length; i++) ns[i] = in.nextInt();

    int min, k = ns[0], cnt = 0;
    for(int i=0; i<ns.length; i++) {
      min = i;
      for(int j=i+1; j<ns.length; j++) {
        if(ns[j] < ns[min]) min = j;
      }
      if(min != i) {
        if(ns[i] == k || ns[min] == k) cnt++;
        int t = ns[i];
        ns[i] = ns[min];
        ns[min] = t;
      }
    }

    System.out.println(cnt);
  }
}
