package page12.q1179;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int t = in.nextInt(), q;

    while(t-- > 0) {
      char c[] = in.next().toCharArray();
      q = in.nextInt();
      StringBuilder sb = new StringBuilder();

      while(q-- > 0) {
        if(isSame(c, in.nextInt(), in.nextInt(), in.nextInt(), in.nextInt()))
          sb.append('1');
        else
          sb.append('0');
      }
      System.out.println(sb.toString());
    }
  }

  private static boolean isSame(char ch[], int a, int b, int c, int d) {
    int k = b-a;
    if(k != d-c) return false;
    for(int i=0; i<=k; i++)
      if(ch[a+i] != ch[c+i])
        return false;
    return true;
  }
}
