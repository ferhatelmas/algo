package page22.q2164;

import java.util.Scanner;

public class Main {

  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    String s = in.nextLine();
    int n = in.nextInt();

    char[] c = new char[s.length()];
    for(int i=0; i<c.length; i++) {
      int ord = s.charAt(i) - n;
      if(ord < 'A') ord += 26;
      c[i] = (char)ord;
    }
    System.out.println(c);
  }
}
