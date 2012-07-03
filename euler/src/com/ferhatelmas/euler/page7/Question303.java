package com.ferhatelmas.euler.page7;

import java.util.ArrayList;
import java.util.regex.Pattern;

public class Question303 {

  private static ArrayList<Integer> numbers;
  private static long sum = 0;

  private static Pattern pattern = Pattern.compile(".*[^012].*");

  public static void main(String[] args) {

    numbers = new ArrayList<Integer>();
    for(int i=1; i<10001; i++) {
      if(i == 9 || i == 99 || i == 999 || i == 9999) continue;
      numbers.add(i);
    }

    sum += 1358; // 9
    sum += 11335578; // 99
    sum += 111333555778l; // 999
    sum += 1111333355557778l; // 9999

    int depth = 1;
    while(true) {
      yield(new StringBuffer(), depth);
      depth++;
    }


    //System.out.println(sum);
  }

  private static void yield(StringBuffer sb, int depth) {

    if(depth == 0) {
      long l = Long.parseLong(sb.toString());

      ArrayList<Integer> tobeRemoved = new ArrayList<Integer>();
      for(int i : numbers) {
        if(i > l) break;
        if(l%i == 0) {
          tobeRemoved.add(i);
          sum += l/i;
        }
      }
      for(int i : tobeRemoved) numbers.remove((Integer)i);
      if(numbers.size() == 0) {
        System.out.println(sum);
        System.exit(0);
      }
      return;
    }

    for(int i=0; i<3; i++) {
      if(i==0 && sb.length() == 0) continue;
      sb.append((char) (48 + i));
      yield(sb, depth-1);
      sb.deleteCharAt(sb.length()-1);
    }

  }

  // brute F to get values for 9, 99, ...
  private static int getF(int n) {

    int cnt = 1;
    long r = n;

    while(pattern.matcher(String.valueOf(r)).matches()) {
      cnt++;
      r += n;
    }

    return cnt;
  }

}
