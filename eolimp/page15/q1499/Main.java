package page15.q1499;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    String s = in.nextLine(), b = in.nextLine();

    for(int i=0, l=s.length(); i<l; i++) {
      if((s.substring(l-i) + s.substring(0, l-i)).equals(b)) {
        System.out.println(i);
        return;
      }
    }
    System.out.println(-1);
  }
}
