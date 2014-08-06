package page48.q4739;

import java.util.Arrays;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int a = in.nextInt(), b = in.nextInt();
    boolean s[] = new boolean[b+1];
    Arrays.fill(s, true);

    s[1] = false;
    for(int i=2; i<s.length; i++)
      if(s[i])
        for(int j=2*i; j<s.length; j+=i)
          s[j] = false;

    StringBuilder sb = new StringBuilder();
    while(a <= b) {
      if(s[a])
        sb.append(' ').append(a);
      a++;
    }
    System.out.println(sb.length() > 1 ? sb.substring(1) : "");
  }
}
