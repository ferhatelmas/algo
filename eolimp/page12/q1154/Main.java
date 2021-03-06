package page12.q1154;

import java.util.Scanner;
import java.util.ArrayList;

public class Main {

  public static void main(String[] args) {

    Scanner in = new Scanner(System.in);

    ArrayList<String> list=new ArrayList<String>();
    int m,n,l,i,cnt;

    while(in.hasNextInt()) {

      m=in.nextInt();
      n=in.nextInt();
      l=lcm(m,n);
      cnt=0;

      for(i=1; i<=l; i+=n) cnt++;

      if(cnt==m) list.add("YES");
      else list.add("NO");

    }
    for(String s : list) System.out.println(s);
  }

  private static int gcd(int a, int b) {
    return b == 0 ? a : gcd(b, a%b);
  }

  private static int lcm(int a, int b) {
    return (a*b)/gcd(a,b);
  }

}