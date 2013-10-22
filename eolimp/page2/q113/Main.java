package page2.q113;

import java.util.Scanner;
import java.util.HashMap;

public class Main {

  public static void main(String[] args) {

    Scanner in = new Scanner(System.in);
    HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();

    int n = in.nextInt();
    int i, tmp, cnt, max = 0;

    for(i=0; i<n; i++) {
      tmp=in.nextInt();
      if(map.containsKey(tmp)) {
        cnt=map.get(tmp);
        cnt++;
        map.put(tmp, cnt);
        if(cnt > max) max = cnt;
      } else {
        map.put(tmp, 1);
        if(1>max) max=1;
      }
    }

    System.out.println(n-max);
  }

}