package page72.q7111;

import java.util.Scanner;

public class Main {
  private static int n;

  public static void main(String[] args) {
    n = new Scanner(System.in).nextInt();
    permutation("AEIJOUY");
  }

  public static void permutation(String str) {
    permutation("", str);
  }

  private static void permutation(String prefix, String str) {
    int l = str.length();
    if(l == 0) {
      if(--n == 0) {
        System.out.println(prefix);
        System.exit(0);
      }
    } else {
      for (int i=0; i<l; i++)
        permutation(prefix + str.charAt(i), str.substring(0, i) + str.substring(i+1));
    }
  }
}
