package page54.q5319;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    System.out.println(in.nextInt() & (Integer.MAX_VALUE - (1 << in.nextInt())));
  }
}
