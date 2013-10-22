package page23.q2262;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    boolean[] b = new boolean[10];
    for(int i=0; i<10; i++)
      b[i] = in.nextInt() == 1;

    boolean r = false;
    for(int i=0; i<9; i++)
      for(int j=i+1; j<10; j++)
        r ^= (b[i] || b[j]);

    for(int i=0; i<8; i++)
      for(int j=i+1; j<9; j++)
        for(int k=j+1; k<10; k++)
          r ^= (b[i] || b[j] || b[k]);
    System.out.println(r ? "1" : "0");
  }
}
