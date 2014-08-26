package vol12.p2105;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int t = in.nextInt();

    while(t-- > 0) {
      String line = in.next();
      for(int i=0; i<32; i+=8) {
        System.out.print(Integer.parseInt(line.substring(i, i+8), 2));
        if(i != 24) System.out.print(".");
      }
      System.out.println();
    }
  }

}
