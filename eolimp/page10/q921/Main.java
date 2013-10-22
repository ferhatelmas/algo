package page10.q921;

import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.text.DecimalFormat;

public class Main {

  public static void main(String[] args) throws Exception{

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    int n = Integer.parseInt(br.readLine()), cnt=0;
    String[] s=br.readLine().split(" ");
    double d, sum=0;
    for(int i=0; i<s.length;i++) {
      d=Double.parseDouble(s[i]);
      if(d<0){
        cnt++;
        sum+=d;
      }
    }
    System.out.println(cnt + " " + new DecimalFormat("#########0.00").format(sum).replace(",", "."));
  }

}