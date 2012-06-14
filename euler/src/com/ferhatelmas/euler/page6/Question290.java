package com.ferhatelmas.euler.page6;

import java.util.HashMap;

public class Question290 {

  public static void main(String[] args) {

    HashMap<Key, Long> cache = new HashMap<Key, Long>();
    cache.put(new Key(0, 0), 1L);

    for(int i=0; i<18; i++) {
      HashMap<Key, Long> newCache = new HashMap<Key, Long>();

      for(int j=0; j<10; j++) {
        for(Key key : cache.keySet()) {
          int newCarry = key.getCarry() + 137*j;
          int newDiff = key.getDiff() + j - (newCarry%10);

          Key newKey = new Key(newDiff, newCarry/10);
          if(newCache.containsKey(newKey)) {
            newCache.put(newKey, newCache.get(newKey) + cache.get(key));
          } else {
            newCache.put(newKey, cache.get(key));
          }
        }
      }
      cache = newCache;
    }

    long count = 0;
    for(Key key : cache.keySet()) {
      if(key.getDiff() == getDigitSum(key.getCarry())) count += cache.get(key);
    }

    System.out.println(count);
  }

  private static int getDigitSum(long l) {

    String s = String.valueOf(l);
    int sum = 0;
    for(int i=0; i<s.length(); i++) {
      sum += s.charAt(i) - '0';
    }

    return sum;
  }

}

class Key {
  private int diff;
  private int carry;

  Key(int diff, int carry) {
    this.diff = diff;
    this.carry = carry;
  }

  public int getDiff() {
    return diff;
  }

  public int getCarry() {
    return carry;
  }

  public int hashCode() {
    return String.valueOf(diff).hashCode() ^ String.valueOf(carry).hashCode();
  }

  public boolean equals(Object o) {
    if(o instanceof Key) {
      Key key = (Key)o;
      return this.diff == key.getDiff() && this.carry == key.getCarry();
    }
    return false;
  }
}
