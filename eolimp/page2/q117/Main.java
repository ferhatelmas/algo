package page2.q117;

import java.util.Scanner;

public class Main {

  public static void main(String[] args) {

    Scanner in = new Scanner(System.in);
    int n = in.nextInt(), m = in.nextInt(), sum = 0;
    int l[] = new int[n];
    for(int i=0; i<n; i++) {
      l[i] = in.nextInt();
      sum += l[i];
    }

    int max = sum / m;
    while(max > 0 && !isFine(l, max, m)) max--;
    System.out.println(max);

  }

  private static boolean isFine(int l[], int max, int m) {
    int cnt = 0;
    for(int i : l) cnt += i/max;
    return cnt >= m;
  }

}
