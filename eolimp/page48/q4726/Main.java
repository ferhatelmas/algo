package page48.q4726;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    String s = new Scanner(System.in).next();
    int i = s.indexOf('f');
    if(i >= 0) {
      int j = s.lastIndexOf('f');
      System.out.println(i == j ? i : (i + " " + j));
    }
  }
}
