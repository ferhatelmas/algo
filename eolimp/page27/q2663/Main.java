package page27.q2663;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int n = in.nextInt(), ns[] = new int[n];

    for(int i=0; i<n; i++) ns[i] = in.nextInt();

    int c = 0;
    boolean swapped = true;
    while(swapped) {
      swapped = false;
      for(int i=1; i<n; i++)
        if(ns[i-1] > ns[i]) {
          ns[i-1] ^= ns[i];
          ns[i] ^= ns[i-1];
          ns[i-1] ^= ns[i];
          swapped = true;
          c++;
        }
    }

    System.out.println(c);
  }
}
