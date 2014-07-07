package page22.q2196;

import java.util.Arrays;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    char c[] = in.nextLine().toCharArray();

    int t = in.nextInt();
    in.nextLine();
    while(t-- > 0) {
      String s[] = in.nextLine().split("\\s");
      int i = Integer.parseInt(s[1])-1, j = Integer.parseInt(s[2])-1;
      if("S".equals(s[0])) {
        Arrays.sort(c, i, j+1);
      } else {
        for(; i<j; i++, j--) {
          char ch = c[i];
          c[i] = c[j];
          c[j] = ch;
        }
      }
    }
    System.out.println(c);
  }
}
