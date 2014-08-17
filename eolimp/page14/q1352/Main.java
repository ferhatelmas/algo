package page14.q1352;

import java.util.Arrays;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    int k = new Scanner(System.in).nextInt(), c = 0, n = 0;
    boolean bs[] = new boolean[1000001];
    Arrays.fill(bs, true);

    for(int i=2; i<bs.length; i++) {
      if(bs[i]) {
        c++;
        n += i;
        if(n%k == 0) {
          System.out.println(c);
          break;
        }
        for(int j=2*i; j<bs.length; j += i)
          bs[j] = false;
      }
    }
  }
}
