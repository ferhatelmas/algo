package page8.q773;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    int n = new Scanner(System.in).nextInt();
    System.out.println(solve(new char[n], 0));
  }

  private static int solve(char c[], int offset) {
    if(offset == c.length) return 1;

    int cmp = next(c, offset), sum = 0;
    if(cmp <= 0) {
      c[offset] = '1';
      sum += solve(c, offset+1);
    }
    if(cmp >= 0){
      c[offset] = '2';
      sum += solve(c, offset+1);
    }
    return sum;
  }

  private static int next(char c[], int offset) {
    if(offset < 2) return 0;
    else {
      if(c[offset-1] == '1' && c[offset-2] == '1') return 1;
      if(c[offset-1] == '2' && c[offset-2] == '2') return -1;
      return 0;
    }
  }
}
