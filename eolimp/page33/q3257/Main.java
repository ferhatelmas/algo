package page33.q3257;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int x = in.nextInt(), y = in.nextInt(),
        ns[][] = new int[Math.max(x, y)+1][Math.max(x, y)+1];

    for(int i=0; i<ns.length; i++) {
      for(int j=0; j<ns.length; j++) {

        if(i == 0 && j == 0) ns[i][j] = 1;
        else {
          if(i >= j && (i%2 ==0 || j%2 == 0)) {
            ns[i][j] = ((i > 0 ? ns[i-1][j] : 0) + (j > 0 ? ns[i][j-1] : 0)) % 1000000007;
          }
        }
      }
    }

    System.out.println(ns[x][y]);
  }
}
