package page17.q1647;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    System.out.println(in.nextInt() & (Integer.MAX_VALUE << in.nextInt()));
  }
}
