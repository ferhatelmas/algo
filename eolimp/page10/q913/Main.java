package page10.q913;

import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.util.ArrayList;
import java.text.DecimalFormat;

public class Main {

  public static void main(String[] args) throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    ArrayList<String> list = new ArrayList<String>();
    int n=Integer.parseInt(br.readLine());
    double d1, d2;
    String[] s;
    DecimalFormat df = new DecimalFormat("#########0.0000");
    for(int i=0;i<n; i++){
      s=br.readLine().split(" ");
      d1=Double.parseDouble(s[0]);
      d2=Double.parseDouble(s[1]);
      list.add(df.format(d1+d2).replace(",", "."));
      list.add(df.format(d1*d2).replace(",", "."));
    }

    for(int i=0; i<list.size(); i+=2) {
      System.out.print(list.get(i) + " ");
      System.out.println(list.get(i+1));
    }
  }

}