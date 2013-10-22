package page6.q575;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    int k = new Scanner(System.in).nextInt();
    System.out.println(k < 3 ? k : (k-2)*3);
  }
}
