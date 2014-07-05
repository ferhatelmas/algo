package page67.q6628;

import java.util.Arrays;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);

    int i = 1;
    String a, b;
    while(!"END".equals(a = in.nextLine()) && !"END".equals(b = in.nextLine())) {
      System.out.printf("Case %d: %s\n", i++, is_same(a, b));
    }
  }

  private static String is_same(String a, String b) {
    return sorted(a).equals(sorted(b)) ? "same" : "different";
  }

  private static String sorted(String s) {
    char c[] = s.toCharArray();
    Arrays.sort(c);
    return new String(c);
  }
}
