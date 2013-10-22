package page20.q1951;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    String[] s = new Scanner(System.in).nextLine().split("\\.");
    for(String ss : s) {
      try {
        int i = Integer.parseInt(ss);
        if(i < 0 || i > 255) {
          System.out.println(0);
          return;
        }
      } catch (Exception e) {
        System.out.println(0);
        return;
      }
    }
    System.out.println(1);
  }
}
