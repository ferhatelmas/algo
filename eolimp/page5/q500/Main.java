package page5.q500;

import java.util.Scanner;

public class Main {

  public static void main(String[] args) {

    Scanner in = new Scanner(System.in);

    int n = in.nextInt();
    int l,w,h;

    for(int i=0; i<n; i++) {
      l=in.nextInt();
      w=in.nextInt();
      h=in.nextInt();
      System.out.println((int)Math.ceil(((l+w)*h)/8.0));
    }
  }

}
