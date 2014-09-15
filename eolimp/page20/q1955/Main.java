package page20.q1955;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int d1 = in.nextInt(), m1 = in.nextInt(), y1 = in.nextInt(),
        d2 = in.nextInt(), m2 = in.nextInt(), y2 = in.nextInt(),
        c = y2 - y1;

    if(m2 < m1 || (m1 == m2 && d2 < d1)) c--;
    System.out.println(c);
  }
}
