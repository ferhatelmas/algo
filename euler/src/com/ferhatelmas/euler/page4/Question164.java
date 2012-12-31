package com.ferhatelmas.euler.page4;

import java.util.HashMap;

public class Question164 {
  // generic consecutive sum
  private static int consecutiveCnt = 3;
  private static int digitCnt = 20;

  private static HashMap<String, Long> cache = new HashMap<String, Long>();

  public static void main(String[] args) {
    System.out.println(count(new int[digitCnt], 0));
  }

  private static long count(int[] n, int o) {
    if(o >= n.length) return 1;

    String key = getKey(n, o);
    if(cache.containsKey(key)) return cache.get(key);

    long cnt = 0;
    int low = o==0?1:0, high = 10;
    if(o >= consecutiveCnt-1)
      for(int i=consecutiveCnt-1; i>0; i--)
        high -= n[o-i];

    for(int i=low; i<high; i++) {
      n[o] = i;
      cnt += count(n, o+1);
    }
    cache.put(key, cnt);
    return cnt;
  }

  private static String getKey(int[] n, int o) {
    StringBuilder sb = new StringBuilder();
    for(int i=Math.max(o-consecutiveCnt+1, 0); i<o; i++)
      sb.append(n[i]);
    sb.append(":");
    sb.append(o);
    return sb.toString();
  }
}
