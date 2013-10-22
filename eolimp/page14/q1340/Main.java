package page14.q1340;

import java.util.ArrayList;
import java.util.Scanner;

public class Main {

  public static void main(String[] args) {

    ArrayList<Integer> list = new ArrayList<Integer>();
    Scanner in = new Scanner(System.in);
    int n, i, j, k;

    while((n=in.nextInt()) != 0) list.add(n);

    for(k=0; k<list.size(); k++) {
      n = list.get(k);

      for(i=0; i<n; i++) {
        for(j=n-i-1; j>0; j--)
          System.out.print(" ");

        for(j=2*i+1; j>0; j--)
          System.out.print("*");

        System.out.println();
      }

      for(i=0; i<n-1; i++) {
        for(j=-1; j<i; j++)
          System.out.print(" ");

        for(j=2*(n-1-i)-1; j>0; j--)
          System.out.print("*");

        System.out.println();
      }

      if(k!=list.size()-1) System.out.println();
    }

  }

}