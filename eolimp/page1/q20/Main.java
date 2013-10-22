package page1.q20;

import java.util.Scanner;

public class Main {

  public static void main(String[] args) {

    int n = new Scanner(System.in).nextInt();

    int cnt=0, i;
    String s;

    while(n>0) {
      s = String.valueOf(n);
      for(i=0; i<s.length(); i++)
        n -= (s.charAt(i) - '0');
      cnt++;
    }

    System.out.println(cnt);
  }

}