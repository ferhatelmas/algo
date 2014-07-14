package page7.q653;

import java.util.Arrays;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int ns[] = new int[3];
    for(int i=0; i<ns.length; i++) ns[i] = in.nextInt();
    Arrays.sort(ns);
    if(ns[2] >= ns[1] + ns[0])
      System.out.println("IMPOSSIBLE");
    else {
      int c = ns[2]*ns[2] - ns[1]*ns[1] - ns[0]*ns[0];
      if(c == 0)
        System.out.println("RIGHT");
      else if(c > 0)
        System.out.println("OBTUSE");
      else
        System.out.println("ACUTE");
    }
  }
}
