package page2.q145;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;

public class Main {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    HashMap<String, Integer> segments = new HashMap<String, Integer>();
    br.readLine();
    for(String s : br.readLine().split(" ")) {
      if(segments.containsKey(s)) segments.put(s, segments.get(s)+1);
      else segments.put(s, 1);
    }

    int cnt = 0;
    for(int v : segments.values())
       cnt += v/4;
    System.out.println(cnt);
  }
}
