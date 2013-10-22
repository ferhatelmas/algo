package page10.q927;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {

  public static void main(String[] args) throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    int n = Integer.parseInt(br.readLine()), cnt=0, tmp;
    double val;
    String[] s;

    for(int i=0; i<n; i++) {
      s = br.readLine().split(" ");
      tmp = Integer.parseInt(s[0]);
      val = Double.parseDouble(s[1]);
      if(val<50) cnt += tmp;
    }
    System.out.println(cnt);
  }

}