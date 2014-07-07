package page23.q2206;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int ns[] = new int[3], s = 0;
    for(int i=0; i<ns.length; i++) {
      ns[i] = in.nextInt();
      s += ns[i];
    }
    if(s%3 == 0) {
      int c = 0;
      s /= 3;
      for(int i : ns) c += Math.abs(i - s);
      System.out.println(c/2);
    } else {
      System.out.println("IMPOSSIBLE");
    }
  }
}
