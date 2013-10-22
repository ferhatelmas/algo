package page17.q1623;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    boolean o = false, e = false;
    for(int i=0; i<3; i++) {
      boolean j = in.nextInt()%2 == 0;
      o = o || !j;
      e = e || j;
    }
    System.out.println(e && o ? "YES" : "NO");
  }
}
