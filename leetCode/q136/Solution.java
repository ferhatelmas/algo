package q136;

public class Solution {
  public int singleNumber(int[] A) {
    int r = 0;
    for(int i : A) r ^= i;
    return r;
  }
}
