package page58.q5718;

import java.util.Arrays;
import java.util.Collections;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Character c[] = toCharArray(Integer.toBinaryString(new Scanner(System.in).nextInt()));
    Arrays.sort(c);
    int a = Integer.parseInt(toString(c), 2);
    Arrays.sort(c, Collections.reverseOrder());
    System.out.println(Integer.parseInt(toString(c), 2) - a);
  }

  private static String toString(Character c[]) {
    StringBuilder sb = new StringBuilder();
    for(char ch : c) sb.append(ch);
    return sb.toString();
  }

  private static Character[] toCharArray(String s) {
    Character c[] = new Character[s.length()];
    for(int i=0; i<c.length; i++)
      c[i] = s.charAt(i);
    return c;
  }
}
