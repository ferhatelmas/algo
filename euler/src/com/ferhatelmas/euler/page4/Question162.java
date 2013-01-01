package com.ferhatelmas.euler.page4;

import java.util.HashMap;

public class Question162 {

  private static char[] alphabet = "0123456789ABCDEF".toCharArray();

  private static HashMap<String, Long> cache = new HashMap<String, Long>();

  public static void main(String[] args) {
    System.out.println(Long.toHexString(count(new char[alphabet.length], 0)).toUpperCase());
  }

  private static long count(char[] chars, int o) {
    if(o >= chars.length) return 0;

    int i0 = index(chars, o, '0'),
        i1 = index(chars, o, '1'),
        iA = index(chars, o, 'A');

    String key = i0 + ":" + i1 + ":" + iA + ":" + o;
    if(cache.containsKey(key)) return cache.get(key);

    long cnt = 0;
    for(int i=o==0?1:0; i<alphabet.length; i++) {
      if(isValid(i0, i1, iA, alphabet[i])) cnt += add(alphabet.length-o);
      else {
      chars[o] = alphabet[i];
      cnt += count(chars, o+1);
      }
    }

    cache.put(key, cnt);
    return cnt;
  }

  private static long add(int o) {
    long sum = 0;
    for(int i=0; i<o; i++)
      sum += Math.pow(alphabet.length, i);
    return sum;
  }

  private static boolean isValid(int i0, int i1, int iA, char c) {
    return (i0 > -1 && i1 > -1 && iA == -1 && c == 'A') ||
           (i0 > -1 && i1 == -1 && iA > -1 && c == '1') ||
           (i0 == -1 && i1 > -1 && iA > -1 && c == '0');
  }

  private static int index(char[] chars, int o, char c) {
    for(int i=0; i<o; i++)
      if(chars[i] == c) return i;
    return -1;
  }
}
