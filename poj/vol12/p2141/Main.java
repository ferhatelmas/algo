package vol12.p2141;

import java.util.Scanner;

public class Main {

  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    char[] mapping = in.nextLine().trim().toCharArray();
    StringBuilder sb = new StringBuilder();

    String txt = in.nextLine().trim();
    for(char c : txt.toCharArray()) {
      if(c != ' ') sb.append(decode(mapping, c));
      else sb.append(c);
    }

    System.out.println(sb.toString());
  }

  private static char decode(char[] m, char c) {
    if(c >= 'A' && c <= 'Z')
      return (char)('A' - 'a' + m[c - 'A']);
    return m[c-'a'];
  }

}
