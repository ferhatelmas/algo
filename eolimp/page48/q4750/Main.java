package page48.q4750;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    int n = new Scanner(System.in).nextInt();

    for(int i=0; i<n; i++) {
      if(i%2 == 0)
        System.out.println(getRow(i*n+1, (i+1)*n));
      else
        System.out.println(getRow((i+1)*n, i*n+1));
    }
  }

  private static String getRow(int i, int j) {
    StringBuilder sb = new StringBuilder();
    int rep = i < j ? 1 : -1;
    while(i != j) {
      sb.append(i).append(' ');
      i += rep;
    }
    sb.append(j);
    return sb.toString();
  }
}
