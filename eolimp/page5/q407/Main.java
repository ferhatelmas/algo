package page5.q407;

import java.util.Scanner;

public class Main {

  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int n = in.nextInt();
    String s[] = new String[n];
    int i,j,k;
    char[] c = new char[3];
    for(i=0; i<n; i++) {
      k = in.nextInt();
      c[0] = 'G';
      c[1] = 'C';
      c[2] = 'V';
      for(j=0; j<k; j++)
        swap(c);

      s[i] = new String(c);
    }
    for(String ss : s) System.out.println(ss);
  }

  static void swap(char[] s) {
    char c = s[2];
    s[2] = s[1];
    s[1] = s[0];
    s[0] = c;
  }

}
