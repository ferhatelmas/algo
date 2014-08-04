package page54.q5315;

import java.util.Arrays;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    char c[] = new char[32], r[] = Integer.toBinaryString(in.nextInt()).toCharArray();
    Arrays.fill(c, '0');
    System.arraycopy(r, 0, c, 32-r.length, r.length);
    c[31-in.nextInt()] = '1';
    System.out.println(Integer.parseInt(new String(c), 2));
  }
}
