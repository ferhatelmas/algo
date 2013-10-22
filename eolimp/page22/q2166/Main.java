package page22.q2166;

import java.util.Arrays;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    char[] a = in.nextLine().toCharArray(), b = in.nextLine().toCharArray();
    Arrays.sort(a);
    Arrays.sort(b);
    System.out.println(Arrays.equals(a, b) ? "YES" : "NO");
  }
}
