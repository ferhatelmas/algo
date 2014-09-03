package page54.q5318;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    System.out.println(in.nextInt() & ((1 << in.nextInt()) - 1));
  }
}
