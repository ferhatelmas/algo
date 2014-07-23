package page8.q774;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int r = in.nextInt(), w = in.nextInt(), l = in.nextInt();
    System.out.println(2*r >= Math.sqrt(w*w + l*l) ? "YES" : "NO");
  }
}
