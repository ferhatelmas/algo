package page52.q5199;

import java.util.Arrays;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int n = in.nextInt(), t = in.nextInt(),
        ns[] = new int[n];

    for(int i=0; i<n; i++)
      ns[i] = in.nextInt();

    for(int i=0; i<t; i++) {
      int k = in.nextInt();
      int j = Arrays.binarySearch(ns, k);
      if(j < 0) {
        System.out.println(0);
      } else {
        while(j < ns.length && ns[j] == k)
          j++;
        System.out.println(j);
      }
    }

  }
}
