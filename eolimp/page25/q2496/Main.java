package page25.q2496;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    char c[] = new Scanner(System.in).nextLine().toCharArray();
    StringBuilder sb = new StringBuilder();
    boolean f = false;
    for(int i=0, j=0; i<c.length; i++) {
      if(c[i] == '(') {
        f = true;
        j = i;
      } else if(c[i] == ')') {
        f = false;
        for(int k=i-1; k>j; k--)
          sb.append(c[k]);
      } else if(!f)
        sb.append(c[i]);
    }
    System.out.println(sb.toString());
  }
}
